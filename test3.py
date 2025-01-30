row = input("Введи текст: ")
letters = {}

for letter in row:
    if letter.isalpha():
        if letter.lower() in letters:
            letters[letter.lower()] += 1
        else:
            letters[letter.lower()] = 1

for key, value in letters.items():
    print(f"{key}: {value}")