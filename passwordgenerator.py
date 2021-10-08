import random


def generatePassword():
    pass_lengh = int(input(f'how long should password be? \n'.strip()))
    symbols = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'

    print(f'Here, take a pseudo-random passwords: \n ')
    for x in range(8):
        password_generated = ''.join(random.sample(symbols, pass_lengh))
        print(f'{x+1}.{password_generated}')



