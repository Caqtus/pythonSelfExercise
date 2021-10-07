def oddoreven():
    myNumber = int(input('enter number and I will tel you if its odd or even'))


    if (myNumber % 2 == 0):
         print('Your number is even')
         print(f'{myNumber} % 2 - remainder is {myNumber%2}')
    else:
        print('Your number is odd')
        print(f'{myNumber} % 2 - remainder is {myNumber % 2}')


