import sys
import os
from JackTokeniser import JackTokenizer
from CompilationEngine import CompilationEngine

def JackAnalyzer(fileName):

    if os.path.isfile(fileName):
        inputFileList = [fileName]
        print("File is: " + str(inputFileList))
    elif os.path.isdir(fileName):
        inputFileList = glob.glob(fileName + '/*.jack')
        print("Files are: " + str(inputFileList) + " in: " + fileName)

    for fileName in inputFileList:
        outputfile = fileName.split(".")[0] + '.vm'
        compEngine = CompilationEngine(fileName, outputfile)
        compEngine.CompileClass()




if __name__ == "__main__":
    JackAnalyzer(sys.argv[1])