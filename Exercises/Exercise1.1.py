def even_number(number: int) -> bool:
    return number % 2 == 0

user_input = int(input("Enter a number: "))
result = even_number(user_input)

print(f"Is the number even? {result}")
