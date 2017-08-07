import re

class JackTokenizer(object):
    """
    Tokenise a Jack source file ready for the Parsing
    """

    def __init__(self, fileName):
        """ constructor - get ready for tokenising"""
        with open(fileName) as f:
            self.lines = f.read().splitlines()
        self.lines = self.removeCommentsAndWhitespace(self.lines)
        self.lines = self.removeCommentsFromList(self.lines)
        self.lines = list(" ".join(self.lines))
        self.ValidTokens = re.compile("[a-zA-Z(){}\[\].,;+=*/&|<>=~]")
        self.StringChars = re.compile("[a-zA-Z]")
        self.StringDigits = re.compile("[0-9]")
        self.Symbols = re.compile("[(){}\[\].,;+=*/&|<>=~]")
        self.ValidKeywords = ['class', 'constructor', 'function', 'method',
                              'field', 'static', 'var', 'int', 'char',
                              'boolean', 'void', 'true', 'false', 'null',
                              'this', 'let', 'do', 'if', 'else', 'while',
                              'return']
        self.CurrentToken=""
        self.CurrentTokenType=""

    @staticmethod
    def removeCommentsAndWhitespace(fileList):
        """ when passed a list, this function will remove all entries that are empty lines, whitespace or comments"""
        return list(filter(lambda x: (not re.match('^ *$', x)and not re.match('^\/\/.*$', x )
                                      and not re.match('^.*/\*\*.*\*/.*$', x)) , fileList))

    @staticmethod
    def removeCommentsFromList(fileList):
        """ When passed a list this will remove all entries that are commented in the form /** /*"""
        retlist=[]
        comment_pattern = re.compile("/\*\*.+?\*/")
        comment_pattern2 = re.compile("/\*.+?\*/")
        comment_pattern3 = re.compile("//.*$")
        spaces = re.compile('^\s+$')
        for item in fileList:
            print(item)
            item = comment_pattern.sub("", item)
            item = comment_pattern2.sub("", item)
            item = comment_pattern3.sub("", item)
            if not spaces.search(item):
                retlist.append(item)
            else:
                print("Ignoring empty line")
        return retlist


    def hasMoreTokens(self):
        """ checks to see if the line has more tokens in it"""
        if len(list((filter(self.ValidTokens.match, self.lines)))) != 0:
            return True

    def advance(self):
        """ loads next valid token"""
        in_token = False
        while True:
            print(self.lines)
            char = self.lines.pop(0)
            print(char)
            if self.Symbols.match(char):                    # Symbols
                self.currentTokenType = "SYMBOL"
                self.currentToken = char
                break
            elif self.StringDigits.match(char):             # Integer Const
                while self.StringDigits.match(self.lines[0]):
                    char = char + self.lines.pop(0)
                self.currentTokenType = "INT_CONST"
                self.currentToken = char
                break
            elif char == "\"":                              # String constant
                print("RAAR")
                char = "" # Ignore Leading Quote
                while self.lines[0] != "\"":
                    char = char + self.lines.pop(0)
                self.lines.pop(0)   # strip trailing quote
                self.currentTokenType = "STRING_CONST"
                self.currentToken = char
                break
            elif self.StringChars.match(char) or char == "_":       # keyword or identifier
                while self.StringChars.match(self.lines[0]) or \
                        self.StringDigits.match(self.lines[0]) or\
                                self.lines[0] == "_":
                    char = char + self.lines.pop(0)
                if char in self.ValidKeywords:                      # Keyword
                    self.currentTokenType = "KEYWORD"
                    self.currentToken = char
                    break
                else:                                               # Identifier
                    self.currentTokenType = "IDENTIFIER"
                    self.currentToken = char
                    break



    def tokenType(self):
        """ returns the current token type """
        return self.currentTokenType

    def symbol(self):
        if self.currentTokenType == "SYMBOL":
            return str(self.currentToken)
        else:
            return "ERR_NOT_SYMBOL"

    def intVal(self):
        if self.currentTokenType == "INT_CONST":
            return self.currentToken
        else:
            return "ERR_NOT_INT_CONST"

    def stringVal(self):
        if self.currentTokenType == "STRING_CONST":
            return self.currentToken
        else:
            return "ERR_NOT_STRING_CONST"

    def keyWord(self):
        if self.currentTokenType == "KEYWORD":
            return self.currentToken
        else:
            return "ERR_NOT_KEYWORD"

    def identifier(self):
        if self.currentTokenType == "IDENTIFIER":
            return self.currentToken
        else:
            return "ERR_NOT_IDENTIFIER"




if __name__ == "__main__":
    tok = JackTokenizer("testSnippet.jack")
    print(tok.lines)
    print(tok.hasMoreTokens())
    tok.advance()
    print(tok.tokenType())
    print(tok.keyWord())
    tok.advance()
    tok.advance()
    print(tok.tokenType())
    print(tok.identifier())
    tok.advance()
    tok.advance()
    print(tok.tokenType())
    print(tok.intVal())
    tok.advance()
    print(tok.tokenType())
    tok.advance()
    print(tok.tokenType())
    print (tok.stringVal())