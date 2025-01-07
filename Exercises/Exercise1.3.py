def summ(a, b: float) -> float:
    return a + b

user_input_1 = float(input("Enter the first number: "))
user_input_2 = float(input("Enter the second number: "))
result = round(summ(user_input_1, user_input_2), 5)

print(f"Sum of {user_input_1} and {user_input_2} = {result}")










