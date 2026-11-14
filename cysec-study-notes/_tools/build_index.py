"""Post-process the converted manual: tidy index lines and build a full table of contents."""
import os, re, sys

OUT = sys.argv[1]
LINK = re.compile(r"\*\*\[([^\]]+)\]\(([^)]+)\)\*\*")


def read(p):
    return open(os.path.join(OUT, p), encoding="utf-8").read()


def write(p, t):
    open(os.path.join(OUT, p), "w", encoding="utf-8").write(t)


# 1. tidy card lines everywhere
for root, _, files in os.walk(OUT):
    for f in files:
        if f.endswith(".md"):
            p = os.path.relpath(os.path.join(root, f), OUT)
            t = read(p)
            t = re.sub(r" · →$", "", t, flags=re.M)
            t = re.sub(r"Also · (Advanced|Basic|AML) · Ch (\d+)", r"Also \1 Ch \2", t)
            t = re.sub(r" · (Advanced|Basic|AML) · Ch (\d+)", r", \1 Ch \2", t)
            write(p, t)


def subjects_from(index_md):
    """Ordered (chapter label, title, subject dir) from advanced.md / aml.md."""
    res = []
    for line in read(index_md).splitlines():
        m = re.match(r"- (.*?)\. \*\*\[([^\]]+)\]\(([^)]+)\)\*\*", line)
        if m and m.group(3).endswith("/README.md"):
            res.append((m.group(1), m.group(2), m.group(3).split("/")[0]))
        elif m:
            res.append((m.group(1), m.group(2), None))
    return res


def topics_of(subject):
    """Groups -> [(num, title, file)] from a subject README's topic list."""
    t = read(f"{subject}/README.md")
    sec = re.search(r"\n## The \d+ topics?\n(.*?)(\n## |\Z)", t, re.S)
    body = sec.group(1) if sec else t
    groups, cur = [], None
    for line in body.splitlines():
        if line.startswith("### "):
            cur = (line[4:].strip(), [])
            groups.append(cur)
            continue
        m = re.match(r"- (\d+)\. \*\*\[([^\]]+)\]\(([^)#]+)\)\*\*", line)
        if m:
            if cur is None:
                cur = ("", [])
                groups.append(cur)
            cur[1].append((m.group(1), m.group(2), m.group(3)))
    return groups


all_subjects = sorted(d for d in os.listdir(OUT) if os.path.isdir(os.path.join(OUT, d)))
lines = [
    "# Полное оглавление — CySEC study notes",
    "",
    "Все главы и темы в порядке программы. Каждая тема — отдельный файл; внутри: короткий ответ, таблица ключевых фактов, ",
    "разбор, глоссарий, «Exam material vs Current law», типичные ошибки, ссылки на закон и связанные темы.",
    "",
    "Навигация: [Главная](README.md) · [Advanced](advanced.md) · [Basic](basic.md) · [AML](aml.md)",
    "",
]
seen, total = set(), 0


def emit(label, title, subj):
    global total
    lines.append(f"### {label}. [{title}]({subj}/README.md)")
    lines.append("")
    for g, items in topics_of(subj):
        if g:
            lines.append(f"- *{g}*")
        for num, ttl, f in items:
            lines.append(f"{'  ' if g else ''}- {num}. [{ttl}]({subj}/{f})")
            total += 1
    lines.append("")
    seen.add(subj)


lines += ["## CySEC Advanced", ""]
for label, title, subj in subjects_from("advanced.md"):
    if subj:
        emit(label, title, subj)
    else:
        lines += [f"### {label}. [{title}](aml.md) — см. раздел AML ниже", ""]
lines += ["## CySEC AML", ""]
for label, title, subj in subjects_from("aml.md"):
    if subj and subj not in seen:
        emit(label, title, subj)
rest = [s for s in all_subjects if s not in seen]
if rest:
    lines += ["## Прочее", ""]
    for s in rest:
        emit("Subject", s, s)
lines += ["## CySEC Basic", "",
          "Basic использует те же заметки, в другом порядке глав — соответствие см. в [basic.md](basic.md).", ""]
write("INDEX.md", "\n".join(lines))
print("subjects", len(seen), "topics", total)
