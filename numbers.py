def is_prime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def is_even(num: int) -> bool:
    return num % 2 == 0


def is_odd(num: int) -> bool:
    return num % 2 == 1
