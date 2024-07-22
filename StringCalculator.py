def add(numbers: str) -> int:
    if numbers.startswith('//'):
        delimiter, numbers = parse_custom_delimiter(numbers)
    else:
        delimiter = ','
    
    num_list = split_numbers(numbers, delimiter)
    return sum_valid_numbers(num_list)


def parse_custom_delimiter(numbers: str) -> tuple:
    delimiter, numbers = numbers[2:].split('\n', 1)
    return delimiter, numbers


def split_numbers(numbers: str, delimiter: str) -> list:
    return numbers.replace('\n', delimiter).split(delimiter)


def sum_valid_numbers(num_list: list) -> int:
    def is_valid(num):
        return num.isdigit() and int(num) <= 1000
    
    return sum(int(num) for num in num_list if is_valid(num))

