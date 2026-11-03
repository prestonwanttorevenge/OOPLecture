# -*- coding: utf-8 -*-
import sys, re

sys.stdout.reconfigure(encoding='utf-8')

from module_preamble import preamble_text
from module_chap1 import chap1_text
from module_chap2 import chap2_text
from module_chap3 import chap3_text
from module_chap4 import chap4_text
from module_chap5 import chap5_text
from module_chap6 import chap6_text
from module_chap7 import chap7_text
from module_chap8 import chap8_text

full_tex = (
    preamble_text.strip() + "\n\n" +
    chap1_text.strip() + "\n\n" +
    chap2_text.strip() + "\n\n" +
    chap3_text.strip() + "\n\n" +
    chap4_text.strip() + "\n\n" +
    chap5_text.strip() + "\n\n" +
    chap6_text.strip() + "\n\n" +
    chap7_text.strip() + "\n\n" +
    chap8_text.strip() + "\n"
)

# Automated checks
print("--- Automated Quality Verification ---")

# 1. Environment balance
begins = re.findall(r'\\begin\{([a-zA-Z0-9*]+)\}', full_tex)
ends = re.findall(r'\\end\{([a-zA-Z0-9*]+)\}', full_tex)
print(f"Total \\begin: {len(begins)}, Total \\end: {len(ends)}")
if len(begins) != len(ends):
    print("WARNING: Begin and End counts do not match!")
    # Find mismatch
    from collections import Counter
    b_count = Counter(begins)
    e_count = Counter(ends)
    for k in set(b_count.keys()).union(e_count.keys()):
        if b_count[k] != e_count[k]:
            print(f"Mismatch in environment '{k}': begin={b_count[k]}, end={e_count[k]}")

# 2. Check unescaped ampersands outside listings/tabular
in_listing = False
in_table = False
for idx, line in enumerate(full_tex.split('\n'), 1):
    if '\\begin{lstlisting}' in line:
        in_listing = True
    elif '\\end{lstlisting}' in line:
        in_listing = False
        continue
    if '\\begin{tabular}' in line:
        in_table = True
    elif '\\end{tabular}' in line:
        in_table = False
        continue
    if not in_listing and not in_table:
        clean = re.sub(r'(?<!\\)%.*$', '', line)
        matches = list(re.finditer(r'(?<!\\)&', clean))
        if matches:
            print(f"Line {idx} unescaped &: {clean.strip()[:60]}")

# 3. Check unescaped underscores outside texttt/math/listings
in_listing = False
for idx, line in enumerate(full_tex.split('\n'), 1):
    if '\\begin{lstlisting}' in line:
        in_listing = True
    elif '\\end{lstlisting}' in line:
        in_listing = False
        continue
    if not in_listing:
        clean = re.sub(r'(?<!\\)%.*$', '', line)
        clean = re.sub(r'\\texttt\{[^}]*\}', '', clean)
        clean = re.sub(r'\$[^$]*\$', '', clean)
        clean = re.sub(r'\\detokenize\{[^}]*\}', '', clean)
        clean = re.sub(r'\\includegraphics(\[[^\]]*\])?\{[^}]*\}', '', clean)
        # ignore node names in parentheses like (sp_title)
        clean = re.sub(r'\([a-zA-Z0-9_]+\)', '', clean)
        clean = re.sub(r'morekeywords=\{[^}]*\}', '', clean)
        matches = list(re.finditer(r'(?<!\\)_', clean))
        if matches:
            print(f"Line {idx} unescaped _: {clean.strip()[:60]}")

# Write to file
with open('The_OOP_C_Bible.tex', 'w', encoding='utf-8') as f:
    f.write(full_tex)

print(f"Successfully assembled and written The_OOP_C_Bible.tex ({len(full_tex.splitlines())} lines)!")
