from datetime import datetime

name = input("Введи ваше имя: ")
age = input("Введи ваш возраст: ")

while not age.isdigit():
    print("Введи корректное значение (целое число)!")
    age = input("Введи ваш возраст: ")

age = int(age)
birthday_passed = input("Был ли день рождения в этом году? (да/нет): ")

if birthday_passed == "да":
    print(f"Привет, {name} {datetime.now().year - age} года рождения!")
elif birthday_passed == "нет":
    print(f"Привет, {name} {datetime.now().year - age - 1} года рождения!")
else:
    print(f"Такого ответа я не ожидал о тебя, {name}...")