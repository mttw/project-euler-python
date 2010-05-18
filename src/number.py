import math


def lsqrt(number):
    return int(math.sqrt(number))


def is_palindrome(number):
    return str(number) == str(number)[::-1]