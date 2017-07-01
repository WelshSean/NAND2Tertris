import re
import sys

class Parser(object):
    """
    Parser - this class is tasked with breaking each VM up

    Attributes:
        filename: path to the file that is going to be parsed
    """


    def __init__(self, fileName):
        """ Open the file specified and ready it for parsing """

        stem = fileName.split(".")[0]  # Making assumption that file is stem.vm
        self.fileIndex=0
        self.inputFile = open(fileName, 'r')
        with open(fileName) as f:
            self.lines = f.read().splitlines()
        self.lines = self.removeCommentsAndWhitespace(self.lines)


    @staticmethod
    def removeCommentsAndWhitespace(fileList):
        """ when passed a list, this function will remove all entries that are empty lines, whitespace or comments"""

        return list(filter(lambda x: (not re.match('^ *$', x)and not re.match('^\/\/.*$', x )) , fileList))

    def getLine(self, index=-1):
        """ return the raw value of an indexed line - index = line number - 1 - used for testing """
        if index == -1:
            return self.lines[self.fileIndex]
        else:
            return self.lines[index]

    def getNumberLines(self):
        """ return the number of lines in file dict - used for testing"""
        return len(self.lines)

    def advance(self):
        """ move to the next line """
        self.fileIndex += 1

    def hasMoreCommands(self):
        """ indicate if we can advance further """
        if self.fileIndex < len(self.lines) - 1:
            return True
        else:
            return False
