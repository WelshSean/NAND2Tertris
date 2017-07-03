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
        with open(fileName) as f:
            self.lines = f.read().splitlines()
        self.lines = self.removeCommentsAndWhitespace(self.lines)
        self.arithmeticCommands=['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']


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

    def commandType(self):
        """ return the type of command"""
        # todo C_LABEL, C_GOTO, C_IF, C_FUNCTION, C_RETURN, C_CALL
        currentLine = self.lines[self.fileIndex]

        firstCommand = currentLine.split()[0]
        if  firstCommand in self.arithmeticCommands:        # Arithmetic commands
            return 'C_ARITHMETIC'
        elif firstCommand == 'push':                          # Push
            return 'C_PUSH'
        elif firstCommand =='pop':
            return 'C_POP'

    def arg1(self):
        """ return the first argument of the VM command """
        if self.commandType() == 'C_RETURN':
            return "C_ERROR_BAD_CALL"
        else:
            currentLine = self.lines[self.fileIndex]
            splitLine = currentLine.split()
            if self.commandType() != 'C_ARITHMETIC' and len(splitLine) > 1:
                return splitLine[1]
            elif self.commandType() == 'C_ARITHMETIC' and len(splitLine) == 1 :
                return splitLine[0]
            else:
                return 'C_ERROR_NOMATCH'

    def arg2(self):
        """ return the second argument of the VM command"""
        if self.commandType() in ['C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL']:
            currentLine = self.lines[self.fileIndex]
            return currentLine.split()[2]
        else:
            return 'C_BAD_CALL'


class CodeWriter(object):
    """
    CodeWriter - takes output of the Parser and creates output file
    """

    def __init__(self, fileName):
        self.file = open(fileName, 'w')

    def setFileName(self, fileName):
        self.file = open(fileName, 'w')

    def close(self):
        self.file.close()

    def writeArithmetic(self, command):
        pass

    def writePushPop(self, command, segment, index):
        """ Implement push and pop functionality """
        if command == 'C_PUSH':
            if segment == 'local':
                self.file.write('@' + str(index) + '\t\t//D=' + str(index) + '\n')
                self.file.write('D=A' + '\n')
                self.file.write('@SP' + '\t\t//*SP=D' + '\n' )
                self.file.write('A=M' + '\n')
                self.file.write('M=D' + '\n')
                self.file.write('@SP' + '\t\t//SP++' + '\n')
                self.file.write('M=M+1' + '\n')
            else:
                print "ERROR: local should only push!"






