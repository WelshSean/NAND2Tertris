import unittest
from Assembler import assembler
from Assembler import convA2Bin



class MyTestCase(unittest.TestCase):
    def test_convA2Bin(self):
        self.assertEqual(convA2Bin(10), "000000000001010")

    def test_assembly_Add(self):
        testOutput=assembler('/Users/Sean/Desktop/nand2tetris/projects/06/Assembler/add/Add.asm')
        self.assertEqual(len(testOutput), 6)
        counter = 0
        with open('/Users/Sean/Desktop/nand2tetris/projects/06/Assembler/add/Add.testhack', mode='r') as f:
            lines = f.read().splitlines()
        for line in lines:
            self.assertEqual(testOutput[counter],line)
            counter += 1


    def test_assembly_Max(self):
        testOutput = assembler('/Users/Sean/Desktop/nand2tetris/projects/06/Assembler/max/Max.asm')
        self.assertEqual(len(testOutput), 16)
        counter = 0
        with open("/Users/Sean/Desktop/nand2tetris/projects/06/Assembler/max/Max.testhack", mode='r') as f:
            lines = f.read().splitlines()
        for line in lines:
            self.assertEqual(testOutput[counter], line)
            counter += 1

if __name__ == '__main__':
    unittest.main()
