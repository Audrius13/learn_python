import random

# Let's create list
try:
    lst_len = int(input('Enter number for list lenght: '))
    base_num = int(input('Enter base line number: '))
except ValueError:
    print('Please enter valid integer number')

lst = [random.randint(1, 100) for item in range(lst_len)]


# Create empty list and logic
new_lst = []

for item in lst:
    if item > base_num:
        new_lst.append(item)

# Print random generated list and new one
print(lst)
print(new_lst)