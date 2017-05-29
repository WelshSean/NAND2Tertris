// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// fill - will be 0 if we arent writing anything or -1 if we want to write 16 bits of 1
	@8192
	D=A
	@num
	M=D 		// n=8191 - number of 16-bit words to blank the screen

// spoint - screen pointer - used to iterate over the memory locations that represent the screen
// 							 Screen is 512 x 256, each row is 32 consecutive 16-bit words
//							 ie we will need to write 256 x 32 16-bit words
//							  we initialise to the base address




(MAININFINITE)
	@KBD					// Check if a key is pressed and jump out of maininifite if true
	D=M
	@KEYPRESSED
	D;JNE 

// Note that if we didnt JUMP them we get here which means that no key is pressed - blank the screen and carry on looping inifitely
	@SCREEN
	D=A
	@spoint
	M=D

// First of alll blank the screen just in case we'd filled it!

	@0		//initialise counter variable
	D=A
	@n
	M=D

(BLANKLOOP)
	@spoint	
	A=M 			// Load pointer into address register
	M=0				// Write 0 (16 blanks) into the relevant place in the Screen memory map
	@spoint
	M=M+1			// increment the pointer address

	@n  			// increment the counter
	M=M+1

	@num
	D=M
	@n
	D=D-M			// Carry on looping if current index - number of 16-bit words needed > 0
	@BLANKLOOP
	D;JGT
	@MAININFINITE			
	0;JMP


(KEYPRESSED)
	@SCREEN // Initialise screen pointer
	D=A
	@spoint
	M=D

	@0		//initialise counter variable
	D=A
	@n
	M=D

(FILLLOOP)
	@spoint	
	A=M 			// Load pointer into address register
	M=-1			// Write -1 (16 pixels) into the relevant place in the Screen memory map
	@spoint
	M=M+1			// increment the pointer address

	@n  			// increment the counter
	M=M+1

	@num
	D=M
	@n
	D=D-M			// Carry on looping if current index - number of 16-bit words needed > 0
	@FILLLOOP
	D;JGT




	@MAININFINITE
	0;JMP