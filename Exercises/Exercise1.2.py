def vowel_count(text: str) -> int:
    count = 0
    text = text.lower()
    vowels = set("aeiouy")
    for char in text:
        if char in vowels:
            count += 1
    return count

user_input = input("Enter a text: ")
result = vowel_count(user_input)

print(f"Number of vowels: {result}")

