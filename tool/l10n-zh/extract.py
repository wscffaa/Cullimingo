#!/usr/bin/env python3
"""Extract candidate UI string literals from Dart files under lib/features and lib/shared."""
import os, re, json, sys

ROOT = "/Users/caifeifan/NewLife/VibeMCN/20261003摄影图片初筛/vendor/Cullimingo"
DIRS = ["lib/features", "lib/shared"]

def scan_dart_strings(path, text):
    """Yield dicts: {line, col, end_line, quote, raw, content, context_line}."""
    n = len(text)
    i = 0
    line = 1
    col = 0
    results = []
    # state helpers
    def advance(ch):
        nonlocal line, col
        if ch == '\n':
            line += 1; col = 0
        else:
            col += 1
    lines = text.split('\n')
    while i < n:
        ch = text[i]
        # comments
        if ch == '/' and i + 1 < n and text[i+1] == '/':
            while i < n and text[i] != '\n':
                advance(text[i]); i += 1
            continue
        if ch == '/' and i + 1 < n and text[i+1] == '*':
            advance(text[i]); advance(text[i+1]); i += 2
            depth = 1
            while i < n and depth:
                if text[i] == '/' and i+1 < n and text[i+1] == '*':
                    depth += 1; advance(text[i]); advance(text[i+1]); i += 2
                elif text[i] == '*' and i+1 < n and text[i+1] == '/':
                    depth -= 1; advance(text[i]); advance(text[i+1]); i += 2
                else:
                    advance(text[i]); i += 1
            continue
        # strings
        raw = False
        start = i
        if ch == 'r' and i + 1 < n and text[i+1] in "'\"":
            raw = True
            quote_ch = text[i+1]
            triple = text[i+1:i+4] == quote_ch * 3
            i += 1
        elif ch in "'\"":
            quote_ch = ch
            triple = text[i:i+3] == ch * 3
        else:
            advance(ch); i += 1
            continue
        start_line, start_col = line, col
        # consume opening quote
        q = quote_ch * (3 if triple else 1)
        for _ in q:
            advance(text[i]); i += 1
        buf = []
        closed = False
        while i < n:
            if not raw and text[i] == '\\':
                buf.append(text[i:i+2])
                advance(text[i]); advance(text[i+1]); i += 2
                continue
            if text[i] == quote_ch:
                if triple:
                    if text[i:i+3] == quote_ch * 3:
                        for _ in range(3):
                            advance(text[i]); i += 1
                        closed = True
                        break
                    buf.append(text[i]); advance(text[i]); i += 1
                    continue
                else:
                    advance(text[i]); i += 1
                    closed = True
                    break
            # record interpolation braces for skipping nested strings
            if not raw and text[i] == '$' and i + 1 < n:
                if text[i+1] == '{':
                    buf.append('${')
                    advance(text[i]); advance(text[i+1]); i += 2
                    d = 1
                    while i < n and d:
                        if text[i] == '{':
                            d += 1
                        elif text[i] == '}':
                            d -= 1
                        buf.append(text[i])
                        advance(text[i]); i += 1
                    continue
                else:
                    m = re.match(r'\$[a-zA-Z_][a-zA-Z0-9_]*', text[i:])
                    if m:
                        s = m.group(0)
                        buf.append(s)
                        for c in s:
                            advance(c)
                        i += len(s)
                        continue
            buf.append(text[i])
            advance(text[i]); i += 1
        content = ''.join(buf)
        if closed:
            ctx_line = lines[start_line-1] if start_line-1 < len(lines) else ''
            results.append({
                "file": path, "line": start_line, "col": start_col,
                "quote": q[0], "triple": triple, "raw": raw,
                "content": content, "context": ctx_line.strip(),
            })
    return results

KEY_RE = re.compile(r'^[a-z][a-z0-9_]*$')                    # pure lowercase key
EXT_RE = re.compile(r'^\.?[a-z0-9]{1,5}$', re.I)              # file ext like jpg, .cr3
B64_RE = re.compile(r'^[A-Za-z0-9+/]{40,}={0,2}$')
NUM_RE = re.compile(r'^[\d\s.,:+\-()%/xX*]+$')
PATH_RE = re.compile(r'^[a-z0-9_\-./]+$', re.I)               # path-ish (no spaces, has / or .)
UPPER_IDENT_RE = re.compile(r'^[A-Z][A-Z0-9_]{1,}$')          # CONST_KEY
HEX_RE = re.compile(r'^(0x)?[0-9a-fA-F]+$')

def is_candidate(s):
    if s is None: return False
    t = s.strip()
    if len(t) < 2: return False
    if not re.search(r'[a-zA-Z]', t): return False        # must contain a letter
    if '\n' in t: return False
    if ';' in t: return False
    if t.startswith(('http://', 'https://', 'package:', 'dart:')): return False
    if KEY_RE.match(t): return False                       # 'rating', 'keep'
    if HEX_RE.match(t): return False
    if NUM_RE.match(t): return False
    if B64_RE.match(t): return False
    if EXT_RE.match(t) and ' ' not in t: return False      # 'jpg', '.CR3'
    if UPPER_IDENT_RE.match(t) and '_' in t: return False  # CONST_KEYS
    # path-like without spaces: likely import/asset
    if PATH_RE.match(t) and ('/' in t): return False
    # single token camelCase/identifier: likely code identifier
    if re.match(r'^[a-z][a-zA-Z0-9_]*$', t): return False
    return True

def line_is_log(context):
    return bool(re.search(r'\b(debugPrint|print|log|logger|\.fine|\.info|\.warning|\.severe)\b', context))

def main():
    all_strings = []
    for d in DIRS:
        base = os.path.join(ROOT, d)
        for dirpath, _, files in os.walk(base):
            for f in sorted(files):
                if not f.endswith('.dart'): continue
                if f.endswith('.g.dart'): continue  # generated
                p = os.path.join(dirpath, f)
                rel = os.path.relpath(p, ROOT)
                with open(p, encoding='utf-8') as fh:
                    text = fh.read()
                for rec in scan_dart_strings(rel, text):
                    rec["full"] = rec["content"]
                    all_strings.append(rec)
    # classify
    cands = []
    for rec in all_strings:
        s = rec["content"]
        if not is_candidate(s): continue
        if line_is_log(rec["context"]): continue
        cands.append(rec)
    print(f"total string literals scanned: {len(all_strings)}", file=sys.stderr)
    print(f"candidates after filter: {len(cands)}", file=sys.stderr)
    with open('/tmp/cullimingo-l10n/candidates.json', 'w', encoding='utf-8') as fh:
        json.dump(cands, fh, ensure_ascii=False, indent=1)

if __name__ == '__main__':
    main()
