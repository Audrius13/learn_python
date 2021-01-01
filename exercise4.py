# Ask user input

try:
    num = int(input('Please enter number: '))
except:
    print('Please input valid integer')

# Create a list of numbers 1 to 100

lst = list(range(1,101))

# Create main logic

def main_funct (num):
    new_lst = []
    if num > 0:
        for item in lst:
            if item % num == 0:
                new_lst.append(item)
        return new_lst
    else:
        return 'Number should be > 0'

print(main_funct(num))