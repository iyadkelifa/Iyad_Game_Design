#Iyad K Mohammed
#Homework for 1/23/22
import os
import random
os.system('clear')
gameOn=True

print("#############################")

print("#   Guess a number Menu     #")

print("#############################")

def menu():
    print("[1] Choices 1-10")
    print("[2] Choices 1-50")
    print("[3] Choices 1-100")

menu()
option = int(input("Enter your option: "))

#adds counter system for gameover
counter=0
while gameOn:
    #allows user to access menu by writing numbers 1-3
    while option !=0:
        if option == 1:
            #start guessing game from 1-10
            guess = random.randint(1,10)
            #user inputs a number between 1-10
            user_guess = input("guess a number between 1-10 ")
            #classify the data type
            user_guess=int(user_guess)
            #give hints to the user to make the game easier
            if user_guess>guess:
                print("you were too far")
            else:
                if user_guess<guess:
                    print("You were too low")
            counter = counter + 1
            #if user guesses the right number
            if guess == user_guess:
                print("Well done you guessed right")
                gameOn=False
            else:
                #if user guesses wrong
                if guess != user_guess:
                    print("Wrong guess try again later")
        elif option == 2:
            #start guessing game from 1-50
            guess = random.randint(1,50)
            #user inputs a number between 1-50
            user_guess = input("guess a number between 1-50")
            #classify the data type
            user_guess=int(user_guess)
            #give hints to the user to make the game easier
            if user_guess>guess:
                print("you were too far")
            else:
                if user_guess<guess:
                    print("You were too low")
            counter = counter + 1
            #if user guesses the right number
            if guess == user_guess:
                print("Well done you guessed right")
                gameOn=False
            else:
                if guess != user_guess:
                    print("Wrong, please try again")
        elif option == 3:
            #start guessing game from 1-100
            guess = random.randint(1,100)
            #user inputs a number between 1-100
            user_guess = input("guess a number between 1-100")
            #classify the data type
            user_guess=int(user_guess)
            #give hints to the user to make the game easier
            if user_guess>guess:
                print("you were too far")
            else:
                if user_guess<guess:
                    print("You were too low")
            counter = counter + 1
            #if user guesses the right number
            if guess == user_guess:
                print("Well done you guessed right")
                gameOn=False
            else: 
                if guess != user_guess:
                    print("Wrong, please try again")
        if counter == 5:
            print("Game Over :(")