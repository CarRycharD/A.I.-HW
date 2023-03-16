import unittest

from roman_numerals import RomanNumeral

class TestRomanNumeral(unittest.TestCase):
    def setUp(self):
        self.rn = RomanNumeral()

    def test_integer_to_roman(self):
        self.assertEqual(self.rn.integer_to_roman(2), 'II')
        self.assertEqual(self.rn.integer_to_roman(13), 'XIII')
        self.assertEqual(self.rn.integer_to_roman(78), 'LXXVIII')
        self.assertEqual(self.rn.integer_to_roman(789), 'DCCLXXXIX')
        self.assertEqual(self.rn.integer_to_roman(1999), 'MCMXCIX')
        self.assertEqual(self.rn.integer_to_roman(2022), 'MMXXII')

    def test_roman_to_integer(self):
        self.assertEqual(self.rn.roman_to_integer('XXI'), 21)
        self.assertEqual(self.rn.roman_to_integer('CXXXV'), 135)
        self.assertEqual(self.rn.roman_to_integer('DXCII'), 592)
        self.assertEqual(self.rn.roman_to_integer('MCMXCVI'), 1996)
        self.assertEqual(self.rn.roman_to_integer('MMXXII'), 2022)
        self.assertEqual(self.rn.roman_to_integer('MMMCMXCIX'), 3999)

if __name__ == '__main__':
    unittest.main()