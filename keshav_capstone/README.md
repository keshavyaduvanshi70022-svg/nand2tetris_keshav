# Nand to Tetris I Capstone — Keshav

**Name:** Keshav  
**Roll number:** 25017304322  
**Personal K:** 22  
**Project:** Make the Computer Draw a Box

This starter submission follows the supplied two-page capstone brief. The personalized rectangle is 48 pixels wide (3 Hack screen words), 20 rows tall, beginning at screen row 22. The assembler's K-dependent feature is line-numbered error reporting because 22 mod 3 = 1.

## Folder structure

- `capstone/assembler.py` — two-pass Hack assembler, with predefined symbols and line-numbered diagnostics.
- `capstone/programs/Box.asm` — key-controlled rectangle program.
- `capstone/hdl/CPU.hdl`, `Memory.hdl`, `Computer.hdl` — HDL integration files.
- `report/REPORT_TEMPLATE.md` — report outline to complete with your own screenshots and observations.

## Run the assembler

From the repository root:

```bash
python capstone/assembler.py capstone/programs/Box.asm
```

This creates `capstone/programs/Box.hack`.

To choose an output path:

```bash
python capstone/assembler.py capstone/programs/Box.asm -o capstone/programs/Box.hack
```

## Run in Nand2Tetris tools

1. Open the HDL files in the Hardware Simulator. The HDL directory needs the standard Nand2Tetris built-in chips and your completed prerequisite chips from the course.
2. Run the official supplied tests for CPU, Memory, and Computer (`CPU.tst`, `Memory.tst`, `ComputerAdd.tst`, `ComputerMax.tst`, `ComputerRect.tst`). The official test scripts and `.cmp` files were not included in the assignment PDF, so add them from your course materials.
3. Assemble `Box.asm` with the Python assembler above.
4. Open the Hack CPU Emulator, load `Box.hack`, and run. Hold any key to draw; release to clear.
5. Capture genuine screenshots of the test outputs and rectangle for your report.

## Important verification note

The assignment asks you to join the lab chips into CPU/Memory/Computer. The supplied PDF does not include your previous lab chip files or the official test scripts. Therefore this ZIP includes the integration HDL source, but you must validate it against the exact simulator version and your course's official tests. Do not claim tests passed until you have run and captured them. If your lab already has working `ARegister`, `DRegister`, `ALU`, `PC`, `RAM16K`, `Screen`, and `Keyboard` chips, keep those working versions in the simulator's project directory.

## K-specific calculation

- `22 mod 3 = 1`: assembler reports an invalid instruction with its original source line number.
- `22 mod 4 = 2`: width = `16 × (2 + 1) = 48` pixels.
- Starting screen address = `SCREEN + 32 × 22 = 16384 + 704 = 17088`.
