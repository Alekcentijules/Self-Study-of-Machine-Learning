def devisor(num_div_del: int) -> list:
    if num_div_del == 0:
        raise ZeroDivisionError("Error: You cannot division by zero!")
    numbers = list(range(1, 101))
    filtered_numbers = [num for num in numbers if num % num_div_del != 0]
    return filtered_numbers

try:
    user_input = int(input("Enter a positive number: "))
    if user_input <= 0:
        raise ValueError("Error: Please enter a positive number greater than zero!")
    result = devisor(user_input)
    print(f"Filtered list (1-100): {result}")
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)




