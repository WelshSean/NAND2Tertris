import unittest
from VMTranslator import Parser


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.testParser = Parser('/Users/Sean/Desktop/nand2tetris/projects/07/StackArithmetic/SimpleAdd/SimpleAdd.vm')

    def test_removeCommentsAndWhitespace(self):
        test_list=['//ssss', '      ', 'one', 'two', '//three', 'three']
        output=Parser.removeCommentsAndWhitespace(test_list)
        self.assertEqual(output, ['one', 'two', 'three'])

    def test_init(self):
        """ Parser setup should read the first line of the file"""
        self.assertEqual(self.testParser.getLine(0), "push constant 7")
        self.assertEqual(self.testParser.getLine(2), "add")
        self.assertEqual(self.testParser.getNumberLines(), 3)

    def test_advance(self):
        """ Test that advance moves us to the second line of the file"""
        self.assertEqual(self.testParser.getLine(), "push constant 7")
        self.testParser.advance()
        self.assertEqual(self.testParser.getLine(), "push constant 8")

    def test_hasMoreCommands(self):
        self.assertTrue(self.testParser.hasMoreCommands())        # Line 1 - should be true
        self.testParser.advance()
        self.assertTrue(self.testParser.hasMoreCommands())        # Line 2 - should be true
        self.testParser.advance()
        self.assertFalse(self.testParser.hasMoreCommands())        # Line 3 - should be false













    if __name__ == '__main__':
        unittest.main()

