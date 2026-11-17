import random
import string

def generate_email():
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"test_{suffix}@yandex.ru"

def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def generate_name():
    return f"User_{''.join(random.choices(string.ascii_uppercase, k=5))}"