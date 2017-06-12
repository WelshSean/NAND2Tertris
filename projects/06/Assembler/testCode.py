import unittest
from Assembler import Code

class MyTestCase(unittest.TestCase):

    def test_jump_JGT(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.jump("JGT"), "001")

    def test_jump_JEQ(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.jump("JEQ"), "010")


    def test_jump_JGE(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.jump("JGE"), "011")

    def test_jump_JLT(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.jump("JLT"), "100")

    def test_jump_JNE(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.jump("JNE"), "101")

    def test_jump_JLE(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.jump("JLE"), "110")

    def test_jump_JMP(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.jump("JMP"), "111")

    def test_dest_M(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.dest("M"), "001")

    def test_dest_D(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.dest("D"), "010")

    def test_dest_MD(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.dest("MD"), "011")

    def test_dest_A(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.dest("A"), "100")

    def test_dest_AM(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.dest("AM"), "101")

    def test_dest_AD(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.dest("AD"), "110")

    def test_dest_AMD(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.dest("AMD"), "111")

    def test_comp_zero(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("0"), "0101010")

    def test_comp_one(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("1"), "0111111")

    def test_comp_minone(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("-1"), "0111010")

    def test_comp_D(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("D"), "0001100")

    def test_comp_A(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("A"), "0110000")

    def test_comp_notD(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("!D"), "0001101")

    def test_comp_notA(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("!A"), "0110001")

    def test_comp_minD(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("-D"), "0001111")

    def test_comp_minA(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("-A"), "0110011")

    def test_comp_DplusOne(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("D+1"), "0011111")

    def test_comp_AplusOne(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("A+1"), "0110111")

    def test_comp_DminOne(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("D-1"), "0001110")

    def test_comp_AminOne(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("A-1"), "0110010")

    def test_comp_DplusA(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("D+A"), "0000010")

    def test_comp_DminA(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("D-A"), "0010011")

    def test_comp_AminD(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("A-D"), "0000111")

    def test_comp_DandA(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("D&A"), "0000000")

    def test_comp_DorA(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("D|A"), "0010101")

    def test_comp_M(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("M"), "1110000")

    def test_comp_notM(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("!M"), "1110001")

    def test_comp_minM(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("-M"), "1110011")

    def test_comp_Mplus1(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("M+1"), "1110111")

    def test_comp_Mmin1(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("M-1"), "1110010")

    def test_comp_DplusM(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("D+M"), "1000010")

    def test_comp_DminM(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("D-M"), "1010011")

    def test_comp_MminD(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("M-D"), "1000111")

    def test_comp_DandM(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("D&M"), "1000000")

    def test_comp_DorM(self):
        self.testingCode = Code()
        self.assertEqual(self.testingCode.comp("D|M"), "1010101")



if __name__ == '__main__':
    unittest.main()
