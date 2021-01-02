options = ['paper', 'rock', 'scissors']


def check_winer(x, y):
    if x == y:
        return "It's a draw"
    elif x == 'paper' and y == 'rock':
        return x
    elif x == 'paper' and y == 'scissors':
        return y
    elif x == 'rock' and y == 'paper':
        return y
    elif x == 'rock' and y == 'scissors':
        return x
    elif x == 'scissors' and y == 'paper':
        return x
    else:
        return y

while True:
    player1 = input('Please enter "Paper", "Rock" or "Scissors": ').strip()
    player2 = input('Please enter "Paper", "Rock" or "Scissors": ').strip()
    if player1.lower() in options and player2.lower() in options:
        if player1 and player2:
            print(check_winer(player1.lower(), player2.lower()))
            x = input('Do you want to play again? y/n: ').strip()
            if x.lower() == 'y':
                pass
            else:
                break
        else:
            print('Please enter "Paper", "Rock" or "Scissors"')
            x = input('Do you want to play again? y/n: ').title()
            if x.lower() == 'y':
                pass
            else:
                break
    else:
        print('Please chose "Paper", "Rock" or "Scissors"')