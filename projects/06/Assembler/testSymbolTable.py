import unittest

from Assembler import SymbolTable

class MyTestCase(unittest.TestCase):

    def test_addEntry(self):
        table = SymbolTable()
        table.addEntry("testkey", 69)
        self.assertEqual(table.table["testkey"], 69)

    def test_contains_empty(self):
        table = SymbolTable()
        answer = table.contains("testkey")
        self.assertEqual(answer, False)

    def test_contains_full(self):
        table = SymbolTable()
        table.addEntry("testkey", 69)
        answer = table.contains("testkey")
        self.assertEqual(answer, True)

    def test_GetAddressFull(self):
        table = SymbolTable()
        table.addEntry("testkey", 69)
        answer = table.GetAddress("testkey")
        self.assertEqual(answer, 69)

    def test_GetAddressEmpty(self):
        table = SymbolTable()
        table.addEntry("testkey", 69)
        answer = table.GetAddress("testkey2")
        self.assertEqual(answer, -1)


if __name__ == '__main__':
    unittest.main()
