import re
import unittest

def add(numbers: str) -> int:
    if numbers.startswith('//'):
        delimiter, numbers = parse_custom_delimiter(numbers)
    else:
        delimiter = ','
    
    num_list = split_numbers(numbers, delimiter)
    return sum_numbers(num_list)


def parse_custom_delimiter(numbers: str) -> tuple:
    if numbers[2] == '[':
        end = numbers.index(']\n')
        delimiter = numbers[3:end]
        numbers = numbers[end + 2:]
    else:
        delimiter, numbers = numbers[2:].split('\n', 1)
    return delimiter, numbers


def split_numbers(numbers: str, delimiter: str) -> list:
    if len(delimiter) > 1:
        numbers = re.split(re.escape(delimiter), numbers)
    else:
        numbers = numbers.replace('\n', delimiter).split(delimiter)
    return numbers


def sum_numbers(num_list: list) -> int:
    valid_numbers = []
    negatives = []
    
    for num in num_list:
        number = parse_number(num)
        if number is not None:
            if number < 0:
                negatives.append(number)
            elif number <= 1000:
                valid_numbers.append(number)
    
    if negatives:
        raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")
    
    return sum(valid_numbers)


def parse_number(num: str) -> int:
    if num.lstrip('-').isdigit():
        return int(num)
    return None


# Test cases
class TestStringCalculator(unittest.TestCase):
    
    def test_expectZeroForEmptyInput(self):
        self.assertEqual(add(""), 0)
        
    def test_expectZeroForSingleZero(self):
        self.assertEqual(add("0"), 0)
        
    def test_expectSumForTwoNumbers(self):
        self.assertEqual(add("1,2"), 3)
        
    def test_ignoreNumbersGreaterThan1000(self):
        self.assertEqual(add("1,1001"), 1)
        
    def test_expectSumWithCustomDelimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)
        
    def test_expectSumWithNewlineDelimiter(self):
        self.assertEqual(add("1\n2,3"), 6)
    
    def test_throwExceptionForNegativeNumbers(self):
        with self.assertRaises(ValueError) as context:
            add("1,-2,3")
        self.assertEqual(str(context.exception), "negatives not allowed: -2")
    
    def test_multipleNegativeNumbers(self):
        with self.assertRaises(ValueError) as context:
            add("-1,-2,3")
        self.assertEqual(str(context.exception), "negatives not allowed: -1, -2")
    
    def test_customDelimiterOfAnyLength(self):
        self.assertEqual(add("//[***]\n1***2***3"), 6)
    
    def test_customDelimiterWithSpecialCharacters(self):
        self.assertEqual(add("//[$$$]\n1$$$2$$$3"), 6)
    
    def test_mixedDelimiters(self):
        self.assertEqual(add("//[;]\n1;2,3\n4"), 10)

if __name__ == '__main__':
    unittest.main()
