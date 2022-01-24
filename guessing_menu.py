#Iyad K Mohammed
#Homework for 1/23/22
import os

import random

os.system('clear')

print("#############################")

print("#   Guess a number Menu     #")

def menu():
    print("[1] Choices 1-10")
    print("[2] Choices 1-50")
    print("[3] Choices 1-100")

menu()
option = int(input("Enter your option: "))

while option !=0:
    if option == 1:
        #start guessing game from 1-10
        guess = random.randint(1,10)
        user_guess = input("guess a number between 1-10 ")
        user_guess=int(user_guess)
        if guess == user_guess:
            print("Well done you guessed right")
        else:
            if guess != user_guess:
                print("Wrong guess try again later")
    elif option == 2:
        #start guessing game from 1-50
        guess = random.randint(1,50)
        user_guess = input("guess a number between 1-50")
        user_guess=int(user_guess)
        if guess == user_guess:
            print("Well done you guessed right")
        else:
            if guess != user_guess:
                print("Wrong, please try again")
    elif option == 3:
        #start guessing game from 1-100
        guess = random.randint(1,100)
        user_guess = input("guess a number between 1-100")
        user_guess=int(user_guess)
        if guess == user_guess:
            print("Well done you guessed right")
        else: 
            if guess != user_guess:
                print("Wrong, please try again")
