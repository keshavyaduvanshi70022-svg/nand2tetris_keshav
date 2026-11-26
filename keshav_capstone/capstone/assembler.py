#!/usr/bin/env python3
"""A small two-pass assembler for the Hack computer (Nand2Tetris).
Student: Keshav | Roll: 25017304322 | K = 22
K-specific feature: report invalid instructions with their source line number.
"""
from pathlib import Path
import argparse
import re
import sys

DEST = {None: "000", "M": "001", "D": "010", "MD": "011", "A": "100", "AM": "101", "AD": "110", "AMD": "111"}
JUMP = {None: "000", "JGT": "001", "JEQ": "010", "JGE": "011", "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"}
COMP = {
    "0":"0101010", "1":"0111111", "-1":"0111010", "D":"0001100", "A":"0110000", "M":"1110000",
    "!D":"0001101", "!A":"0110001", "!M":"1110001", "-D":"0001111", "-A":"0110011", "-M":"1110011",
    "D+1":"0011111", "A+1":"0110111", "M+1":"1110111", "D-1":"0001110", "A-1":"0110010", "M-1":"1110010",
    "D+A":"0000010", "D+M":"1000010", "D-A":"0010011", "D-M":"1010011", "A-D":"0000111", "M-D":"1000111",
    "D&A":"0000000", "D&M":"1000000", "D|A":"0010101", "D|M":"1010101"
}
PREDEFINED = {"SP":0,"LCL":1,"ARG":2,"THIS":3,"THAT":4,"SCREEN":16384,"KBD":24576}
PREDEFINED.update({f"R{i}": i for i in range(16)})
SYMBOL_RE = re.compile(r"^[A-Za-z_.$:][A-Za-z0-9_.$:]*$")

class AssemblyError(Exception):
    pass

def clean_source(path):
    rows = []
    for line_no, raw in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        line = raw.split("//", 1)[0].strip()
        if line:
            rows.append((line_no, re.sub(r"\s+", "", line)))
    return rows

def assemble(source_path, output_path):
    rows = clean_source(source_path)
    symbols = dict(PREDEFINED)
    rom = 0
    # Pass 1: labels.
    for line_no, line in rows:
        if line.startswith("("):
            if not line.endswith(")") or len(line) < 3:
                raise AssemblyError(f"Line {line_no}: invalid label declaration")
            label = line[1:-1]
            if not SYMBOL_RE.match(label):
                raise AssemblyError(f"Line {line_no}: invalid label name '{label}'")
            if label in symbols:
                raise AssemblyError(f"Line {line_no}: duplicate or reserved label '{label}'")
            symbols[label] = rom
        else:
            rom += 1
    # Pass 2: instructions.
    output = []
    next_variable = 16
    for line_no, line in rows:
        if line.startswith("("):
            continue
        try:
            if line.startswith("@"):  # A-instruction
                value = line[1:]
                if not value:
                    raise ValueError("missing A-instruction value")
                if value.isdigit():
                    address = int(value)
                else:
                    if not SYMBOL_RE.match(value):
                        raise ValueError(f"invalid symbol '{value}'")
                    if value not in symbols:
                        symbols[value] = next_variable
                        next_variable += 1
                    address = symbols[value]
                if not 0 <= address <= 32767:
                    raise ValueError("A-instruction value must be between 0 and 32767")
                output.append(f"{address:016b}")
            else:  # C-instruction: dest=comp;jump
                if line.count("=") > 1 or line.count(";") > 1:
                    raise ValueError("malformed C-instruction")
                if "=" in line:
                    dest, rest = line.split("=", 1)
                    if dest not in DEST or not dest:
                        raise ValueError(f"invalid destination '{dest}'")
                else:
                    dest, rest = None, line
                if ";" in rest:
                    comp, jump = rest.split(";", 1)
                    if jump not in JUMP or not jump:
                        raise ValueError(f"invalid jump '{jump}'")
                else:
                    comp, jump = rest, None
                if comp not in COMP:
                    raise ValueError(f"invalid computation '{comp}'")
                output.append("111" + COMP[comp] + DEST[dest] + JUMP[jump])
        except ValueError as exc:
            raise AssemblyError(f"Line {line_no}: invalid instruction ({exc})") from exc
    Path(output_path).write_text("\n".join(output) + "\n", encoding="utf-8")
    return len(output), symbols

def main():
    parser = argparse.ArgumentParser(description="Assemble Hack .asm source into .hack machine code")
    parser.add_argument("source", help="input .asm file")
    parser.add_argument("-o", "--output", help="output .hack file (default: same name)")
    args = parser.parse_args()
    source = Path(args.source)
    output = Path(args.output) if args.output else source.with_suffix(".hack")
    try:
        count, _ = assemble(source, output)
    except (OSError, AssemblyError) as exc:
        print(exc, file=sys.stderr)
        return 1
    print(f"Assembled {count} instructions: {output}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
