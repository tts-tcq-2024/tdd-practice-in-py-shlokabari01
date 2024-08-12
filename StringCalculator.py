#global variable
Upper_limit = 1000;

def add(numbers):

    # If the input string is empty, return 0
    if not numbers:
        return 0
    #default delimiter
    delimiter = ';'

    # Check the starting delimiter
    if numbers.startswith('//'):
        delimiter, numbers = Eliminating_Delimiter(numbers)

    # Separating the numbers
    List_of_Numbers = Separate_Numbers(numbers, delimiter)
    
    #Check for upper limit of numbers
    List_of_Numbers = Check_Numbers_Upper_Limit(List_of_Numbers)

    # Check for negative numbers
    Check_Negative_Numbers(List_of_Numbers)

    # Calculate and return the sum of the numbers
    Sum_of_numbersList = sum(List_of_Numbers)
    
    return Sum_of_numbersList


def Eliminating_Delimiter(numbers):

    # Extract the delimiter and remove it from the numbers string
    delimiter, numbers = numbers.split('\n', 1)
    delimiter = delimiter[2:]  # Ignore the initial '//' characters
    return delimiter, numbers


def Separate_Numbers(numbers, delimiter):

    # Replace newline characters with the delimiter and split the string
    numbers = numbers.replace('\n', delimiter)
    Numbers_separated = list(map(int, numbers.split(delimiter)))
    
    return Numbers_separated


def Check_Negative_Numbers(numbers_list):

    # Check for negative numbers
    negative_numbers = [num for num in numbers_list if num < 0]
    ErrorMessage(negative_numbers)
    return negative_numbers

def Check_Numbers_Upper_Limit (numbers_list):
    
    # Check for the upper limit of numbers
    upper_limit_of_numbers = [num for num in numbers_list if num <= Upper_limit]
    return upper_limit_of_numbers 

def ErrorMessage(negative_numbers):
    #Error message for negative numbers
    if negative_numbers:
        raise ValueError(f"Negatives not allowed: {', '.join(map(str, negative_numbers))}")
