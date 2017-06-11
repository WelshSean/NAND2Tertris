import unittest
from Assembler import Parser


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.testParser = Parser('/Users/Sean/Desktop/nand2tetris/projects/06/add/Add.asm')

    def test_removeCommentsAndWhitespace(self):
        test_list=['//ssss', '      ', 'one', 'two', '//three', 'three']
        output=Parser.removeCommentsAndWhitespace(test_list)
        self.assertEqual(output, ['one', 'two', 'three'])

    def test_init(self):
        """ Parser setup should read the first line of the file"""
        testParser = Parser('/Users/Sean/Desktop/nand2tetris/projects/06/add/Add.asm')
        self.assertEqual(self.testParser.getLine(0), "@2")
        self.assertEqual(self.testParser.getLine(3), "D=D+A")
        self.assertEqual(testParser.getNumberLines(), 6)

    # def test_advance(self):
    #     """ Test that advance reads the next line of the file"""
    #     self.testParser.advance()
    #     testLine = self.testParser.getCommand()
    #     print "TESTLINE: " + str(testLine)
    #     self.assertEqual(testLine, "D=A")

    if __name__ == '__main__':
        unittest.main()

