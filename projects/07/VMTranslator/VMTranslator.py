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

    def gotoLine(self, n):
        """ goto line n - used for testing """
        self.fileIndex = n

    def hasMoreCommands(self):
        """ indicate if we can advance further """
        if self.fileIndex < len(self.lines) - 1:
            return True
        else:
            return False

    def commandType(self):
        """ return the type of command"""
        # todo C_FUNCTION, C_RETURN, C_CALL
        currentLine = self.lines[self.fileIndex]

        firstCommand = currentLine.split()[0]
        if  firstCommand in self.arithmeticCommands:        # Arithmetic commands
            return 'C_ARITHMETIC'
        elif firstCommand == 'push':                          # Push
            return 'C_PUSH'
        elif firstCommand =='pop':
            return 'C_POP'
        elif firstCommand == 'label':
            return 'C_LABEL'
        elif firstCommand == 'goto':
            return 'C_GOTO'
        elif firstCommand == 'if-goto':
            return 'C_IF'
        else:
            return 'ERROR_NOCOMMANDMATCH'

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
        self.fileName=fileName
        self.uuid = 0

    def getNewUUID(self):
        self.uuid += 1
        return '$' + str(self.uuid)

    def setFileName(self, fileName):
        self.file = open(fileName, 'w')

    def close(self):
        self.file.close()

    def writeArithmetic(self, command):
        if command == 'add':
            self.file.write('@SP' + '\t\t//SP--' + '\n')
            self.file.write('M=M-1' + '\n')
            self.file.write('A=M' + '\t\t//D=*SP' '\n')
            self.file.write('D=M' + '\n')
            self.file.write('@SP' + '\t\t//SP--' + '\n')
            self.file.write('M=M-1' + '\n')
            self.file.write('A=M' + '\t\t//*SP=D+*SP' '\n')
            self.file.write('M=D+M' + '\n')
            self.file.write('@SP' + '\t\t//SP++' + '\n')
            self.file.write('M=M+1' + '\n')
        elif command == 'sub':
            self.file.write('@SP' + '\t\t//SP--' + '\n')
            self.file.write('M=M-1' + '\n')
            self.file.write('A=M' + '\t\t//D=*SP' '\n')
            self.file.write('D=M' + '\n')
            self.file.write('@SP' + '\t\t//SP--' + '\n')
            self.file.write('M=M-1' + '\n')
            self.file.write('A=M' + '\t\t//*SP=D+*SP' '\n')
            self.file.write('M=M-D' + '\n')
            self.file.write('@SP' + '\t\t//SP++' + '\n')
            self.file.write('M=M+1' + '\n')
        elif command == 'or':
            self.file.write('@SP' + '\t\t//SP--' + '\n')
            self.file.write('M=M-1' + '\n')
            self.file.write('A=M' + '\t\t//D=*SP' '\n')
            self.file.write('D=M' + '\n')
            self.file.write('@SP' + '\t\t//SP--' + '\n')
            self.file.write('M=M-1' + '\n')
            self.file.write('A=M' + '\t\t//*SP=D+*SP' '\n')
            self.file.write('M=D|M' + '\n')
            self.file.write('@SP' + '\t\t//SP++' + '\n')
            self.file.write('M=M+1' + '\n')
        elif command == 'and':
            self.file.write('@SP' + '\t\t//SP--' + '\n')
            self.file.write('M=M-1' + '\n')
            self.file.write('A=M' + '\t\t//D=*SP' '\n')
            self.file.write('D=M' + '\n')
            self.file.write('@SP' + '\t\t//SP--' + '\n')
            self.file.write('M=M-1' + '\n')
            self.file.write('A=M' + '\t\t//*SP=D+*SP' '\n')
            self.file.write('M=D&M' + '\n')
            self.file.write('@SP' + '\t\t//SP++' + '\n')
            self.file.write('M=M+1' + '\n')
        elif command == 'neg':
            self.file.write('@SP' + '\t\t//SP--' + '\n')
            self.file.write('M=M-1' + '\n')
            self.file.write('A=M' + '\t\t//*SP=-*SP' '\n')
            self.file.write('M=-M' + '\n')
            self.file.write('@SP' + '\t\t//SP++' + '\n')
            self.file.write('M=M+1' + '\n')
        elif command == 'not':
            self.file.write('@SP' + '\t\t//SP--' + '\n')
            self.file.write('M=M-1' + '\n')
            self.file.write('A=M' + '\t\t//*SP=-*SP' '\n')
            self.file.write('M=!M' + '\n')
            self.file.write('@SP' + '\t\t//SP++' + '\n')
            self.file.write('M=M+1' + '\n')
        elif command == 'gt':
            GREATERUUID = self.getNewUUID()
            ENDUUID = self.getNewUUID()
            self.file.write('@SP' + '\t\t//SP--' + '\n')
            self.file.write('M=M-1' + '\n')
            self.file.write('A=M' + '\t\t//D=*SP' '\n')
            self.file.write('D=M' + '\n')
            self.file.write('@SP' + '\t\t//SP--' + '\n')
            self.file.write('M=M-1' + '\n')
            self.file.write('A=M' + '\n')
            self.file.write('D=M-D' + '\n')
            self.file.write('@GREATER' + GREATERUUID + '\t// Jump to greater if top item in stack is greater than the one below it' + '\n')
            self.file.write('D;JGT' +'\n')
            self.file.write('@SP' + '\n')
            self.file.write('A=M' + '\n')
            self.file.write('M=0' + '\t// Not greater therefore set stack entry at SP to 0 and then jump to end infinite loop' + '\n')
            self.file.write('@SP' + '\t// Increment SP' +'\n')
            self.file.write('M=M+1' +'\n')
            self.file.write('@END' + ENDUUID +'\n')
            self.file.write('0;JMP' + '\n')
            self.file.write('(GREATER' +GREATERUUID + ')' + '\n')
            self.file.write('@SP' + '\n')
            self.file.write('A=M' + '\n')
            self.file.write('M=-1' + '\t// We jumped here because top item was greate than item below it so set top Stack entry to -1' + '\n')
            self.file.write('@SP' + '\t// Increment SP' +'\n')
            self.file.write('M=M+1' + '\n')
            self.file.write('(END' + ENDUUID + ')' + '\n')
        elif command == 'lt':
            LESSUUID = self.getNewUUID()
            ENDUUID = self.getNewUUID()
            self.file.write('@SP' + '\t\t//SP--' + '\n')
            self.file.write('M=M-1' + '\n')
            self.file.write('A=M' + '\t\t//D=*SP' '\n')
            self.file.write('D=M' + '\n')
            self.file.write('@SP' + '\t\t//SP--' + '\n')
            self.file.write('M=M-1' + '\n')
            self.file.write('A=M' + '\n')
            self.file.write('D=D-M' + '\n')
            self.file.write('@LESS' + LESSUUID + '\t// Jump to less if top item in stack is greater than the one below it' + '\n')
            self.file.write('D;JGT' +'\n')
            self.file.write('@SP' + '\n')
            self.file.write('A=M' + '\n')
            self.file.write('M=0' + '\t// Not greater therefore set stack entry at SP to 1 and then jump to end infinite loop' + '\n')
            self.file.write('@SP' + '\t// Increment SP' +'\n')
            self.file.write('M=M+1' +'\n')
            self.file.write('@END' + ENDUUID +'\n')
            self.file.write('0;JMP' + '\n')
            self.file.write('(LESS' + LESSUUID + ')' + '\n')
            self.file.write('@SP' + '\n')
            self.file.write('A=M' + '\n')
            self.file.write('M=-1' + '\t// We jumped here because top item was greater than item below it so set top Stack entry to -1' + '\n')
            self.file.write('@SP' + '\t// Increment SP' +'\n')
            self.file.write('M=M+1' + '\n')
            self.file.write('(END' + ENDUUID + ')' + '\n')
        elif command == 'eq':
            ENDUUID = self.getNewUUID()
            NOTEQUALUUID = self.getNewUUID()
            self.file.write('@SP' + '\t\t//SP--' + '\n')
            self.file.write('M=M-1' + '\n')
            self.file.write('A=M' + '\t\t//D=*SP' '\n')
            self.file.write('D=M' + '\n')
            self.file.write('@SP' + '\t\t//SP--' + '\n')
            self.file.write('M=M-1' + '\n')
            self.file.write('A=M' + '\n')
            self.file.write('D=D-M' + '\n')
            self.file.write('@NOTEQUAL' + NOTEQUALUUID + '\t// Jump to notequal if top item in stack is not equal to the one below it' + '\n')
            self.file.write('D;JNE' +'\n')
            self.file.write('@SP' + '\n')
            self.file.write('A=M' + '\n')
            self.file.write('M=-1' + '\t// Equal therefore set stack entry at SP to 1 and then jump to end infinite loop' + '\n')
            self.file.write('@SP' + '\t// Increment SP' +'\n')
            self.file.write('M=M+1' +'\n')
            self.file.write('@END'+ ENDUUID +'\n')
            self.file.write('0;JMP' + '\n')
            self.file.write('(NOTEQUAL' + NOTEQUALUUID + ')' + '\n')
            self.file.write('@SP' + '\n')
            self.file.write('A=M' + '\n')
            self.file.write('M=0' + '\t// We jumped here because top item was not equal to the item below it so set top Stack entry to 0' + '\n')
            self.file.write('@SP' + '\t// Increment SP' +'\n')
            self.file.write('M=M+1' + '\n')
            self.file.write('(END' + ENDUUID + ')' + '\n')

    def writePushPop(self, command, segment, index):
        """ Implement push and pop functionality """
        segmap = {'local':'LCL', 'argument': 'ARG', 'this':'THIS', 'that':'THAT'}
        if command == 'C_PUSH':
            if segment == 'constant':
                self.file.write('@' + str(index) + '\t\t//D=' + str(index) + '\n')
                self.file.write('D=A' + '\n')
                self.file.write('@SP' + '\t\t//*SP=D' + '\n' )
                self.file.write('A=M' + '\n')
                self.file.write('M=D' + '\n')
                self.file.write('@SP' + '\t\t//SP++' + '\n')
                self.file.write('M=M+1' + '\n')
            elif segment in ["local","argument", 'this', 'that']:
                SEGLABEL = '@' + segmap[segment]
                self.file.write('@' + index + '\t// Store address relative to ' + SEGLABEL +' (offset)' +'\n')
                self.file.write('D=A' +'\n')
                self.file.write('@i' + '\n')
                self.file.write('M=D' + '\n')
                self.file.write(SEGLABEL +'\t// Store ' + SEGLABEL + ' + i' +'\n')
                self.file.write('D=M' + '\n')
                self.file.write('@TEMPADDR' + '\n')
                self.file.write('M=D' + '\n')
                self.file.write('@i' + '\n')
                self.file.write('D=M' + '\n')
                self.file.write('@TEMPADDR' + '\n')
                self.file.write('M=M+D' + '\n')
                self.file.write('@TEMPADDR\t// Store local[i] in D' + '\n')
                self.file.write('A=M' + '\n')
                self.file.write('D=M' + '\n')
                self.file.write('@SP\t// set the topmost value in the stack to D' + '\n')
                self.file.write('A=M' + '\n')
                self.file.write('M=D' + '\n')
                self.file.write('@SP' + '\n')
                self.file.write('M=M+1' + '\n')
            elif segment == 'static':
                funcname = '@' + self.fileName.split('/')[-1].split('.')[0] + '.' + index
                self.file.write(funcname + '\t// Read in funcname.index and put on top of stack' + '\n')
                self.file.write('D=M' + '\n')
                self.file.write('@SP' + '\n')
                self.file.write('A=M' +'\n')
                self.file.write('M=D' + '\n')
                self.file.write('@SP' + '\t// increment Stack pointer' + '\n')
                self.file.write('M=M+1' + '\n')
            elif segment == 'temp':
                self.file.write('@' + index +'\t// Store address relative to 5' +'\n')
                self.file.write('D=A' + '\n')
                self.file.write('@i' + '\n')
                self.file.write('M=D' + '\n')
                self.file.write('@5' + '\n')
                self.file.write('D=A' + '\n')
                self.file.write('@TEMPADDR' + '\n')
                self.file.write('M=D' + '\n')
                self.file.write('@i\t// Store local[i] in D' + '\n')
                self.file.write('D=M+D' + '\n')
                self.file.write('A=D' + '\n')
                self.file.write('D=M' + '\n')
                self.file.write('@SP\t// set the topmost value in the stack to D' + '\n')
                self.file.write('A=M' + '\n')
                self.file.write('M=D' + '\n')
                self.file.write('@SP' + '\n')
                self.file.write('M=M+1' + '\n')
            elif segment == 'pointer':
                self.file.write('@' + index +'\t// Store address relative to 5' +'\n')
                self.file.write('D=A' + '\n')
                self.file.write('@i' + '\n')
                self.file.write('M=D' + '\n')
                self.file.write('@3' + '\n')
                self.file.write('D=A' + '\n')
                self.file.write('@TEMPADDR' + '\n')
                self.file.write('M=D' + '\n')
                self.file.write('@i\t// Store local[i] in D' + '\n')
                self.file.write('D=M+D' + '\n')
                self.file.write('A=D' + '\n')
                self.file.write('D=M' + '\n')
                self.file.write('@SP\t// set the topmost value in the stack to D' + '\n')
                self.file.write('A=M' + '\n')
                self.file.write('M=D' + '\n')
                self.file.write('@SP' + '\n')
                self.file.write('M=M+1' + '\n')

        elif command == "C_POP":
            if segment in ["local","argument", 'this', 'that']:
                SEGLABEL = '@' + segmap[segment]
                self.file.write('@' + index + '\t// Store address relative to ' + SEGLABEL +' (offset)' +'\n')
                self.file.write('D=A' +'\n')
                self.file.write('@i' + '\n')
                self.file.write('M=D' + '\n')
                self.file.write(SEGLABEL +'\t// Store ' + SEGLABEL + ' + i' +'\n')
                self.file.write('D=M' + '\n')
                self.file.write('@TEMPADDR' + '\n')
                self.file.write('M=D' + '\n')
                self.file.write('@i' + '\n')
                self.file.write('D=M' + '\n')
                self.file.write('@TEMPADDR' + '\n')
                self.file.write('M=M+D' + '\n')
                self.file.write('@SP\t//    SP--' + '\n')
                self.file.write('M=M-1' + '\n')
                self.file.write('@SP\t// Store top stack value in D' + '\n')
                self.file.write('A=M' + '\n')
                self.file.write('D=M' + '\n')
                self.file.write('@TEMPADDR\t// set MEM[TEMPADDR] (LCL+i) to D' + '\n')
                self.file.write('A=M' + '\n')
                self.file.write('M=D' + '\n')
            elif segment == 'constant':
                print "ERROR: constant should only push!"
            elif segment == 'static':
                funcname = '@' + self.fileName.split('/')[-1].split('.')[0] + '.' + index
                self.file.write('@SP' + '\t// take from top of stack and save to filename.index' + '\n')
                self.file.write('M=M-1' + '\n')
                self.file.write('A=M' + '\n')
                self.file.write('D=M' + '\n')
                self.file.write(funcname +  '\n')
                self.file.write('M=D' + '\n')
            elif segment == 'temp':
                self.file.write('@' + index +'\t// Store address relative to 5' +'\n')
                self.file.write('D=A' + '\n')
                self.file.write('@i' + '\n')
                self.file.write('M=D' + '\n')
                self.file.write('@5' + '\n')
                self.file.write('D=A' + '\n')
                self.file.write('@TEMPADDR' + '\n')
                self.file.write('M=D' + '\n')
                self.file.write('@i\t// Store local[i] in D' + '\n')
                self.file.write('D=M' + '\n')
                self.file.write('@TEMPADDR' + '\n')
                self.file.write('M=M+D' + '\n')
                self.file.write('@SP' + '\n')
                self.file.write('M=M-1' + '\n')
                self.file.write('A=M'+ '\n')
                self.file.write('D=M' + '\n')
                self.file.write('@TEMPADDR' + '\n')
                self.file.write('A=M' + '\n')
                self.file.write('M=D' + '\n')
            elif segment == 'pointer':
                self.file.write('@' + index +'\t// Store address relative to 5' +'\n')
                self.file.write('D=A' + '\n')
                self.file.write('@i' + '\n')
                self.file.write('M=D' + '\n')
                self.file.write('@3' + '\n')
                self.file.write('D=A' + '\n')
                self.file.write('@TEMPADDR' + '\n')
                self.file.write('M=D' + '\n')
                self.file.write('@i\t// Store local[i] in D' + '\n')
                self.file.write('D=M' + '\n')
                self.file.write('@TEMPADDR' + '\n')
                self.file.write('M=M+D' + '\n')
                self.file.write('@SP' + '\n')
                self.file.write('M=M-1' + '\n')
                self.file.write('A=M'+ '\n')
                self.file.write('D=M' + '\n')
                self.file.write('@TEMPADDR' + '\n')
                self.file.write('A=M' + '\n')
                self.file.write('M=D' + '\n')
        else:
            print "ERROR: no push or pop!"


def VMTranslator(fileName):
    vmParse = Parser(fileName)
    vmCodeWriter = CodeWriter(fileName.split(".")[0] + '.asm')
    while True:
        commandType = vmParse.commandType()
        arg1 = vmParse.arg1()
        arg2 = vmParse.arg2()
        print commandType, arg1, arg2
        if commandType == 'C_PUSH':
            print commandType + " PUSH!"
            vmCodeWriter.writePushPop(commandType, arg1, arg2)
        elif commandType == 'C_POP':
            print commandType + " POP!"
            vmCodeWriter.writePushPop(commandType, arg1, arg2)
        elif commandType == 'C_ARITHMETIC':
            print commandType + " ARITHMETIC"
            vmCodeWriter.writeArithmetic(arg1)
        else:
            print commandType + " Error - Catch all reached"
        if vmParse.hasMoreCommands():
            vmParse.advance()
        else:
            break
    vmCodeWriter.close()

if __name__ == '__main__':
    VMTranslator(sys.argv[1])






