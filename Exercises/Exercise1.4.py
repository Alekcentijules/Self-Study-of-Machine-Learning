import random

def del_num_div(num_div_del: int) -> list:
    # new_lst = []
    # for num in random.randint[]:
    #     if not num.isdigit():
    #         print(f"Error: {num} - it's not a digit!")
    #         break
    #     elif not num // num_div_del:
    #         new_lst.append(num)
    # return new_lst
    if num_div_del == 0:
        raise ZeroDivisionError("Error: you cannot division by zero!")
    return [random.randint(1, 100) for i in range(random.randint(1, 100)) if not i // num_div_del]


try:
    user_input = int(input("Enter a number: "))
    result = del_num_div(user_input)
    print(f"Your list: {result}")
except ZeroDivisionError as err:
    print(err)





