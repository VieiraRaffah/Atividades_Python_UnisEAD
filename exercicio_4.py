import math

def primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(numero)) + 1, 2):
        if numero % i == 0:
            return False
    return True

for num in range(1, 101):
    if primo(num):
        print(f'O número {num} é um número primo.')
    else:
        print(f'O número {num} não é um número primo.')