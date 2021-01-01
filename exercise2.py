# Ask user input
try:
    num = int(input('Please enter a number: '))
    check = int(input('Please enter second number: '))
except ValueError:
    print('Please enter a valid integer numbers')

# Define functions to check against numbers
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def is_multiply_4(num):
    if (num % 2 == 0) and (num % 4 == 0):
        return True
    else:
        return False

def devides_evenly(num, check):
    if num % check == 0:
        return True
    else:
        return False

# Logic to check 
if is_even(num):
    print('First function return that number is even')
else:
    print('First function return thar number is odd')

if is_multiply_4(num):
    print('Second function return that number is multiply by 4')
else:
    print('Second function return that number is not multiply by 4')

if devides_evenly(num, check):
    print('Third function returns that number is even devisible by check num')
else:
    print('Third function returns that number is not even devisible by check num')