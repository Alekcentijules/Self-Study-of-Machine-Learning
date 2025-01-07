def vowel_count(text) -> str:
    count = 0
    text.lower()
    for word in text:
        if word in ("aeiouy"):
            count += 1
    return count

user_input = input("Enter a text: ")
result = vowel_count(user_input)

print(result)

