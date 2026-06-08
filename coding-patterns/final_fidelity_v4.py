"""
DEFINITIVE JSON-to-MARKDOWN FIDELITY CHECK - Final Version
============================================================
Correctly handles all edge cases:
- Unicode escapes (\\uXXXX, \\xHH)
- \\t only replaced when standalone (not inside \\text)
- KaTeX annotation double-backslashes -> single
- \\cdot -> middle dot (U+00B7)
- \\log -> log
- Non-breaking space \\xA0 -> regular space
- Curly quotes preserved
"""

import json
import re
import os
from collections import Counter

BASE = os.path.dirname(os.path.abspath(__file__))

CHAPTERS = [
    "03-two-pointers-triplet-sum",
    "46-heaps-k-most-frequent-strings",
    "74-tries-find-all-words-on-a-board",
    "97-dynamic-programming-longest-common-subsequence",
]


def unescape(s):
    """Unescape JSON/JSX strings, being careful not to corrupt \\text, \\node, etc."""
    s = re.sub(r'\\u([0-9a-fA-F]{4})', lambda m: chr(int(m.group(1), 16)), s)
    s = re.sub(r'\\x([0-9a-fA-F]{2})', lambda m: chr(int(m.group(1), 16)), s)
    # Only replace \n and \t when NOT followed by a letter (avoids corrupting \text, \node, etc.)
    s = re.sub(r'\\n(?![a-zA-Z])', '\n', s)
    s = re.sub(r'\\t(?![a-zA-Z])', '\t', s)
    s = s.replace('\\"', '"')
    return s


def normalize(s):
    """Normalize for comparison."""
    s = s.replace("\u00a0", " ")
    s = re.sub(r'\s+', ' ', s).strip()
    return s.lower()


def latex_to_md(s):
    """Convert LaTeX commands to their markdown equivalents."""
    # Halve double backslashes (KaTeX annotation -> raw LaTeX)
    s = s.replace("\\\\", "\\")
    # Convert LaTeX commands to unicode/text
    s = s.replace("\\cdot", "\u00b7")
    s = s.replace("\\log", "log")
    return s


def check_in_md(s, md_norm):
    """Check if string from JSON is present in markdown using multiple strategies."""
    # Strategy 1: Direct match
    sn = normalize(s)
    if sn in md_norm:
        return True, "direct"

    # Strategy 2: LaTeX conversions (\\cdot -> middle dot, \\log -> log, halve backslashes)
    s_latex = latex_to_md(s)
    s_latex_n = normalize(s_latex)
    if s_latex_n in md_norm:
        return True, "latex-converted"

    # Strategy 3: Strip formatting characters
    ss = re.sub(r'[*_`\[\](){}\\]', '', sn)
    md_stripped = re.sub(r'[*_`\[\](){}\\]', '', md_norm)
    if len(ss) > 15 and ss in md_stripped:
        return True, "stripped"

    # Strategy 4: Partial match (first 35 chars)
    if len(sn) > 20 and sn[:35] in md_norm:
        return True, "partial"

    return False, "NOT FOUND"


def analyze(name):
    json_path = os.path.join(BASE, "raw_json", name + ".json")
    md_path = os.path.join(BASE, name + ".md")

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    with open(md_path, 'r', encoding='utf-8') as f:
        md = f.read()

    code = data['pageProps']['code']
    md_norm = normalize(md)

    # === 1. TEXT STRINGS ===
    raw = re.findall(r'children:"((?:[^"\\]|\\.)*)"', code)
    strings = []
    seen = set()
    for s in raw:
        u = unescape(s)
        if len(u) > 15 and u not in seen:
            seen.add(u)
            strings.append(u)

    found = []
    missing = []
    methods = Counter()
    for s in strings:
        ok, method = check_in_md(s, md_norm)
        if ok:
            found.append((s, method))
            methods[method] += 1
        else:
            missing.append(s)

    # === 2. IMAGES ===
    json_imgs = len(re.findall(r'var \w+="(/images/[^"]+\.(?:svg|png|jpg|jpeg|gif))"', code))
    md_imgs = len(re.findall(r'!\[', md))

    # === 3. CODE BLOCKS ===
    json_pre = len(re.findall(r'\w\.pre,', code))
    md_fences = re.findall(r'^```(\w+)', md, re.MULTILINE)
    md_closings = len(re.findall(r'^```\s*$', md, re.MULTILINE))

    # === 4. LANGUAGE TAGS ===
    json_langs = re.findall(r'language-(\w+)', code)

    return {
        'name': name,
        'str_total': len(strings),
        'str_found': len(found),
        'str_missing': len(missing),
        'missing_list': missing,
        'methods': dict(methods),
        'json_imgs': json_imgs,
        'md_imgs': md_imgs,
        'json_pre': json_pre,
        'md_fences': len(md_fences),
        'md_closings': md_closings,
        'json_lang_counts': dict(Counter(json_langs)),
        'md_lang_counts': dict(Counter(md_fences)),
        'md_lang_set': sorted(set(md_fences)),
    }


def main():
    out = []
    def p(s=""):
        out.append(s)

    p("=" * 80)
    p("DEFINITIVE JSON-to-MARKDOWN FIDELITY CHECK")
    p("=" * 80)
    p()

    results = []
    for ch in CHAPTERS:
        r = analyze(ch)
        results.append(r)

        p("-" * 80)
        p("CHAPTER: " + r['name'])
        p("-" * 80)

        p()
        p("1. TEXT STRING FIDELITY")
        p("   Strings checked (>15 chars, unique): " + str(r['str_total']))
        p("   Found in markdown:                   " + str(r['str_found']))
        p("   Missing from markdown:               " + str(r['str_missing']))
        p("   Match methods: " + str(r['methods']))
        if r['missing_list']:
            p("   MISSING STRINGS:")
            for i, s in enumerate(r['missing_list'], 1):
                p("     " + str(i) + ". [" + str(len(s)) + " ch] " + repr(s[:200]))
        else:
            p("   >>> ALL STRINGS FOUND <<<")

        p()
        p("2. IMAGE COUNT")
        p("   JSON: " + str(r['json_imgs']) + "  |  MD: " + str(r['md_imgs']) +
          "  |  Match: " + ("YES" if r['json_imgs'] == r['md_imgs'] else "NO"))

        p()
        p("3. CODE BLOCK COUNT")
        p("   JSON pre: " + str(r['json_pre']) +
          "  |  MD fenced: " + str(r['md_fences']) +
          "  |  MD closings: " + str(r['md_closings']) +
          "  |  Match: " + ("YES" if r['json_pre'] == r['md_fences'] else "NO"))

        p()
        p("4. LANGUAGE TAGS")
        p("   JSON: " + str(r['json_lang_counts']))
        p("   MD:   " + str(r['md_lang_counts']))
        counts_match = r['json_lang_counts'] == r['md_lang_counts']
        p("   Per-language counts match: " + ("YES" if counts_match else "NO"))
        p("   python: " + ("YES" if "python" in r['md_lang_set'] else "NO") +
          "  |  java: " + ("YES" if "java" in r['md_lang_set'] else "NO") +
          "  |  javascript: " + ("YES" if "javascript" in r['md_lang_set'] else "NO"))
        p()

    # SUMMARY
    p("=" * 80)
    p("OVERALL SUMMARY")
    p("=" * 80)
    tc = sum(r['str_total'] for r in results)
    tf = sum(r['str_found'] for r in results)
    tm = sum(r['str_missing'] for r in results)
    pct = round(100.0 * tf / tc, 1) if tc > 0 else 0

    p()
    p("  Chapters analyzed:           4")
    p("  Total strings checked:       " + str(tc))
    p("  Total found:                 " + str(tf))
    p("  Total missing:               " + str(tm))
    p("  String fidelity:             " + str(pct) + "%")
    p()
    all_img = all(r['json_imgs'] == r['md_imgs'] for r in results)
    all_code = all(r['json_pre'] == r['md_fences'] for r in results)
    all_lang = all(r['json_lang_counts'] == r['md_lang_counts'] for r in results)
    p("  All image counts match:      " + ("YES" if all_img else "NO"))
    p("  All code block counts match: " + ("YES" if all_code else "NO"))
    p("  All lang tag counts match:   " + ("YES" if all_lang else "NO"))
    p()

    p("  Per-chapter breakdown:")
    p("  " + "-" * 76)
    fmt = "  {:<50s} {:>6s} {:>6s} {:>6s} {:>6s}"
    p(fmt.format("Chapter", "Str%", "Imgs", "Code", "Langs"))
    p("  " + "-" * 76)
    for r in results:
        pct_ch = "{:.1f}%".format(100.0 * r['str_found'] / r['str_total'])
        img_ok = "OK" if r['json_imgs'] == r['md_imgs'] else "FAIL"
        code_ok = "OK" if r['json_pre'] == r['md_fences'] else "FAIL"
        lang_ok = "OK" if r['json_lang_counts'] == r['md_lang_counts'] else "FAIL"
        p(fmt.format(r['name'][:50], pct_ch, img_ok, code_ok, lang_ok))
    p("  " + "-" * 76)
    p()
    p("=" * 80)
    p("END OF REPORT")
    p("=" * 80)

    report = "\n".join(out)
    print(report)


if __name__ == "__main__":
    main()
