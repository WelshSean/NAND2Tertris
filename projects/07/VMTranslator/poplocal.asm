	@258
	D=A
	@SP
	M=D	

	@512
	D=A
	@LCL
	M=D

	@5
	D=A
	@257
	M=D


	@12
	D=A
	@256
	M=D

	// pop local 2
	//
	// Algo is
	// SP--
	// addr = LCL +i
	// *addr = *SP
	//
	// setup - remove before adding to VMTransla / setup - remove before adding to VMTranslator
	@2 			// Store address relative to LCL (offset)
	D=A
	@i
	M=D

	@LCL			// Store LCL + i (2 in this case)
	D=M
	@TEMPADDR
	M=D
	@i
	D=M
	@TEMPADDR
	M=M+D

	@SP   			//    SP--
	M=M-1

	@SP            // Store top stack value in D
	A=M
	D=M

	@TEMPADDR      // set MEM[TEMPADDR] (LCL+i) to D
	A=M
	M=D

