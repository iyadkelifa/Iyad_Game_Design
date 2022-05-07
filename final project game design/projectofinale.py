import pygame as p 
from sys import exit
from pygame.locals import * #imports important modules required to help run game

p.init()

#gives values for screen width and screen height
screen_width = 1000
screen_height = 1000

#creates the window
screen = p.display.set_mode((screen_width, screen_height))
#sets the title for the window
p.display.set_caption('Final Project Game')

#load neccesary images
sun_pic = p.image.load('images/sun1.png')

#makes it so that the game only ends when the boolean variable is false
run = True
while run:
    screen.blit(sun_pic, (100,100)) 
    for event in p.event.get():#cycles through all events
        if event.type == p.quit: #when you click on the x button game closes
            p.quit()
            exit()
    p.display.update()#updates the display window with instructions


p.quit()#finalises and closes it all out
