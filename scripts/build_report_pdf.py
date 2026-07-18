#!/usr/bin/env python3
"""
Build a styled GEO report HTML from a markdown audit, without pandoc.

Why this exists
---------------
The documented geo-report-pdf pipeline uses pandoc to fill the bundled
template. On machines without pandoc (and without Homebrew to install it),
this script performs the same job: it renders the markdown, resolves the
pandoc-style placeholders in geo-report-template.html, inlines the CSS, and
writes a self-contained HTML file ready for Chrome headless to print.

Usage
-----
    build_report_pdf.py <report.md> <out.html> key=value [key=value ...]

Recognised keys (all optional; the template has defaults):
    title, brand_name, domain, geo_score, score_label,
    date, business_type, locations, platform
    footer   -- overrides the @page bottom-center footer string

Notes
-----
* Pass geo_score explicitly. If omitted, the template falls back to a
  placeholder score, which would put a fabricated number on the cover of
  a client deliverable. For a partial audit with no composite, pass
  something non-numeric, e.g. geo_score=— score_label="Partial audit".
* Requires the `markdown` package in the active interpreter.
"""
import re
import sys
import pathlib

TPL = pathlib.Path.home() / ".claude/skills/geo/templates/geo-report-template.html"
CSS = pathlib.Path.home() / ".claude/skills/geo/templates/geo-report-style.css"

# The default footer declaration in the bundled CSS, replaced when footer= is given.
FOOTER_RE = re.compile(r'(@bottom-center\s*\{[^}]*?content:\s*)"[^"]*"')


def build(md_path: pathlib.Path, out_path: pathlib.Path, meta: dict) -> str:
    import markdown

    # $title$ is not wrapped in a pandoc conditional, so it would leak literally
    # into <title> if unset. Derive a sensible default.
    meta.setdefault(
        "title",
        f"GEO Audit Report — {meta['brand_name']}" if meta.get("brand_name")
        else "GEO Audit Report",
    )

    body = markdown.markdown(
        md_path.read_text(encoding="utf-8"),
        extensions=["tables", "fenced_code", "attr_list", "sane_lists"],
    )

    css = CSS.read_text(encoding="utf-8")
    if meta.get("footer"):
        css, n = FOOTER_RE.subn(lambda m: m.group(1) + '"%s"' % meta["footer"], css)
        if not n:
            print("WARNING: footer override requested but the @bottom-center "
                  "rule was not found in the CSS — footer left unchanged.",
                  file=sys.stderr)

    t = TPL.read_text(encoding="utf-8")

    # $if(key)$A$else$B$endif$  ->  A when key set, else B
    t = re.sub(r'\$if\((\w+)\)\$(.*?)\$else\$(.*?)\$endif\$',
               lambda m: m.group(2) if meta.get(m.group(1)) else m.group(3),
               t, flags=re.S)
    # $if(key)$A$endif$
    t = re.sub(r'\$if\((\w+)\)\$(.*?)\$endif\$',
               lambda m: m.group(2) if meta.get(m.group(1)) else '',
               t, flags=re.S)
    # $for(css)$...$endfor$  ->  inlined stylesheet (pandoc --embed-resources)
    t = re.sub(r'\$for\(css\)\$.*?\$endfor\$',
               "<style>\n" + css + "\n</style>", t, flags=re.S)

    for k, v in meta.items():
        t = t.replace(f"${k}$", v)
    t = t.replace("$body$", body)
    # pandoc escapes a literal '$' as '$$'; unescape inside the template's JS regex
    t = t.replace(r"/100$$/", r"/100$/")

    out_path.write_text(t, encoding="utf-8")
    return t


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__.strip())
        return 2

    md_path = pathlib.Path(sys.argv[1])
    out_path = pathlib.Path(sys.argv[2])
    if not md_path.is_file():
        print(f"ERROR: no such report: {md_path}", file=sys.stderr)
        return 1

    meta = {}
    for arg in sys.argv[3:]:
        if "=" not in arg:
            print(f"ERROR: expected key=value, got {arg!r}", file=sys.stderr)
            return 2
        k, v = arg.split("=", 1)
        meta[k] = v

    t = build(md_path, out_path, meta)

    leftover = set(re.findall(r'\$[a-z_]+\$', t))
    print(f"wrote {out_path} ({len(t):,} bytes)")
    print(f"unresolved placeholders: {leftover or 'none'}")
    if meta.get("footer"):
        print(f"footer: {meta['footer']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
