mylist=['','O','']
from random import shuffle
def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=input("input:0,1, or 2")
    return int(guess)
def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)
shuffle(mylist)
guess=player_guess()
check_guess(mylist,guess)
