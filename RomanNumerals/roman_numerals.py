class RomanNumeral:
    def __init__(self):
        # Create a dictionary to map Roman numerals to integers
        self.roman_to_int = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }

    def integer_to_roman(self, number: int) -> str:
        # Convert an integer to a Roman numeral
        roman_numeral = ""
        for symbol, value in self.roman_to_int.items():
            count = number // value
            roman_numeral += symbol * count
            number -= value * count
        return roman_numeral

    def roman_to_integer(self, roman: str) -> int:
        # Convert a Roman numeral to an integer
        total = 0
        for i, symbol in enumerate(roman):
            value = self.roman_to_int[symbol]
            if i < len(roman) - 1 and value < self.roman_to_int[roman[i + 1]]:
                # Subtract value if the current symbol is smaller than the next symbol
                total -= value
            else:
                # Add value if the current symbol is greater than or equal to the next symbol
                total += value
        return total
