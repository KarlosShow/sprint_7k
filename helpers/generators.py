import random
import string

def random_lower_string(length: int = 10): # генерация случсйно строки
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))