import unittest
from CompilationEngine import CompilationEngine
from JackTokeniser import JackTokenizer


class CETestCase(unittest.TestCase):
    def test_ClassSimplest(self):
        answer = [ '<class>',
                   '<keyword> class </keyword>',
                   '<identifier> bar </identifier>',
                   '<symbol> { </symbol>',
                   '<symbol> } </symbol>',
                   '</class>']
        testCompEngine = CompilationEngine('testSnippetClassSimplest.jack', '/tmp/output')
        testCompEngine.CompileClass()
        counter=0
        with open('/tmp/output', mode='r') as f:
            lines = f.read().splitlines()
            print("AAA", lines)
            self.assertNotEqual(len(lines), 0)
        for line in lines:
            print("BBB", line)
            self.assertEqual(line, answer[counter])
            counter += 1

        self.assertEqual(counter , len(answer))

    def test_ClassSimplestAndVarDec(self):
        answer = ['<class>',
                      '<keyword> class </keyword>',
                      '<identifier> bar </identifier>',
                      '<symbol> { </symbol>',
                      '<classVarDec>',
                      '<keyword> static </keyword>',
                      '<keyword> boolean </keyword>',
                      '<identifier> test </identifier>',
                      '<symbol> ; </symbol>',
                      '</classVarDec>',
                      '<symbol> } </symbol>',
                      '</class>']
        testCompEngine = CompilationEngine('testSnippetClassAndVarDec.jack', '/tmp/output')
        testCompEngine.CompileClass()
        counter = 0
        with open('/tmp/output', mode='r') as f:
            lines = f.read().splitlines()
            print("AAA", lines)
            self.assertNotEqual(len(lines), 0)
        for line in lines:
            print("BBB", line)
            self.assertEqual(line, answer[counter])
            counter += 1

        self.assertEqual(counter, len(answer))

    def test_ClassSimplestAndVarDec2Vars(self):
        answer = ['<class>',
                  '<keyword> class </keyword>',
                  '<identifier> bar </identifier>',
                  '<symbol> { </symbol>',
                  '<classVarDec>',
                  '<keyword> static </keyword>',
                  '<keyword> boolean </keyword>',
                  '<identifier> test </identifier>',
                  '<identifier> test2 </identifier>',
                  '<symbol> ; </symbol>',
                  '</classVarDec>',
                  '<symbol> } </symbol>',
                  '</class>']
        testCompEngine = CompilationEngine('testSnippetClassAndVarDec2Vars.jack', '/tmp/output')
        testCompEngine.CompileClass()
        counter = 0
        with open('/tmp/output', mode='r') as f:
            lines = f.read().splitlines()
            print("AAA", lines)
            self.assertNotEqual(len(lines), 0)
        for line in lines:
            print("BBB", line)
            self.assertEqual(line, answer[counter])
            counter += 1

        self.assertEqual(counter, len(answer))

    def test_ClassSimplestAndVarDec2VarDecs(self):
        answer = ['<class>',
                  '<keyword> class </keyword>',
                  '<identifier> bar </identifier>',
                  '<symbol> { </symbol>',
                  '<classVarDec>',
                  '<keyword> static </keyword>',
                  '<keyword> boolean </keyword>',
                  '<identifier> test </identifier>',
                  '<symbol> ; </symbol>',
                  '</classVarDec>',
                  '<classVarDec>',
                  '<keyword> field </keyword>',
                  '<keyword> int </keyword>',
                  '<identifier> test4 </identifier>',
                  '<symbol> ; </symbol>',
                  '</classVarDec>',
                  '<symbol> } </symbol>',
                  '</class>']
        testCompEngine = CompilationEngine('testSnippetClassAndVarDec2VarDecs.jack', '/tmp/output')
        testCompEngine.CompileClass()
        counter = 0
        with open('/tmp/output', mode='r') as f:
            lines = f.read().splitlines()
            print("AAA", lines)
            self.assertNotEqual(len(lines), 0)
        for line in lines:
            print("BBB", line)
            self.assertEqual(line, answer[counter])
            counter += 1

        self.assertEqual(counter, len(answer))






    # def test_VarDecSimplest(self):
    #     answer = [ '<class>','<keyword> class </keyword>', '</class>']
    #     testCompEngine = CompilationEngine('testSnippetClassSimplest.jack', '/tmp/output')
    #     testCompEngine.CompileClass()
    #     counter=0
    #     with open('/tmp/output', mode='r') as f:
    #         lines = f.read().splitlines()
    #         self.assertNotEqual(len(lines), 0)
    #     for line in lines:
    #         print(line)
    #         self.assertEqual(line, answer[counter])
    #         counter += 1


if __name__ == '__main__':
    unittest.main()
