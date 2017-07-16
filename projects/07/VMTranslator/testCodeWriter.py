import unittest
from VMTranslator import CodeWriter


class MyTestCaseCodeWriter(unittest.TestCase):
    def setUp(self):
        self.testCodeWriter = CodeWriter('/tmp/testfile.asm')
        self.reader = open('/tmp/testfile.asm', 'r')


    def tearDown(self):
        self.testCodeWriter.close()
        self.reader.close()


    def test_writePushConstant(self):
        answer = ['@7\t\t//D=7', 'D=A', '@SP\t\t//*SP=D', 'A=M', 'M=D', '@SP\t\t//SP++', 'M=M+1']
        self.testCodeWriter.writePushPop('C_PUSH', 'constant', '7')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter +=1

    def test_writePushlocal(self):
        answer = ['@7\t// Store address relative to @LCL (offset)', 'D=A', '@i', 'M=D',
                    '@LCL\t// Store @LCL + i', 'D=M', '@TEMPADDR',  'M=D',  '@i',
                    'D=M', '@TEMPADDR' , 'M=M+D',  '@TEMPADDR\t// Store local[i] in D',
                    'A=M', 'D=M' , '@SP\t// set the topmost value in the stack to D',  'A=M', 'M=D', '@SP', 'M=M+1']
        self.testCodeWriter.writePushPop('C_PUSH', 'local', '7')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter +=1

    def test_writePoPlocal(self):
        answer = ['@7\t// Store address relative to @LCL (offset)', 'D=A', '@i', 'M=D',
                    '@LCL\t// Store @LCL + i', 'D=M', '@TEMPADDR',  'M=D',  '@i',
                    'D=M', '@TEMPADDR' , 'M=M+D' , '@SP\t//    SP--', 'M=M-1', '@SP\t// Store top stack value in D',
                    'A=M', 'D=M' , '@TEMPADDR\t// set MEM[TEMPADDR] (LCL+i) to D',  'A=M', 'M=D']
        self.testCodeWriter.writePushPop('C_POP', 'local', '7')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter +=1

    def test_writePushArgument(self):
        answer = ['@7\t// Store address relative to @ARG (offset)', 'D=A', '@i', 'M=D',
                    '@ARG\t// Store @ARG + i', 'D=M', '@TEMPADDR',  'M=D',  '@i',
                    'D=M', '@TEMPADDR' , 'M=M+D' ,   '@TEMPADDR\t// Store local[i] in D',
                    'A=M', 'D=M' , '@SP\t// set the topmost value in the stack to D',  'A=M', 'M=D', '@SP', 'M=M+1']
        self.testCodeWriter.writePushPop('C_PUSH', 'argument', '7')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter +=1

    def test_writePoPArgument(self):
        answer = ['@7\t// Store address relative to @ARG (offset)', 'D=A', '@i', 'M=D',
                    '@ARG\t// Store @ARG + i', 'D=M', '@TEMPADDR',  'M=D',  '@i',
                    'D=M', '@TEMPADDR' , 'M=M+D' , '@SP\t//    SP--', 'M=M-1', '@SP\t// Store top stack value in D',
                    'A=M', 'D=M' , '@TEMPADDR\t// set MEM[TEMPADDR] (LCL+i) to D',  'A=M', 'M=D']
        self.testCodeWriter.writePushPop('C_POP', 'argument', '7')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter +=1

    def test_writePushThis(self):
        answer = ['@7\t// Store address relative to @THIS (offset)', 'D=A', '@i', 'M=D',
                    '@THIS\t// Store @THIS + i', 'D=M', '@TEMPADDR',  'M=D',  '@i',
                    'D=M', '@TEMPADDR' , 'M=M+D' ,   '@TEMPADDR\t// Store local[i] in D',
                    'A=M', 'D=M' , '@SP\t// set the topmost value in the stack to D',  'A=M', 'M=D', '@SP', 'M=M+1']
        self.testCodeWriter.writePushPop('C_PUSH', 'this', '7')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter +=1

    def test_writePoPThis(self):
        answer = ['@7\t// Store address relative to @THIS (offset)', 'D=A', '@i', 'M=D',
                    '@THIS\t// Store @THIS + i', 'D=M', '@TEMPADDR',  'M=D',  '@i',
                    'D=M', '@TEMPADDR' , 'M=M+D' , '@SP\t//    SP--', 'M=M-1', '@SP\t// Store top stack value in D',
                    'A=M', 'D=M' , '@TEMPADDR\t// set MEM[TEMPADDR] (LCL+i) to D',  'A=M', 'M=D']
        self.testCodeWriter.writePushPop('C_POP', 'this', '7')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter +=1

    def test_writePushThat(self):
        answer = ['@7\t// Store address relative to @THAT (offset)', 'D=A', '@i', 'M=D',
                    '@THAT\t// Store @THAT + i', 'D=M', '@TEMPADDR',  'M=D',  '@i',
                    'D=M', '@TEMPADDR' , 'M=M+D' ,  '@TEMPADDR\t// Store local[i] in D',
                    'A=M', 'D=M' , '@SP\t// set the topmost value in the stack to D',  'A=M', 'M=D', '@SP', 'M=M+1']
        self.testCodeWriter.writePushPop('C_PUSH', 'that', '7')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter +=1
            
    def test_writePushStatic(self):
        answer = ['@testfile.7\t// Read in funcname.index and put on top of stack', 'D=M', '@SP', 'A=M', 'M=D',
                    '@SP\t// increment Stack pointer', 'M=M+1']
        self.testCodeWriter.writePushPop('C_PUSH', 'static', '7')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter +=1

    def test_writePoPStatic(self):
        answer = ['@SP\t// take from top of stack and save to filename.index', 'M=M-1', 'A=M', 'D=M',
                    '@testfile.7', 'M=D']
        self.testCodeWriter.writePushPop('C_POP', 'static', '7')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter +=1

    def test_writePoPThat(self):
        answer = ['@7\t// Store address relative to @THAT (offset)', 'D=A', '@i', 'M=D',
                    '@THAT\t// Store @THAT + i', 'D=M', '@TEMPADDR',  'M=D',  '@i',
                    'D=M', '@TEMPADDR' , 'M=M+D' , '@SP\t//    SP--', 'M=M-1', '@SP\t// Store top stack value in D',
                    'A=M', 'D=M' , '@TEMPADDR\t// set MEM[TEMPADDR] (LCL+i) to D',  'A=M', 'M=D']
        self.testCodeWriter.writePushPop('C_POP', 'that', '7')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter +=1


    def test_writePushTemp(self):
        answer = ['@7\t// Store address relative to 5', 'D=A', '@i', 'M=D', '@5', 'D=A', '@TEMPADDR',
                     'M=D', '@i\t// Store local[i] in D', 'D=M+D', 'A=D' , 'D=M',
                  '@SP\t// set the topmost value in the stack to D',  'A=M', 'M=D', '@SP', 'M=M+1']
        self.testCodeWriter.writePushPop('C_PUSH', 'temp', '7')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter +=1



    def test_writeArithmeticAdd(self):
        answer = ['@SP\t\t//SP--', 'M=M-1', 'A=M\t\t//D=*SP', 'D=M', '@SP\t\t//SP--', 'M=M-1', 'A=M\t\t//*SP=D+*SP',
                  'M=D+M', '@SP\t\t//SP++', 'M=M+1' ]
        self.testCodeWriter.writeArithmetic('add')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
            self.assertNotEqual(len(lines), 0)
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter += 1


    def test_writeArithmeticSub(self):
        answer = ['@SP\t\t//SP--', 'M=M-1', 'A=M\t\t//D=*SP', 'D=M', '@SP\t\t//SP--', 'M=M-1', 'A=M\t\t//*SP=D+*SP',
                    'M=M-D', '@SP\t\t//SP++', 'M=M+1']
        self.testCodeWriter.writeArithmetic('sub')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
            self.assertNotEqual(len(lines), 0)
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter += 1

    def test_writeArithmeticOr(self):
        answer = ['@SP\t\t//SP--', 'M=M-1', 'A=M\t\t//D=*SP', 'D=M', '@SP\t\t//SP--', 'M=M-1', 'A=M\t\t//*SP=D+*SP',
                    'M=D|M', '@SP\t\t//SP++', 'M=M+1']
        self.testCodeWriter.writeArithmetic('or')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
            self.assertNotEqual(len(lines), 0)
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter += 1

    def test_writeArithmeticAnd(self):
        answer = ['@SP\t\t//SP--', 'M=M-1', 'A=M\t\t//D=*SP', 'D=M', '@SP\t\t//SP--', 'M=M-1', 'A=M\t\t//*SP=D+*SP',
                    'M=D&M', '@SP\t\t//SP++', 'M=M+1']
        self.testCodeWriter.writeArithmetic('and')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
            self.assertNotEqual(len(lines), 0)
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter += 1

    def test_writeArithmeticNeg(self):
        answer = ['@SP\t\t//SP--', 'M=M-1', 'A=M\t\t//*SP=-*SP', 'M=-M', '@SP\t\t//SP++', 'M=M+1']
        self.testCodeWriter.writeArithmetic('neg')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
            self.assertNotEqual(len(lines), 0)
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter += 1

    def test_writeArithmeticNot(self):
        answer = ['@SP\t\t//SP--', 'M=M-1', 'A=M\t\t//*SP=-*SP', 'M=!M', '@SP\t\t//SP++', 'M=M+1']
        self.testCodeWriter.writeArithmetic('not')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
            self.assertNotEqual(len(lines), 0)
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter += 1

    def test_writeArithmeticGT(self):
        answer = ['@SP\t\t//SP--', 'M=M-1', 'A=M\t\t//D=*SP', 'D=M', '@SP\t\t//SP--', 'M=M-1', 'A=M', 'D=M-D',
                  '@GREATER.1\t// Jump to greater if top item in stack is greater than the one below it', 'D;JGT',
                  '@SP', 'A=M',
                  'M=0\t// Not greater therefore set stack entry at SP to 0 and then jump to end infinite loop',
                  '@SP\t// Increment SP', 'M=M+1', '@END.2', '0;JMP', '(GREATER.1)', '@SP', 'A=M',
                  'M=-1\t// We jumped here because top item was greate than item below it so set top Stack entry to -1',
                  '@SP\t// Increment SP', 'M=M+1', '(END.2)']
        self.testCodeWriter.writeArithmetic('gt')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
            self.assertNotEqual(len(lines), 0)
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter += 1

    def test_writeArithmeticLT(self):
        answer = ['@SP\t\t//SP--', 'M=M-1', 'A=M\t\t//D=*SP', 'D=M', '@SP\t\t//SP--', 'M=M-1', 'A=M', 'D=D-M',
                  '@LESS.1\t// Jump to less if top item in stack is greater than the one below it', 'D;JGT','@SP', 'A=M',
                  'M=0\t// Not greater therefore set stack entry at SP to 1 and then jump to end infinite loop',
                  '@SP\t// Increment SP', 'M=M+1', '@END.2', '0;JMP', '(LESS.1)', '@SP', 'A=M',
                  'M=-1\t// We jumped here because top item was greater than item below it so set top Stack entry to -1',
                  '@SP\t// Increment SP', 'M=M+1', '(END.2)']
        self.testCodeWriter.writeArithmetic('lt')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
            self.assertNotEqual(len(lines), 0)
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter += 1

    def test_writeArithmeticEQ(self):
        answer = ['@SP\t\t//SP--', 'M=M-1', 'A=M\t\t//D=*SP', 'D=M', '@SP\t\t//SP--', 'M=M-1', 'A=M', 'D=D-M',
                  '@NOTEQUAL.2\t// Jump to notequal if top item in stack is not equal to the one below it', 'D;JNE',
                  '@SP', 'A=M',
                  'M=-1\t// Equal therefore set stack entry at SP to 1 and then jump to end infinite loop',
                  '@SP\t// Increment SP', 'M=M+1', '@END.1', '0;JMP', '(NOTEQUAL.2)','@SP', 'A=M',
                  'M=0\t// We jumped here because top item was not equal to the item below it so set top Stack entry to 0',
                  '@SP\t// Increment SP', 'M=M+1', '(END.1)']
        self.testCodeWriter.writeArithmetic('eq')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
            self.assertNotEqual(len(lines), 0)
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter += 1

    def test_writeLabel(self):
        answer = ['(testfile$testlabel.1)']

        self.testCodeWriter.writeLabel('testlabel')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
            self.assertNotEqual(len(lines), 0)
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter += 1

    def test_writeIf(self):
        answer = ['@SP', 'M=M-1', 'A=M', 'D=M', '@testfile$testlabel.1', 'D;JNE'  ]

        self.testCodeWriter.writeIf('testlabel')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
            self.assertNotEqual(len(lines), 0)
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter += 1

    def test_Goto(self):
        answer = ['@testfile$testlabel.1', '0;JMP'  ]

        self.testCodeWriter.writeGoto('testlabel')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
            self.assertNotEqual(len(lines), 0)
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter += 1

    def test_writeFunctionTwo(self):
        answer = ['(testfunc)\t// Start new Function', '@SP', 'A=M', 'M=0', '@SP', 'M=M+1', '@SP', 'A=M', 'M=0', '@SP', 'M=M+1'    ]

        self.testCodeWriter.writeFunction('testfunc',2)
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
            self.assertNotEqual(len(lines), 0)
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter += 1

    def test_writeFunctionZero(self):
        answer = ['(testfunc)\t// Start new Function']

        self.testCodeWriter.writeFunction('testfunc', 0)
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile.asm', mode='r') as f:
            lines = f.read().splitlines()
            self.assertNotEqual(len(lines), 0)
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter += 1

    def test_getNewUUIDAnonymous(self):
        UUID = self.testCodeWriter.getNewUUID()
        self.assertEqual(UUID, '.1')
        UUID = self.testCodeWriter.getNewUUID()
        self.assertEqual(UUID,'.2')

    def test_getNewUUIDNamed(self):
        UUID = self.testCodeWriter.getNewUUID('testuuid1')
        self.assertEqual(UUID, '.1')
        UUID = self.testCodeWriter.getNewUUID('testuuid2')
        self.assertEqual(UUID,'.2')
        UUID = self.testCodeWriter.getNewUUID('testuuid1')
        self.assertEqual(UUID, '.1')







if __name__ == '__main__':
    unittest.main()
