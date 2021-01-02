import random

# Generate two random len lists
list_a = [random.randint(0, 30) for item in range(random.randint(20, 30))]
list_b = [random.randint(0, 30) for item in range(random.randint(20, 30))]


# Main logic
def common_elements(x, y):
    new_lst = []
    if len(x) >= len(y):
        for item in x:
            if (item in y) and (item not in new_lst):
                new_lst.append(item)
    else:
        for item in y:
            if (item in x) and (item not in new_lst):
                new_lst.append(item) 
    return new_lst

print(list_a)
print(list_b)

print(common_elements(list_a, list_b))