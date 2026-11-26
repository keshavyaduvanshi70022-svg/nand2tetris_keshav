// Keshav | Roll No. 25017304322 | K = 22
// Draw a black rectangle while any key is pressed.
// Top row = 22, height = 20 rows, width = 48 pixels (3 screen words).
// Each Hack screen row contains 32 words. SCREEN + 32*22 = 17088.

(LOOP)
    @KBD
    D=M
    @DRAW
    D;JNE

// No key: clear the same 20 x 3-word area.
    @17088
    D=A
    @ADDR
    M=D
    @20
    D=A
    @ROWS
    M=D
(CLEAR_ROW)
    @3
    D=A
    @WORDS
    M=D
(CLEAR_WORD)
    @ADDR
    A=M
    M=0
    @ADDR
    M=M+1
    @WORDS
    MD=M-1
    @CLEAR_WORD
    D;JGT
    @29
    D=A
    @ADDR
    M=D+M
    @ROWS
    MD=M-1
    @CLEAR_ROW
    D;JGT
    @LOOP
    0;JMP

(DRAW)
    @17088
    D=A
    @ADDR
    M=D
    @20
    D=A
    @ROWS
    M=D
(DRAW_ROW)
    @3
    D=A
    @WORDS
    M=D
(DRAW_WORD)
    @ADDR
    A=M
    M=-1
    @ADDR
    M=M+1
    @WORDS
    MD=M-1
    @DRAW_WORD
    D;JGT
    @29
    D=A
    @ADDR
    M=D+M
    @ROWS
    MD=M-1
    @DRAW_ROW
    D;JGT
    @LOOP
    0;JMP
