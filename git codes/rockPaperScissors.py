import random

def play():
    user = input("What's your choice? \n 'r' for rock, 'p' for paper and 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    

    if isWin(user, computer):
        return('You won') 
    else:
        if user == computer:
            print ('It\'s a tie')
            response = input('Do you want to play again?(y/n)')
            if response == 'y':
                return(play())
            else:
                quit(code='')
        else:
            print('You lose') 
            response = input('Do you want to play again?(y/n)')
            if response == 'y':
                return(play())
            else:
                quit(code='')
           

# r>s, s>p, p>r

def isWin(player, opponent):
    if (player == 'r' and opponent == 's') or (player =='s' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())

