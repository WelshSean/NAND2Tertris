class Parser(object):
    """
    Parser - this class is tasked with breaking each assembly command into field and Symbols

    Attributes:
        filename: path to the file that is going to be parsed
    """


    def __init__(self, fileName):
        """ Open the file specified and ready it for parsing """

        stem = fileName.split(".")[0]  # Making assumption that file is stem.asm
        self.fileIndex=0
        self.inputFile = open(fileName, 'r')
        with open(fileName) as f:
            self.lines = f.read().splitlines()
        self.lines = self.removeCommentsAndWhitespace(self.lines)
        self.outputFile = open(stem + ".hack", 'w')

    @staticmethod
    def removeCommentsAndWhitespace(fileList):
        """ when passed a list, this function will remove all entries that are empty lines, whitespace or comments"""
        import re
        return list(filter(lambda x: (not re.match('^ *$', x)and not re.match('^\/\/.*$', x )) , fileList))

    def getLine(self, index):
        """ return the raw value of an indexed line - index = line number - 1 - used for testing """
        return self.lines[index]

    def getNumberLines(self):
        """ return the number of lines in file dict - used for testing"""
        return len(self.lines)

    def advance(self):
        """ move to the next line that doesnt line containing a command """
        import re
        while True:
            print "Searching...."
            self.line = self.inputFile.readline().rstrip("\r\n")
            print self.line
            if (not re.match('^\/\/.*$', self.line ) and not re.match('^$', self.line)):
                print "DIDNT MATCH"
                break

    def commandType(self):
        """ Indicate what type of command:
            A_COMMAND:  @xxx where xxx is a symbol or decimal number
            C_COMMAND: commands of form dest=comp;jump
            L_COMMAND: (xxx) where xxx is a symbol
        """
        pass




