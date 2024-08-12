def parse_input(input_string):
    if input_string.startswith('//'):
        delimiter = input_string[2]
        return input_string[4:], delimiter
    return input_string, ','
 
def split_and_convert(input_string, delimiter):
    return [int(num) for num in input_string.replace('\n', delimiter).split(delimiter)]
 
def filter_numbers(numbers):
    return [num for num in numbers if num <= 1000]
 
def add(input_string):
    if not input_string:
        return 0
    parsed_input, delimiter = parse_input(input_string)
    numbers = split_and_convert(parsed_input, delimiter)
    filtered_numbers = filter_numbers(numbers)
    return sum(filtered_numbers)
