import unittest
from Assembler import Parser


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.testParser = Parser('/Users/Sean/Desktop/nand2tetris/projects/06/add/Add.asm')
    def test_init(self):
        """ Parser setup should read the first line of the file"""
        #testParser = Parser('/Users/Sean/Desktop/nand2tetris/projects/06/add/Add.asm')
        testLine = self.testParser.getCommand()
        self.assertEqual(testLine, "@2")

    def test_advance(self):
        """ Test that advance reads the next line of the file"""
        self.testParser.advance()
        testLine = self.testParser.getCommand()
        self.assertEqual(testLine, "D=A")

    if __name__ == '__main__':
        unittest.main()

