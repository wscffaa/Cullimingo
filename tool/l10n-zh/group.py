#!/usr/bin/env python3
import json, collections
cands = json.load(open('/tmp/cullimingo-l10n/candidates.json'))
groups = collections.OrderedDict()
for c in cands:
    groups.setdefault(c['full'], []).append(c)
print(f"unique strings: {len(groups)}")
out = []
for s, recs in sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0].lower())):
    locs = sorted({f"{r['file']}:{r['line']}" for r in recs})
    ctxs = {r['context'][:110] for r in recs}
    out.append({"s": s, "n": len(recs), "locs": locs, "ctx": sorted(ctxs)[:4]})
with open('/tmp/cullimingo-l10n/unique.json', 'w', encoding='utf-8') as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1)
