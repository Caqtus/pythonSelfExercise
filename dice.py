from numpy import random


# When using this function, need to pass number
# It will generate Random number from 0 to "user input" range


def rolldice():
    diceCount = 100
    print(f'Roll (1-100): {random.random_integers(0, diceCount)}')
