from turtle import tiltangle
import pygame as p 
import sys, time, os
os.system('clear')
from pygame.locals import * #imports important modules required to help run game

p.init()

#gives values for screen width and screen height
screen_width = 1000
screen_height = 1000

#creates the window
screen = p.display.set_mode((screen_width, screen_height))
#sets the title for the window
p.display.set_caption('Final Project Game')

#game variables
tile_size = 50
game_over = 0

#load neccesary images
sun_pic = p.image.load('images/sun1.png')
bg_pic = p.image.load('images/sky.png') 
sun_pic = p.transform.scale(sun_pic, (150, 150))


class World():
    def __init__(self, data):
        self.tile_list = []
        #load images
        dirt_pic = p.image.load('images/dirt.png')
        grass_pic = p.image.load('images/grass.png')

        #allows the computer to know what to do each row if 1 or 0
        row_count = 0 #helps us determine where on the screen the tile goes
        for row in data:
            column_count = 0
            for tile in row: 
                if tile == 1:
                    img = p.transform.scale(dirt_pic, (tile_size, tile_size)) #makes sure the dirt image's size will fit the tile
                    img_rect = img.get_rect() #we call a rectangle for the dirt image to store the info on coordinates helping us with collisions
                    #give it an x and y coordinate to know where it wil show on the window based on where it is on the grid
                    img_rect.x = column_count * tile_size #moves a tile by column
                    img_rect.y = row_count * tile_size #moves a tile by row
                    tile = (img, img_rect)
                    self.tile_list.append(tile) #append function allows me to add items to the list
                if tile == 2:
                    img = p.transform.scale(grass_pic, (tile_size, tile_size)) #makes sure the dirt image's size will fit the tile
                    img_rect = img.get_rect() #we call a rectangle for the dirt image to store the info on coordinates helping us with collisions
                    #give it an x and y coordinate to know where it wil show on the window based on where it is on the grid
                    img_rect.x = column_count * tile_size #moves a tile by column
                    img_rect.y = row_count * tile_size #moves a tile by row
                    tile = (img, img_rect)
                    self.tile_list.append(tile) #append function allows me to add items to the list
                column_count += 1
            row_count += 1
    
    #allows the init function to be drawn on screen
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])#it will take the image and put it in the rect coordinates

class Player():
    def __init__(self, x, y):
        img = p.image.load('images/guy1.png')#load in our character sprite
        self.image = p.transform.scale(img, (90, 90))#scales images to the right size
        self.rect  = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y #creates player

    def update(self): 
        dx = 0
        dy = 0
        #gets keys functions
        key = p.key.get_pressed()
        if key[p.K_LEFT]:
            dx -= 5
        if key[p.K_RIGHT]:
            dx += 5
        if key[p.K_SPACE]:
            dy += 5
        #calculate  new player position
        #check collision at the poistion
        #adjust player position
        self.rect.x += dx
        self.rect.y += dy

        #draws player
        screen.blit(self.image, self.rect)

#list
world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1], 
[1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1], 
[1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

#create an instance of the previous code
player = Player(100, screen_height - 130 )
world = World(world_data)

#creates a function to make a grid for the window
def draw_grid():
	for line in range(0, 20):
		p.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		p.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))




while True: 
    for event in p.event.get(): # event loop

        screen.blit(bg_pic, (0, 0))
        screen.blit(sun_pic, (0, 0))

        world.draw()
        player.update()
        #makes it so that the game only ends when the boolean variable is false
        if event.type == QUIT: # check for window quit
            p.display.quit()
            p.quit() # stop p
            sys.exit()#stops script
    p.display.update()#updates the display window with instructions


