import random
import string


def password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


def email():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6)) + '@ya.ru'


def name():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))