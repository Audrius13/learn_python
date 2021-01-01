from datetime import date

# Ask user input
try: 
    username = input('Please enter your name: ').strip()
    age = int(input('Please enter your age: '))
    times = int(input('Please enter times to repeat message: '))
except ValueError:
    print('age and times must be an integer')

today = date.today()
years = today.year

# Main logic
if username and age > 0 and times > 0:
    while times > 0:
        print('{} you will turn 100 at year {}'.format(username, years + 100 - age))
        times -= 1
elif age <= 0 or times <= 0:
    print('age and times must be > 0')
elif not username:
    print('Please input username')