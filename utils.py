def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def prime(n):
    if n <= 1:
        return 'Число не просте'
    if n <= 3:
        return 'Число просте'
    if n % 2 == 0 or n % 3 == 0:
        return 'Число не просте'
    return 'Число просте'


def stepin5(n):
    while n > 1:
        if n % 5 != 0:
            return 'Число не є степенем 5'
        n /= 5
    return 'Число є степенем 5'
