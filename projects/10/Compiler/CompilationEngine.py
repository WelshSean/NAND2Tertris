import re
from JackTokeniser import JackTokenizer

class CompilationEngine(object):
    """
    Compile a Jack source file
    """

    def __init__(self, jackFile, vmFile):
        """ constructor - get ready for Compilation"""
        print(vmFile)
        self.outputFile = open(vmFile, 'w')
        self.Tokenizer = JackTokenizer(jackFile)

    def _write_opener(self, element):
        self.outputFile.write('<' + element + '>\n')

    def _write_closer(self, element):
        self.outputFile.write('</' + element + '>\n')

    def _write_entry(self, element, name):
        self.outputFile.write('<' + element + '> ' + name + ' </' + element + '>\n')

    def _eat(self,string):
        if self.Tokenizer.currentToken != string:
            raise ValueError('Eat didnt get the string that it expected')
        else:
            if self.Tokenizer.hasMoreTokens():
                self.Tokenizer.advance()

    def CompileClass(self):
        """ Compile a complete class
        Expecting the following form
        'class' className '{' classVarDec* subroutineDec* '}' """

        ## Go to first token
        self.Tokenizer.advance()

        ## Expecting class keyword
        self._eat('class')
        self._write_opener('class')
        self._write_entry('keyword','class')

        ## Now handle the identifier

        if not self.Tokenizer.currentTokenType == "IDENTIFIER":
            raise ValueError("ERROR_UNEXPECTED_TOKEN: " + self.Tokenizer.currentTokenType + " " + self.Tokenizer.currentToken )
        else:
            self._write_entry(self.Tokenizer.currentTokenType.lower(), self.Tokenizer.currentToken)

        self.Tokenizer.advance()

        ## Now opening curly bracket
        self._eat('{')
        self._write_entry('symbol','{')

        #self.Tokenizer.advance()


        # Now expecting 0 or more classVarDec

        # self.Tokenizer.advance()
        #
        # if self.Tokenizer.currentTokenType == "KEYWORD" and self.Tokenizer.currentToken in ["static", "field"]:
        #     self._write_closer('class')
        # self.outputFile.close()


        ## Finally the closing brace
        try:
            self._eat('}')
            self._write_entry('symbol', '}')
            self._write_closer('class')
        except:
            print("waah")

        self.outputFile.close()




    # def CompileVarDec(self):
    #     pass