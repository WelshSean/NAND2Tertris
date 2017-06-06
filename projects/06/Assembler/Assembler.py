class Parser(object):
    """
    Parser - this class is tasked with breaking each assembly command into field and Symbols

    Attributes:
        filename: path to the file that is going to be parsed
    """


    def __init__(self, fileName):
        """ Open the file specified and ready it for parsing """

        stem = fileName.split(".")[0]  # Making assumption that file is stem.asm
        print "Stem: " + str(stem)
        self.inputFile = open(fileName, 'r')
        self.outputFile = open(stem + ".hack", 'w')
        #self.line =  self.inputFile.readline()    # Current line in program
        self.advance()

    def getCommand(self):
        """ return the raw value of the curret line - used for testing """
        return self.line

    def advance(self):
        """ move to the next line that doesnt line containing a command """
        import re
        while True:
            self.line = self.inputFile.readline().rstrip("\r\n")
            if (not re.match(self.line, '^\/\/.*$')) and (not re.match(self.line, '^$')):
                break

    def commandType(self):
        """ Indicate what type of command:
            A_COMMAND:  @xxx where xxx is a symbol or decimal number
            C_COMMAND: commands of form dest=comp;jump
            L_COMMAND: (xxx) where xxx is a symbol
        """
        pass




