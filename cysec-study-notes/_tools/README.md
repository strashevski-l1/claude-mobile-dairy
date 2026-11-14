# Повторная выгрузка

```bash
mkdir -p pages
curl -sSL -A "Mozilla/5.0" https://www.exampasscy.com/sitemap.xml | grep -o '<loc>[^<]*/study-notes[^<]*' | sed 's/<loc>//' > notes.txt
while read u; do p=${u#https://www.exampasscy.com/}; curl -sSL -A "Mozilla/5.0" -o "pages/$(echo $p | tr / _).html" "$u"; sleep 0.3; done < notes.txt
python3 convert.py pages out && python3 build_index.py out   # нужны beautifulsoup4 и markdownify
```
