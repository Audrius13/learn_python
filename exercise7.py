import random

# Generate random list
lst = [random.randint(0, 101) for item in range(20)]

# Main function
def create_lst(lst):
    new_lst = [item for item in lst if item % 2 ==0]
    return new_lst

print(create_lst(lst))