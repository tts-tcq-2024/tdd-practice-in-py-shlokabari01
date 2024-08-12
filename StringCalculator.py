Upper_limit = 1000 

def add_cnn2(numbers):  
    if not numbers:  
        return 0  
    
    delimiter = ';' 
    if numbers.startswith('//'):  
        delimiter, numbers = numbers[2:].split('\n', 1) 

    numbers_list = [int(num) for num in numbers.replace('\n', delimiter).split(delimiter) if int(num) <= Upper_limit]  

    negative_numbers = [num for num in numbers_list if num < 0]  
    if negative_numbers:  
        raise ValueError(f"Negatives not allowed: {', '.join(map(str, negative_numbers))}")  
    
    return sum(numbers_list) 
