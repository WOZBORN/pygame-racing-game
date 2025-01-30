import numbers as nums

num = int(input("Введите четное число: "))

if nums.is_even(num):
    print("Спасибо!")
else:
    print("Это не четное число :(")