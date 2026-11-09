
#!/usr/bin/env python3
"""Resolve duplicate Pandoc Texinfo nodes and menu references."""

from collections import Counter
from pathlib import Path
import re
import sys

path = Path(sys.argv[1])
text = path.read_text(encoding="utf-8")
lines = text.splitlines(keepends=True)

node_re = re.compile(r"^@node (.+?)\s*$")
menu_re = re.compile(r"^(\* )(.+?)::\s*$")

# Record original node names and positions.
nodes = [
    (i, match.group(1))
    for i, line in enumerate(lines)
    if (match := node_re.match(line))
]

counts = Counter()
renamed = {}

for pos, name in nodes:
    counts[name] += 1
    number = counts[name]
    renamed[pos] = name if number == 1 else f"{name} ({number})"

# Check that all resulting names are unique.
if len(set(renamed.values())) != len(renamed):
    raise ValueError("Node names are still not unique")

# Resolve menu entries to following nodes.
in_menu = False
previous_target = -1
changes = {}

for i, line in enumerate(lines):
    stripped = line.strip()

    if stripped == "@menu":
        in_menu = True
        previous_target = i
        continue

    if stripped == "@end menu":
        in_menu = False
        continue

    if not in_menu:
        continue

    match = menu_re.match(line)
    if not match:
        continue

    name = match.group(2)

    candidates = [
        pos for pos, original in nodes
        if original == name and pos > previous_target
    ]

    if not candidates:
        raise ValueError(f"Unresolved menu entry: {name}")

    target = candidates[0]
    previous_target = target

    if renamed[target] != name:
        changes[i] = f"* {name}: {renamed[target]}.\n"

# Apply changes after resolution.
for pos, new_name in renamed.items():
    lines[pos] = f"@node {new_name}\n"

for pos, replacement in changes.items():
    lines[pos] = replacement

path.write_text("".join(lines), encoding="utf-8")

print(f"Processed {len(nodes)} nodes")
print(f"Renamed {sum(a != b for (_, a), b in zip(nodes, renamed.values()))} duplicates")
print(f"Updated {len(changes)} menu entries")
