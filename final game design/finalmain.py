import pygame as p
import sys, time

#controls the fps of the code
clock = p.time.Clock()

from pygame.locals import * #imports important p module

#initiates p
p.init()

#variable for window size
windowSize = (400,400)

#labels the window
p.display.set_caption('My final project')

screen = p.display.set_mode(windowSize, 0, 32) #initiates the window

playerImage = p.image.load('playerr2.png')

moving_right = False
moving_left = False
 
player_location = [50,50]
player_y_momentum = 0
 
player_rect = p.Rect(player_location[0],player_location[1],playerImage.get_width(),playerImage.get_height())
test_rect = p.Rect(100,100,100,50)
 
while True: # game loop
    screen.fill((146,244,255)) # clear screen by filling it with blue
 
    screen.blit(playerImage,player_location) # render player
 
    # bouncy stoff
    if player_location[1] > windowSize[1]-playerImage.get_height():
        player_y_momentum = -player_y_momentum
    else:
        player_y_momentum += 0.2
    player_location[1] += player_y_momentum
    
    # movement
    if moving_right == True:
        player_location[0] += 4
    if moving_left == True:
        player_location[0] -= 4
 
    player_rect.x = player_location[0] # update rect x
    player_rect.y = player_location[1] # update rect y
 
    # test rect for collisions
    if player_rect.colliderect(test_rect):
        p.draw.rect(screen,(255,0,0),test_rect)
    else:
        p.draw.rect(screen,(0,0,0),test_rect)
    
    for event in p.event.get(): # event loop
        if event.type == QUIT: # check for window quit
            p.quit() # stop p
            sys.exit() # stop script
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
 
    p.display.update() # update display
    clock.tick(60) # maintain 60 fps