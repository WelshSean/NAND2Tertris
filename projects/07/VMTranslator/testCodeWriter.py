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
            print lines
        for line in lines:
            print line
            self.assertEqual(line, answer[counter])
            counter +=1

    def test_writeArithmeticAdd(self):
        answer = ['one', 'two', 'three']
        self.testCodeWriter.writeArithmetic('add')
        for line in answer:
            pass
            #self.assertEqual(self.reader.readline().strip(), line)






if __name__ == '__main__':
    unittest.main()
