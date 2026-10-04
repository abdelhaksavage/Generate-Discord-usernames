"""SavageXx Users - clean offline forge. Purpose: readable kremlin-class names. Inputs: count. Outputs: console table + SavageXx.txt."""
import os, random

OUTPUT_FILE = "SavageXx.txt"

os.system("")  # enables VT on Win10+, no-op elsewhere
USE_COLOR = True  # set False for zero codes

def c(code, s):
    return f"\033[{code}m{s}\033[0m" if USE_COLOR else s

G = lambda s: c("92", s)
CY = lambda s: c("96", s)
Y = lambda s: c("93", s)

BANNER = r"""
 _  __               _    _
| |/ /_ __ ___ _ __ | | Habana
| ' /| '__/ _ \ '_ \| | (_)\
| . \| | |  __/ | | | |___ _ 
|_|\_\_|  \___|_| |_|_____(_)
""".replace("Habana", "mlin").replace("(_)", "(_)")


LETTERS = "abcdefghijklmnopqrstuvwxyz"
RARE = "qwxzjk"
DIGITS = "0123456789"

def make_base():
    return random.choice(RARE) + random.choice(DIGITS) + random.choice(DIGITS + LETTERS) + random.choice(LETTERS)

def make_variant(base):
    return random.choice([base + ".", base + "_", base[:2] + "_" + base[2:], base[:2] + "." + base[2:]])

def forge(n=32):
    out = set()
    while len(out) < n:
        out.add(make_variant(make_base()))
    return sorted(out)

def show(names):
    print(CY(BANNER))
    print(Y("== Kremlin Users | kremlin-class | HeMa =="))
    print("-" * 44)
    for i, name in enumerate(names, 1):
        print(f"{i:02d}. {G(name):<16}", end="\n" if i % 4 == 0 else "")
    print("\n" + "-" * 44)
    print(CY(f"saved {len(names)} to {OUTPUT_FILE}"))

if __name__ == "__main__":
    names = forge(32)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(names))
    show(names)