import random

guess = 0

while True:
    num = input('Please enter number between 1 and 9: ')
    ran_num = random.randint(1, 10)
    if num == 'exit':
        print('you played {} times'.format(guess))
        break
    else:
        print('Please enter integer between 1 and 9')
    try:
        if int(num) == ran_num:
            print('You guessed it !')
        elif int(num) > ran_num:
            print('Your number is to high')
        else:
            print('Your guess is to low')
        guess += 1
    except ValueError:
        print('Please enter valid integer')