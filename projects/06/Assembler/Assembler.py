import re
import sys



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
        """ Indicate what type of command:
            A_COMMAND:  @xxx where xxx is a symbol or decimal number
            C_COMMAND: commands of form dest=comp;jump
            L_COMMAND: (xxx) where xxx is a symbol
        """
        currentLine = self.lines[self.fileIndex]
        print "CURRENTLINE:" + str(currentLine)
        if re.match('^\s*@[A-Za-z0-9_]+\s*.*$', currentLine):
            return "A"
        elif re.match('^\s*[ADM]{1,3}?=', currentLine) or re.match('.+;J..', currentLine):
            return "C"
        elif re.match('^\s*\([A-Za-z0-9_]+\)\s*$', currentLine):
            return "L"
        else:
            return"ERR_NOMATCH"

    def symbol(self):
        """ Returns the Symbol or Decimal part of an A command @100 or @SYMBOL"""
        currentLine = self.lines[self.fileIndex]
        if self.commandType() == "A":
            return re.search('^\s*@([0-9A-Za-z_]+)\s*.*$', currentLine).group(1)
        elif self.commandType() == "L":
            #return re.search('^\s*\(([0-9A-Za-z_])\)\s*.*$', currentLine).group(1)
            return re.search('\((.+)\)', currentLine).group(1)
        else:
            print "Error: - called when not A commmand: " + str(currentLine)
            return "-1"

    def dest(self):
        """ Returns the dest Mnemonic from dest = comp;jump """
        currentLine = self.lines[self.fileIndex]
        if self.commandType() == "C":
            m = re.search('([ADM]{1,3})=.+', currentLine)
            if m:
                return m.group(1)
            else:
                return "None"
        else:
            print "Error: - called when not C commmand: " + str(currentLine)
            return "-1"


    def comp(self):
        """ Returns the comp Mnemonic from dest = comp;jump """
        currentLine = self.lines[self.fileIndex]
        if self.commandType() == "C":
            if re.search('=', currentLine):
                m = re.search('([ADM]+=){0,1}([ADM0\-1\+|&]+)(;J..){0,1}', currentLine)
                if m:
                    return m.group(2)
                else:
                    print "bleugh"
            elif re.search(';', currentLine):
                m = re.search('([ADM]+=){0,1}([ADM0\-1\+|&]+)(;J..){0,1}', currentLine)
                if m:
                    return m.group(2)
                else:
                    print "bleugh"
        else:
            print "Error: - called when not C commmand: " + str(currentLine)
            return "-1"

    def jump(self):
        """ returns the jump Mnemonic from dest=comp;jump """
        currentLine = self.lines[self.fileIndex]
        if self.commandType() == "C":
            find_jump = re.search('^.+;(J..).*$', currentLine)
            if find_jump:
                return find_jump.group(1)
            else:
                return "NOJUMP"
        else:
            print "Error: - called when not C commmand: " + str(currentLine)
            return "-1"

class Code(object):
    """
    Code - this class maps mnemonics to binary code
    """


    def __init__(self):
        """ Setup lookup tables """

        self.jumpLookup={ 'JGT' : '001',
                         'JEQ' : '010',
                         'JGE' : '011',
                         'JLT' : '100',
                         'JNE' : '101',
                         'JLE' : '110',
                         'JMP' : '111',
                         'NOJUMP': '000'}

        self.destLookup={ 'M' : '001',
                          'D' : '010',
                          'MD' : '011',
                          'A' : '100',
                          'AM' : '101',
                          'AD' : '110',
                          'AMD' : '111'}
    # for compLookup format is a c1 c2 c3 c4 c5 c6

        self.compLookup={'0' : '0101010',
                         '1' : '0111111',
                         '-1' : '0111010',
                         'D' : '0001100',
                         'A' : '0110000',
                         '!D' : '0001101',
                         '!A' : '0110001',
                         '-D' : '0001111',
                         '-A' : '0110011',
                         'D+1' : '0011111',
                         'A+1' : '0110111',
                         'D-1' : '0001110',
                         'A-1' : '0110010',
                         'D+A' : '0000010',
                         'D-A' : '0010011',
                         'A-D' : '0000111',
                         'D&A' : '0000000',
                         'D|A' : '0010101',
                         'M' : '1110000',
                         '!M' : '1110001',
                         '-M' : '1110011',
                         'M+1' : '1110111',
                         'M-1' : '1110010',
                         'D+M' : '1000010',
                         'D-M' : '1010011',
                         'M-D' : '1000111',
                         'D&M' : '1000000',
                         'D|M' : '1010101'}

    def jump(self, mnemonic):
        """ Lookup binary codes for jump mnemonics"""
        if not (mnemonic is None):
            return self.jumpLookup[mnemonic]
        else:
            return "000"

    def dest(self, mnemonic):
        """ Lookup binary codes for dest mnemonics """
        if not (mnemonic is None) and mnemonic != "None":
            return self.destLookup[mnemonic]
        else:
            return "000"

    def comp(self, mnemonic):
        """ Lookup binary codes for comp mnemonics"""
        return self.compLookup[mnemonic]

class SymbolTable(object):
    """ This class models the symbol table"""

    def __init__(self):
        self.table = {}

    def addEntry(self, key, address):
        self.table[key] = address

    def contains(self, key):
        return key in self.table.keys()

    def GetAddress(self, key):
        if key in self.table.keys():
            return self.table[key]
        else:
            return -1



def convA2Bin(decNumber):
    binNumber = "{0:b}".format(decNumber)
    binNumber = (15 - len(str(binNumber)))*"0" + binNumber
    return binNumber


def assembler(fileName):
    """
    main assembler program that uses the classes that do most of the work
    :param fileName: name of the .asm file to be compiled
    :return: Return code
    """
    output=[]
    stem = fileName.split(".")[0]  # Making assumption that file is stem.asm

    outputFile = open(stem + ".hack", 'w')

    codeParser=Parser(fileName)
    codeLookup=Code()
    symboltable = SymbolTable()
    ram_address = 16
    # Init symbol table
    symboltable.addEntry("SP", 0)
    symboltable.addEntry("LCL", 1)
    symboltable.addEntry("ARG", 2)
    symboltable.addEntry("THIS", 3)
    symboltable.addEntry("THAT", 4)
    for index in range(0,16):
        symboltable.addEntry("R" + str(index), index)
    symboltable.addEntry("SCREEN", 16384)
    symboltable.addEntry("KBD", 24576)

    print symboltable.table

    # Pass1

    ParserPassOne = Parser(fileName)
    index = 0
    while True:
        line=ParserPassOne.getLine()
        if ParserPassOne.commandType() == "L":
            symboltable.addEntry(ParserPassOne.symbol(), index)
        if ParserPassOne.commandType() == "A" or ParserPassOne.commandType() == 'C':
            index +=1

        if ParserPassOne.hasMoreCommands():
            ParserPassOne.advance()
        else:
            break

    # Pass2

    while True:
        line=codeParser.getLine()
        print "ASSEMBLER: " + str(line)
        type = codeParser.commandType()

        if type == "A":
            symbol = codeParser.symbol()
            if symboltable.contains(symbol):    # Existing symbol so subsititute value
                print "SYMB: " + str(symbol)
                symbol = symboltable.GetAddress(symbol)
                assembledLine = "0" + convA2Bin(int(symbol))
            else:
                if re.match("^[A-Za-z_]+$", symbol):            # If symbol isnt only numeric then new declaration so create and go onto next line - no output to write
                    symboltable.addEntry(symbol, ram_address)
                    ram_address += 1
                    continue
                else:                                           # Substitute value for numeric symbol
                    assembledLine = "0" + convA2Bin(int(symbol))
        elif type == "C":
            assembledLine = "111" + codeLookup.comp(codeParser.comp()) + codeLookup.dest(codeParser.dest()) + codeLookup.jump(codeParser.jump())

        if codeParser.commandType() == "A" or codeParser.commandType() == 'C':
            outputFile.write(assembledLine + "\n")
            output.append(assembledLine)

        if codeParser.hasMoreCommands():
            codeParser.advance()
        else:
            break
    outputFile.close()

    return output


if __name__ == "__main__":
    assembler(sys.argv[1])





