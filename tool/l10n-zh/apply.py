#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply en->zh rules to Cullimingo Dart sources (tokenizer-level, exact)."""
import os, re, sys, json
sys.path.insert(0, '/tmp')
sys.path.insert(0, '/tmp/cullimingo-l10n')
from cullimengo_scan import scan, concat_groups
from rules import GLOBAL, P, SPANS

ROOT = "/Users/caifeifan/NewLife/VibeMCN/20261003摄影图片初筛/vendor/Cullimingo"
DIRS = ["lib/features", "lib/shared"]

def norm(s):
    return re.sub(r'\s+', ' ', s).strip()

def dart_quote(text):
    """Emit a Dart single-line string literal for text (escaping newlines)."""
    t = text.replace('\\', '\\\\').replace('\n', '\\n').replace('\t', '\\t')
    if "'" not in t:
        return "'" + t + "'"
    if '"' not in t:
        return '"' + t + '"'
    raise ValueError(f"cannot quote: {text!r}")

def main():
    # load files
    files = {}
    for d in DIRS:
        for dirpath, _, fns in os.walk(os.path.join(ROOT, d)):
            for fn in sorted(fns):
                if fn.endswith('.dart') and not fn.endswith('.g.dart'):
                    p = os.path.join(dirpath, fn)
                    files[os.path.relpath(p, ROOT)] = open(p, encoding='utf-8').read()

    report = {'literal_hits': {}, 'span_hits': [], 'missed_rules': [], 'errors': []}
    changed = {}

    for rel, text in files.items():
        recs = scan(rel, text)
        per = P.get(rel, {})
        replacements = []  # (start, end, newtext, desc)
        covered = set()    # ids of literals handled (incl. inside spans)

        # 1. spans
        groups = concat_groups(recs, text)
        for (sf, old_combined, new_text) in SPANS:
            if sf != rel:
                continue
            hits = [g for g in groups if norm(''.join(r['content'] for r in g)) == norm(old_combined)]
            if len(hits) != 1:
                report['errors'].append(f"SPAN {rel}: matched {len(hits)} groups for {old_combined[:60]!r}")
                continue
            g = hits[0]
            span = (g[0]['span_start'], g[-1]['span_end'])
            replacements.append((span[0], span[1], dart_quote(new_text), f"SPAN:{old_combined[:50]}"))
            for r in g:
                covered.add(id(r))
            report['span_hits'].append((rel, old_combined))

        # 2. literal rules
        for r in recs:
            if id(r) in covered:
                continue
            c = r['content']
            new = per.get(c, GLOBAL.get(c))
            if new is None:
                continue
            if r['raw']:
                report['errors'].append(f"RAW literal matched in {rel}:{r['line']}: {c!r}")
                continue
            q = r['quote']
            # quotes inside ${...} interpolation don't conflict with the literal's own quote
            outside = re.sub(r'\$\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', '', new)
            if q in outside:
                report['errors'].append(f"quote conflict {rel}:{r['line']}: {new!r}")
                continue
            replacements.append((r['content_start'], r['content_end'], new, f"LIT:{c[:50]}"))
            key = (rel, c)
            report['literal_hits'][key] = report['literal_hits'].get(key, 0) + 1

        if not replacements:
            continue
        # check overlaps
        replacements.sort()
        for a, b in zip(replacements, replacements[1:]):
            if b[0] < a[1]:
                report['errors'].append(f"OVERLAP in {rel}: {a[3]} vs {b[3]}")
        if any(b[0] < a[1] for a, b in zip(replacements, replacements[1:])):
            continue
        out = []
        pos = 0
        for start, end, newtext, _ in replacements:
            out.append(text[pos:start]); out.append(newtext); pos = end
        out.append(text[pos:])
        new = ''.join(out)
        if new != text:
            changed[rel] = new

    # missed rules
    hit_keys = set(report['literal_hits'].keys())
    for rel, m in P.items():
        for old in m:
            if (rel, old) not in hit_keys:
                report['missed_rules'].append(f"PER_FILE {rel}: {old!r}")
    for old in GLOBAL:
        if not any(k[1] == old for k in hit_keys):
            report['missed_rules'].append(f"GLOBAL: {old!r}")
    span_hit_set = {(r, norm(o)) for r, o in report['span_hits']}
    for (sf, old, _n) in SPANS:
        if (sf, norm(old)) not in span_hit_set:
            report['missed_rules'].append(f"SPAN {sf}: {old[:60]!r}")

    if report['errors']:
        print("ERRORS:")
        for e in report['errors']:
            print(" ", e)
        sys.exit(1)

    for rel, new in changed.items():
        open(os.path.join(ROOT, rel), 'w', encoding='utf-8').write(new)

    n_lit = sum(report['literal_hits'].values())
    print(f"files changed: {len(changed)}")
    print(f"literal replacements: {n_lit} (unique rules hit: {len(report['literal_hits'])})")
    print(f"span replacements: {len(report['span_hits'])}")
    if report['missed_rules']:
        print("MISSED RULES:")
        for m in report['missed_rules']:
            print(" ", m)
    json.dump({'changed': sorted(changed), 'literal_hits': {f"{k[0]}|{k[1]}": v for k, v in report['literal_hits'].items()},
               'spans': report['span_hits']}, open('/tmp/cullimingo-l10n/apply_report.json', 'w'), ensure_ascii=False, indent=1)

if __name__ == '__main__':
    main()
