import os
import random
rerun = True


def computer_result():
    # Revealing What The Computer Played
    if computer_play == 'R':
        print('I Played Rock')
    elif computer_play == 'S':
        print('I Played Scissors')
    elif computer_play == 'P':
        print('I Played Paper')


# INTRO:
def intro():
    print("Hi welcome to my rock paper scissors game! ")
    print("Now make a decision pick rock papers or scissors.")
intro()

while rerun:
    # R = Rock
    # S = Scissors
    # P = Paper

    # computer's decision
    computer_play = random.randint(1, 3)
    if computer_play == 1:
        computer_play = 'R'
    elif computer_play == 2:
        computer_play = 'S'
    elif computer_play == 3:
        computer_play = 'P'

    # user's decision
    user_play = int(input("Type 1 for rock, 2 for scissors, and 3 for paper."))
    if user_play == 1:
        user_play = 'R'
        print("So you've decided to play rock")
    elif user_play == 2:
        user_play = 'S'
        print("So you've chosen scissors")
    elif user_play == 3:
        user_play = 'P'
        print("Paper it is then")

    # same outcome
    if (user_play == 'R' and computer_play == 'R') or (user_play == 'P' and computer_play == 'P') \
            or (user_play == 'S' and computer_play == 'S'):
        computer_result()
        print('Stalemate...We Both Chose The Same Thing.')

    # User Wins
    if user_play == 'R' and computer_play == 'S':
        computer_result()
        print("Good game you have won")
    if user_play == 'P' and computer_play == 'R':
        computer_result()
        print("Good game you have won")
    if user_play == 'S' and computer_play == 'P':
        computer_result()
        print("Good game you have won")

    # Computer Wins
    if computer_play == 'R' and user_play == 'S':
        computer_result()
        print("HAHAHA I WIN :P")
    if computer_play == 'P' and user_play == 'R':
        computer_result()
        print("HAHAHA I WIN :P")
    if computer_play == 'S' and user_play == 'P':
        computer_result()
        print("HAHAHA I WIN :P")

    # asks if they want to replay
    replay = input('Want to play another game? Y/N: ')
    if replay == 'Y' or replay == 'y':
        continue
    else:
        rerun = False
        print('Thank You For Playing.')