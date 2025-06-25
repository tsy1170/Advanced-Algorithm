import random

def generate_random_numbers():
    numbers = []
    for i in range(100):
        numbers.append(random.randint(0, 10000))
    return numbers

number = generate_random_numbers()
print(number)