import unittest
from VMTranslator import CodeWriter


class MyTestCaseCodeWriter(unittest.TestCase):
    def setUp(self):
        self.testCodeWriter = CodeWriter('/tmp/testfile')
        self.reader = open('/tmp/testfile', 'r')


    def tearDown(self):
        self.testCodeWriter.close()
        self.reader.close()


    def test_writePush(self):
        answer = ['@7\t\t//D=7', 'D=A', '@SP\t\t//*SP=D', 'A=M', 'M=D', '@SP\t\t//SP++', 'M=M+1']
        self.testCodeWriter.writePushPop('C_PUSH', 'local', '7')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile', mode='r') as f:
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
        with open('/tmp/testfile', mode='r') as f:
            lines = f.read().splitlines()
            self.assertNotEqual(len(lines), 0)
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter += 1


    def test_writeArithmeticSub(self):
        answer = ['@SP\t\t//SP--', 'M=M-1', 'A=M\t\t//D=*SP', 'D=M', '@SP\t\t//SP--', 'M=M-1', 'A=M\t\t//*SP=D+*SP',
                    'M=D-M', '@SP\t\t//SP++', 'M=M+1']
        self.testCodeWriter.writeArithmetic('sub')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile', mode='r') as f:
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
        with open('/tmp/testfile', mode='r') as f:
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
        with open('/tmp/testfile', mode='r') as f:
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
        with open('/tmp/testfile', mode='r') as f:
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
        with open('/tmp/testfile', mode='r') as f:
            lines = f.read().splitlines()
            self.assertNotEqual(len(lines), 0)
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter += 1

    def test_writeArithmeticGT(self):
        answer = ['@SP\t\t//SP--', 'M=M-1', 'A=M\t\t//D=*SP', 'D=M', '@SP\t\t//SP--', 'M=M-1', 'A=M',
                  '@GREATER\t// Jump to greater if top item in stack is greater than the one below it', 'D-M;JGT',
                  'M=0\t// Not greater therefore set stack entry at SP to 0 and then jump to end infinite loop',
                  '@SP\t// Increment SP', 'M=M+1', '@END', '0;JMP', '(GREATER)',
                  'M=1\t// We jumped here because top item was greate than item below it so set top Stack entry to 1',
                  '@SP\t// Increment SP', 'M=M+1', '(END)']
        self.testCodeWriter.writeArithmetic('gt')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile', mode='r') as f:
            lines = f.read().splitlines()
            self.assertNotEqual(len(lines), 0)
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter += 1

    def test_writeArithmeticLT(self):
        answer = ['@SP\t\t//SP--', 'M=M-1', 'A=M\t\t//D=*SP', 'D=M', '@SP\t\t//SP--', 'M=M-1', 'A=M',
                  '@GREATER\t// Jump to greater if top item in stack is greater than the one below it', 'D-M;JGT',
                  'M=1\t// Not greater therefore set stack entry at SP to 1 and then jump to end infinite loop',
                  '@SP\t// Increment SP', 'M=M+1', '@END', '0;JMP', '(GREATER)',
                  'M=0\t// We jumped here because top item was greate than item below it so set top Stack entry to 0',
                  '@SP\t// Increment SP', 'M=M+1', '(END)']
        self.testCodeWriter.writeArithmetic('lt')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile', mode='r') as f:
            lines = f.read().splitlines()
            self.assertNotEqual(len(lines), 0)
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter += 1

    def test_writeArithmeticEQ(self):
        answer = ['@SP\t\t//SP--', 'M=M-1', 'A=M\t\t//D=*SP', 'D=M', '@SP\t\t//SP--', 'M=M-1', 'A=M', 'D=D-M',
                  '@NOTEQUAL\t// Jump to notequal if top item in stack is not equal to the one below it', 'D;JNE',
                  '@SP', 'A=M',
                  'M=1\t// Equal therefore set stack entry at SP to 1 and then jump to end infinite loop',
                  '@SP\t// Increment SP', 'M=M+1', '@END', '0;JMP', '(NOTEQUAL)','@SP', 'A=M',
                  'M=0\t// We jumped here because top item was not equal to the item below it so set top Stack entry to 0',
                  '@SP\t// Increment SP', 'M=M+1', '(END)']
        self.testCodeWriter.writeArithmetic('eq')
        self.testCodeWriter.close()
        counter = 0
        with open('/tmp/testfile', mode='r') as f:
            lines = f.read().splitlines()
            self.assertNotEqual(len(lines), 0)
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter += 1






if __name__ == '__main__':
    unittest.main()
