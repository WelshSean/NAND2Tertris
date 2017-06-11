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

    def test_advance(self):
        """ Test that advance moves us to the second line of the file"""
        testParser = Parser('/Users/Sean/Desktop/nand2tetris/projects/06/add/Add.asm')
        self.assertEqual(self.testParser.getLine(), "@2")
        self.testParser.advance()
        self.assertEqual(self.testParser.getLine(), "D=A")

    def test_hasMoreCommands(self):
        testParser = Parser('/Users/Sean/Desktop/nand2tetris/projects/06/add/Add.asm')
        self.assertTrue(testParser.hasMoreCommands())        # Line 1 - should be true
        testParser.advance()
        self.assertTrue(testParser.hasMoreCommands())        # Line 2 - should be true
        testParser.advance()
        testParser.advance()
        self.assertTrue(testParser.hasMoreCommands())        # Line 4 - should be true
        testParser.advance()
        testParser.advance()
        self.assertFalse(testParser.hasMoreCommands())       # Line 6 - should be false

    def test_commandType(self):
        """ Simple test, no jumps"""
        testParser = Parser('/Users/Sean/Desktop/nand2tetris/projects/06/add/Add.asm')
        goodRes = ['A', 'C', 'A', 'C', 'A', 'C']
        first=True
        for res in goodRes:
            if not first:
                testParser.advance()
            print str(res) + " : " + str(testParser.getLine())
            self.assertEqual(testParser.commandType(), res)
            first = False

    def test_commandTypeJump(self):
        """ More complicated test, includes jumps"""
        testParser = Parser('/Users/Sean/Desktop/nand2tetris/projects/06/max/MaxL.asm')
        goodRes = ['A', 'C', 'A', 'C', 'A', 'C', 'A', 'C', 'A', 'C', 'A', 'C', 'A', 'C', 'A', 'C']
        first=True
        for res in goodRes:
            if not first:
                testParser.advance()
            print str(res) + " : " + str(testParser.getLine())
            self.assertEqual(testParser.commandType(), res)
            first = False

    def test_symbol(self):
        """ return symbol for A commands"""
        testParser = Parser('/Users/Sean/Desktop/nand2tetris/projects/06/max/MaxL.asm')
        self.assertEqual(testParser.symbol(), "0")
        testParser.advance()
        testParser.advance()
        testParser.advance()
        testParser.advance()
        self.assertEqual(testParser.symbol(), "10")

    def test_symbolNotACommand(self):
        """ return symbol for A commands"""
        testParser = Parser('/Users/Sean/Desktop/nand2tetris/projects/06/max/MaxL.asm')
        self.assertEqual(testParser.symbol(), "0")
        testParser.advance()
        testParser.advance()
        testParser.advance()
        self.assertEqual(testParser.symbol(), "-1")

    def test_dest(self):
        """ Return the dest mnemonic for a C command"""
        testParser = Parser('/Users/Sean/Desktop/nand2tetris/projects/06/max/MaxL.asm')
        testParser.advance()
        self.assertEqual(testParser.dest(), 'D' )

    def test_destNoDest(self):
        """ Return the dest mnemonic for a C command - this case has no dest mnemonic - should return None"""
        testParser = Parser('/Users/Sean/Desktop/nand2tetris/projects/06/max/MaxL.asm')
        testParser.advance()
        testParser.advance()
        testParser.advance()
        testParser.advance()
        testParser.advance()
        self.assertEqual(testParser.dest(), 'None' )

    def test_comp(self):
        """ Return the comp mnenomic for a C command """
        testParser = Parser('/Users/Sean/Desktop/nand2tetris/projects/06/max/MaxL.asm')
        testParser.advance()
        self.assertEqual(testParser.comp(), 'M' )
        testParser.advance()
        testParser.advance()
        testParser.advance()
        testParser.advance()
        self.assertEqual(testParser.comp(), 'D' )





    if __name__ == '__main__':
        unittest.main()

