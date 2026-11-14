"""Convert downloaded exampasscy.com study-notes HTML pages into a linked Markdown manual."""
import os, re, sys, json
from bs4 import BeautifulSoup, NavigableString, Comment
from markdownify import MarkdownConverter

SITE = "https://www.exampasscy.com"
PAGES_DIR, OUT = sys.argv[1], sys.argv[2]
TOP_LEVEL = {"advanced", "basic", "aml", "about"}

# Headings whose blocks are product/marketing, not learning content.
DROP_HEADINGS = [
    r"^recent regulatory updates", r"^revise this chapter", r"^practise", r"^test what you just read",
    r"^start with 10 free", r"^read, flip", r"^how these notes are written", r"^try ", r"^get all-in-one",
]


def url_to_path(url_path):
    """/study-notes/... -> output file path relative to OUT."""
    parts = [p for p in url_path.strip("/").split("/") if p]
    assert parts[0] == "study-notes", url_path
    parts = parts[1:]
    if not parts:
        return "README.md"
    if len(parts) == 1:
        return f"{parts[0]}.md" if parts[0] in TOP_LEVEL else f"{parts[0]}/README.md"
    return f"{parts[0]}/{parts[1]}.md"


def rewrite_href(href, cur):
    if not href:
        return href
    if href.startswith(SITE):
        href = href[len(SITE):] or "/"
    if href.startswith("#") or href.startswith("mailto:"):
        return href
    if href.startswith("/study-notes"):
        path, _, frag = href.partition("#")
        target = url_to_path(path)
        rel = os.path.relpath(target, os.path.dirname(cur) or ".")
        return rel + ("#" + frag if frag else "")
    if href.startswith("/"):
        return SITE + href
    return href


def text_of(el):
    return re.sub(r"\s+", " ", el.get_text(" ", strip=True)).strip()


def heading_text(sec):
    h = sec.find(["h2", "h3"])
    return text_of(h).lower() if h else ""


def is_drop(t):
    return any(re.search(p, t) for p in DROP_HEADINGS)


def clean(soup, main, cur):
    for x in main.find_all(["script", "style", "noscript", "svg", "button", "form"]):
        x.decompose()
    for c in main.find_all(string=lambda s: isinstance(s, Comment)):
        c.extract()
    # visually hidden helper text such as "(opens in a new tab)"
    for x in main.find_all(class_="sr-only"):
        x.decompose()
    # site footer
    for x in main.find_all("footer"):
        if "ExamPass CY" in text_of(x) and ("LinkedIn" in text_of(x) or "Report an error" in text_of(x) or "How we write" in text_of(x)):
            x.decompose()
    # sidebars (chapter topic list, "On this page"); we rebuild navigation ourselves
    for x in main.find_all("aside"):
        t = heading_text(x)
        if is_drop(t) or x.find("nav") or "on this page" in text_of(x).lower()[:40]:
            x.decompose()
    # mobile duplicate of sidebar topic list
    for x in main.find_all("div", class_="xl:hidden"):
        x.decompose()
    for x in main.find_all("details"):
        if "on this page" in text_of(x).lower()[:40] or "topics" in text_of(x.find("summary") or x).lower()[:60]:
            x.decompose()
    # marketing / product blocks identified by heading
    for h in main.find_all(["h2", "h3"]):
        if h.decomposed if hasattr(h, "decomposed") else False:
            continue
        if is_drop(text_of(h).lower()):
            blk = h.find_parent(["section", "aside"]) or h.parent
            if blk is not None and blk is not main:
                blk.decompose()
    # any remaining block that sells something (links to pricing/demo/auth)
    for a in main.find_all("a", href=re.compile(r"^(/pricing|/demo|/auth|/flashcards)")):
        if a.decomposed if hasattr(a, "decomposed") else False:
            continue
        blk = a.find_parent(["section", "aside", "div"])
        txt = text_of(a)
        a.decompose()
        if blk is not None and blk is not main and not blk.find(["h1", "h2", "table", "dl"]) and len(text_of(blk)) < 300 \
                and re.search(r"flashcard|free questions|All-in-One|€\d+ ?$|Practise", text_of(blk)):
            blk.decompose()
    # paragraphs left empty or pure promos
    for p in main.find_all("p"):
        t = text_of(p)
        if re.search(r"Get All-in-One|Or just this chapter|free flashcards|free questions|free Basic questions|questions in the .{0,30}bank", t):
            p.decompose()
    # "Tested in" chips -> plain text line
    for d in main.find_all("div"):
        sp = d.find("span", recursive=False)
        if sp and text_of(sp) == "Tested in":
            items = [text_of(a) for a in d.find_all("a")]
            new = soup.new_tag("p")
            new.string = "Tested in: " + ", ".join(items)
            d.replace_with(new)
    # Previous / next nav -> simple line
    for nav in main.find_all("nav"):
        if nav.find("ol") and "Home" in text_of(nav)[:10]:
            continue  # breadcrumb handled separately
        links = nav.find_all("a")
        if links and all(len(a.find_all("span")) >= 2 for a in links):
            p = soup.new_tag("p")
            for i, a in enumerate(links):
                spans = a.find_all("span")
                label, title = text_of(spans[0]), text_of(spans[1])
                if i:
                    p.append(" | ")
                na = soup.new_tag("a", href=a["href"])
                na.string = f"{label} {title}" if "→" not in label else f"{title} {label}"
                if label.startswith("←"):
                    na.string = f"{label} {title}"
                elif label.endswith("→"):
                    na.string = f"{label.rstrip('→ ').strip()}: {title} →"
                p.append(na)
            hr = soup.new_tag("hr")
            nav.replace_with(hr)
            hr.insert_after(p)
    # Block-level card links: flatten into "**[title](href)** — details"
    for a in main.find_all("a"):
        if not a.find(["span", "div", "h3", "h4", "p"]):
            continue
        if a.find_parent("td"):
            na = soup.new_tag("a", href=a["href"])
            na.string = text_of(a)
            a.replace_with(na)
            continue
        li = a.find_parent("li")
        if li is not None and li.parent is not None and li.parent.name == "ol":
            li.parent.name = "ul"
        leaves = [s for s in a.find_all(["span", "h3", "h4", "p", "div"]) if not s.find(["span", "h3", "h4", "p", "div"])]
        leaves = [l for l in leaves if text_of(l)]
        if not leaves:
            continue
        title_el = next((l for l in leaves if l.name in ("h3", "h4")), None) or \
            next((l for l in leaves if any("font-semibold" in c or "font-bold" in c for c in (l.get("class") or [])) and not l.get("aria-hidden") and len(text_of(l)) > 3), None) or leaves[0]
        before = [text_of(l) for l in leaves[: leaves.index(title_el)]]
        before = [b + "." if b.isdigit() else b for b in before]
        after = [text_of(l) for l in leaves[leaves.index(title_el) + 1:]]
        p = soup.new_tag("p")
        if before:
            p.append(" ".join(before).rstrip(".") + ". ")
        na = soup.new_tag("a", href=a["href"])
        na.string = text_of(title_el)
        st = soup.new_tag("strong")
        st.append(na)
        p.append(st)
        if after:
            p.append(" — " + " · ".join(after))
        a.replace_with(p)
    # decorative numbers inside list items ("1. 1")
    for li in main.find_all("li"):
        for sp in li.find_all("span", attrs={"aria-hidden": "true"}):
            sp.decompose()
    # keep in-page anchors: put <a id> before headings/sections that carry an id
    for el in main.find_all(attrs={"id": True}):
        if el.name in ("main",):
            continue
        h = el if el.name in ("h1", "h2", "h3", "h4") else el.find(["h2", "h3", "h4"])
        if h is not None:
            h.insert(0, NavigableString(f"\x00ANCHOR:{el['id']}\x00"))
    # links
    for a in main.find_all("a", href=True):
        a["href"] = rewrite_href(a["href"], cur)
        if a["href"].startswith("mailto:"):
            a.unwrap()


class Conv(MarkdownConverter):
    def convert_dl(self, el, text, *args, **kw):
        return "\n\n" + text + "\n\n"

    def convert_dt(self, el, text, *args, **kw):
        return f"\n- **{text.strip()}**"

    def convert_dd(self, el, text, *args, **kw):
        return f" — {text.strip()}\n"


def to_md(html):
    md = Conv(heading_style="ATX", bullets="-", escape_underscores=False, escape_asterisks=False).convert(html)
    md = re.sub(r"(#+ )((?:\x00ANCHOR:[^\x00]+\x00\s*)+)", lambda m: "".join(f'<a id="{i}"></a>' for i in re.findall(r"ANCHOR:([^\x00]+)", m.group(2))) + "\n\n" + m.group(1), md)
    md = re.sub(r"\x00ANCHOR:([^\x00]+)\x00", "", md)
    md = re.sub(r'<a id="([^"]+)-h"></a>(?=<a id="\1"></a>)', "", md)
    md = re.sub(r"^(\s*[-*] )#{1,6} (.+)$", r"\1**\2**", md, flags=re.M)
    md = re.sub(r"^(\s*)(Exam material|Current law[^:\n]*|Today|In the exam):", r"\1**\2:**", md, flags=re.M)
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\s*·\s*", " · ", md)
    md = re.sub(r"^ · ", "", md, flags=re.M)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


def breadcrumb(main, cur):
    ol = None
    for nav in main.find_all("nav"):
        if nav.find("ol") and text_of(nav).startswith("Home"):
            ol = nav
            break
    if not ol:
        return "", None
    items = []
    for li in ol.find_all("li"):
        a = li.find("a")
        if a and a.get("href", "").startswith("/study-notes"):
            items.append(f"[{text_of(a)}]({rewrite_href(a['href'], cur)})")
        elif a:
            continue  # Home -> product site, skip
        else:
            items.append(text_of(li).strip(" /"))
    ol.decompose()
    return " › ".join(items), None


def main_entry():
    os.makedirs(OUT, exist_ok=True)
    meta = {}
    for fn in sorted(os.listdir(PAGES_DIR)):
        url = "/" + fn[:-5].replace("_", "/")
        cur = url_to_path(url)
        soup = BeautifulSoup(open(os.path.join(PAGES_DIR, fn), encoding="utf-8").read(), "html.parser")
        title = text_of(soup.find("h1")) if soup.find("h1") else url
        main = soup.find("article") or soup.find("main")
        crumbs, _ = breadcrumb(soup.find("main"), cur)
        clean(soup, main, cur)
        body = to_md(str(main))
        header = f"> {crumbs}  \n> Source: <{SITE}{url}>\n\n" if crumbs else f"> Source: <{SITE}{url}>\n\n"
        dest = os.path.join(OUT, cur)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "w", encoding="utf-8").write(header + body)
        meta[cur] = {"url": url, "title": title}
    json.dump(meta, open(os.path.join(OUT, ".pages.json"), "w"), indent=1)
    print(len(meta), "pages written")


main_entry()
