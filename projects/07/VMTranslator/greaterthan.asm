	@256
	D=A
	@SP					// setup - remove before adding to VMTranslator
	M=D				// setup - remove before adding to VMTranslator
	@255
	M=1
	@254
	M=0

	@SP 		// SP--
	M=M-1
	A=M 		// D=*SP
	D=M
	@SP 		// SP--
	M=M-1
	A=M
	@GREATER	// Jump to greater if top item in stack is greater than the one below it
	D-M;JGT
	M=0			// Not greater therefore set stack entry at SP to 0 and then jump to end infinite loop
	@SP 		// Increment SP
	M=M+1
	@INFLOOP
	0;JMP
(GREATER)
	M=1			// We jumped here because top item was greate than item below it so set top Stack entry to 1
	@SP 		// Increment SP
	M=M+1
(INFLOOP)
	@INFLOOP
	0;JMP

