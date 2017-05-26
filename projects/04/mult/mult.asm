// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// ans = 0
	@ans
	M=0

// fact = R0
	@R0
	D=M
	@fact
	M=D

// n = R1
	@R1
	D=M
	@n
	M=D

// i = 1
	@i
	M=0

// Initialise R2
	@R2
	M=0

(LOOP)
	@i
	D=M
	@n
	D=D-M	// D = i - n
	@ENDLOOP
	D;JGE	// if i-n > 0 goto ENDLOOP

	@i
	M=M+1  // Increment Loop counter

	@fact
	D=M
	@ans
	M=M+D 	// ans = ans + fact

	@LOOP
	0;JMP	// Goto Loop



(ENDLOOP)
 	@ans	// Finished looping - lets set R2=ans
	D=M
	@R2
	M=D
(INF)
	@INF
	0;JMP	//Infinite Loop




