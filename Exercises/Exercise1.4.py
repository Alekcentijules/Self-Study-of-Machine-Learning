import random

def del_num_div(num_div_del: int) -> list:
    if num_div_del == 0:
        raise ZeroDivisionError("Error: You cannot division by zero!")
    numbers = list(range(1, 101))
    filter_numbers = [num for num in numbers if num % num_div_del != 0]
    return filter_numbers

try:
    user_input = int(input("Enter a number: "))
    result = del_num_div(user_input)
    print(f"Your list: {result}")
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Error: Please enter a valid number.")




