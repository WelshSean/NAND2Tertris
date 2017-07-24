import unittest
from JackTokeniser import JackTokenizer


class testJackTokenizer(unittest.TestCase):
    def setUp(self):
        self.testJackTokenizer = JackTokenizer('testSnippet.jack')
        #self.reader = open('/tmp/testfile.asm', 'r')

    def test_hasMoreTokens(self):
        self.assertEqual(True, self.testJackTokenizer.hasMoreTokens())

    # def test_advanceSimple(self):
    #     self.testJackTokenizer.advance()
    #     self.assertEqual('SYMBOL', self.testJackTokenizer.tokenType())
    #     self.assertEqual('(', self.testJackTokenizer.symbol())
    #
    # def test_advance_intval(self):
    #     self.testJackTokenizer.advance()
    #     self.testJackTokenizer.advance()
    #     self.testJackTokenizer.advance()
    #     self.testJackTokenizer.advance()
    #     self.testJackTokenizer.advance()
    #     self.assertEqual('INT_CONST', self.testJackTokenizer.tokenType())
    #     self.assertEqual('234', self.testJackTokenizer.intVal())
    #
    # def test_advance_stringval(self):
    #     self.testJackTokenizer.advance()
    #     self.testJackTokenizer.advance()
    #     self.testJackTokenizer.advance()
    #     self.testJackTokenizer.advance()
    #     self.testJackTokenizer.advance()
    #     self.testJackTokenizer.advance()
    #     self.testJackTokenizer.advance()
    #     self.assertEqual('STRING_CONST', self.testJackTokenizer.tokenType())
    #     self.assertEqual('Schurgle', self.testJackTokenizer.stringVal())

    def test_removeCommentsFromList(self):
        self.assertEqual(self.testJackTokenizer.removeCommentsFromList(['good line', 'commented line/** should go*/']),
                         ['good line', 'commented line'])

    def test_removeCommentsFromList2(self):
        self.assertEqual(self.testJackTokenizer.removeCommentsFromList(['/**should go*/commented line/** should go*/']),
                         ['commented line'])

    def test_removeCommentsFromList3(self):
        self.assertEqual(self.testJackTokenizer.removeCommentsFromList(['/*should go*/commented line/* should go*/']),
                         ['commented line'])


if __name__ == '__main__':
    unittest.main()



