# Capstone Project Report — Make the Computer Draw a Box

**Student Name:** Keshav  
**Roll Number:** 25017304322  
**Course:** Nand to Tetris – I (ETCCNT301)  
**Personal K:** 22

## 1. Objective
The objective is to build the Hack computer components, write a Python assembler, and create a Hack assembly program that displays a black rectangle while a key is pressed.

## 2. Personalized box dimensions
- Starting row: 22
- Height: 20 rows
- Width: 48 pixels (3 words × 16 pixels)
- Starting screen address: 17088
- K mod 3: 1, so the assembler must print a clear error message with the source line number.

## 3. Part A — Computer construction and testing
Describe how CPU.hdl, Memory.hdl, and Computer.hdl connect. Insert your actual screenshots for the five official tests:

- [Insert CPU.tst screenshot]
- [Insert Memory.tst screenshot]
- [Insert ComputerAdd.tst screenshot]
- [Insert ComputerMax.tst screenshot]
- [Insert ComputerRect.tst screenshot]

## 4. Part B — Python assembler
Explain the two passes: first pass records labels and ROM addresses; second pass translates A- and C-instructions into 16-bit machine instructions and allocates variables from RAM address 16. Explain the K=22 feature: invalid instructions produce a message containing the original line number.

## 5. Part C — Box program
Explain that each screen row contains 32 words and each word represents 16 horizontal pixels. The program checks the keyboard, fills three consecutive screen words for each of 20 rows while a key is pressed, and clears the same area when no key is pressed.

[Insert your actual CPU Emulator screenshot showing the box.]

## 6. One mistake fixed
Write one real mistake you encountered, how you identified it, and what change fixed it. Do not invent a mistake; describe your own debugging experience.

## 7. Conclusion
Summarize what you learned about Hack hardware, machine code, assembly, memory mapping, and keyboard-controlled screen output.
