import unittest
from JackTokeniser import JackTokenizer


class testJackTokenizer(unittest.TestCase):
    def setUp(self):
        self.testJackTokenizer = JackTokenizer('testSnippet.jack')

    def advance_n(self, n=1):
        for i in range(n):
            self.testJackTokenizer.advance()


    def test_hasMoreTokens(self):
        self.assertEqual(True, self.testJackTokenizer.hasMoreTokens())

    def test_advanceSimple(self):
        self.advance_n(4)
        self.assertEqual('SYMBOL', self.testJackTokenizer.tokenType())
        self.assertEqual('(', self.testJackTokenizer.symbol())

    def test_advance_intval(self):
        self.advance_n(10)
        self.assertEqual('INT_CONST', self.testJackTokenizer.tokenType())
        self.assertEqual('234', self.testJackTokenizer.intVal())

    def test_advance_stringval(self):
        self.advance_n(14)
        self.assertEqual('STRING_CONST', self.testJackTokenizer.tokenType())
        self.assertEqual('Schurgle', self.testJackTokenizer.stringVal())

    def test_removeCommentsFromList(self):
        self.assertEqual(self.testJackTokenizer.removeCommentsFromList(['good line', 'commented line/** should go*/']),
                         ['good line', 'commented line'])

    def test_removeCommentsFromList2(self):
        self.assertEqual(self.testJackTokenizer.removeCommentsFromList(['/**should go*/commented line/** should go*/']),
                         ['commented line'])

    def test_removeCommentsFromList3(self):
        self.assertEqual(self.testJackTokenizer.removeCommentsFromList(['/*should go*/commented line/* should go*/']),
                         ['commented line'])

    def test_removeCommentsFromList4(self):
        self.assertEqual(self.testJackTokenizer.removeCommentsFromList(['/** Expressionless version of projects/10/Square/Main.jack. */']),
                         [''])
    def test_removeCommentsFromList5(self):
        self.assertEqual(self.testJackTokenizer.removeCommentsFromList(['good line', 'commented line//should go ']),
                         ['good line', 'commented line'])

    def test_advance_symbol(self):
        self.advance_n(19)
        self.assertEqual('SYMBOL', self.testJackTokenizer.tokenType())
        self.assertEqual('{', self.testJackTokenizer.symbol())

    def test_advance_symbol2(self):
        self.advance_n(27)
        self.assertEqual('SYMBOL', self.testJackTokenizer.tokenType())
        self.assertEqual(';', self.testJackTokenizer.symbol())

    def test_advance_keyword(self):
        self.advance_n(28)
        self.assertEqual('KEYWORD', self.testJackTokenizer.tokenType())
        self.assertEqual('do', self.testJackTokenizer.keyWord())




if __name__ == '__main__':
    unittest.main()



