from tkinter import W
import pygame
from pygame.locals import *

pygame.init()

def playGame():
    clock = pygame.time.Clock()
    fps = 60

    screen_width = 1000
    screen_height = 1000

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Platformer')

    #define game variables
    tile_size = 30
    game_over = 0  
    main_menu = True 


    #load images
    sun_pic = pygame.image.load('images/sun1.png')
    bg_pic = pygame.image.load('images/sky.png')
    restart_img = pygame.image.load('images/restart_btn.png')
    start_img = pygame.image.load('images/start_btn.png')
    exit_img = pygame.image.load('images/exit_btn.png')

    class Button():
        def __init__(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect() 
            self.rect.x = x
            self.rect.y = y
            self.clicked = False

        def draw(self):
            action = False

            #get mouse position
            pos = pygame.mouse.get_pos()

            #check mouseover and clicked conditions
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    action = True
                    self.clicked = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False


            #draw button
            screen.blit(self.image, self.rect)

            return action


    class Player():
        def __init__(self, x, y):
            self.images_right = []
            self.images_left = []
            self.index = 0
            self.counter = 0
            for num in range(1, 5):
                img_right = pygame.image.load(f'images/guy{num}.png')
                img_right = pygame.transform.scale(img_right, (40, 80))
                img_left = pygame.transform.flip(img_right, True, False)
                self.images_right.append(img_right)
                self.images_left.append(img_left)
            self.dead_image = pygame.image.load('images/ghost.png')
            self.dead_image = pygame.transform.scale(self.dead_image, (48, 49))

            self.image = self.images_right[self.index]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            self.vel_y = 0
            self.jumped = False
            self.direction = 0

        def update(self, game_over):
            dx = 0
            dy = 0
            walk_cooldown = 5

            if game_over == 0:
                #get keypresses
                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False: #prevents double jumping to make him jump if he's only on a block
                    self.vel_y = -15
                    self.jumped = True
                if key[pygame.K_SPACE] == False:
                    self.jumped = False
                if key[pygame.K_LEFT]:
                    dx -= 5
                    self.counter += 1
                    self.direction = -1
                if key[pygame.K_RIGHT]:
                    dx += 5
                    self.counter += 1
                    self.direction = 1
                if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                    self.counter = 0
                    self.index = 0
                    if self.direction == 1:
                        self.image = self.images_right[self.index]
                    if self.direction == -1:
                        self.image = self.images_left[self.index]


                #handle animation
                if self.counter > walk_cooldown:
                    self.counter = 0    
                    self.index += 1
                    if self.index >= len(self.images_right):
                        self.index = 0
                    if self.direction == 1:
                        self.image = self.images_right[self.index]
                    if self.direction == -1:
                        self.image = self.images_left[self.index]


                #add gravity
                self.vel_y += 1
                if self.vel_y > 10:
                    self.vel_y = 10
                dy += self.vel_y

                #check for collision
                self.in_air = True #checks if he's in air or in block
                for tile in world.tile_list:
                    #check for collision in x direction
                    if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                        dx = 0
                    #check for collision in y direction
                    if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                        #check if below the ground i.e. jumping
                        if self.vel_y < 0:
                            dy = tile[1].bottom - self.rect.top
                            self.vel_y = 0
                        #check if above the ground i.e. falling
                        elif self.vel_y >= 0:
                            dy = tile[1].top - self.rect.bottom
                            self.vel_y = 0
                            self.in_air = False

                #check for collision with enemies
                if pygame.sprite.spritecollide(self, knight_group, False):
                    game_over = -1

                #check for collision with water
                if pygame.sprite.spritecollide(self, water_group, False):
                    game_over = -1
                    print('game over')




                #update player coordinates
                self.rect.x += dx
                self.rect.y += dy
                dy = 0

            elif game_over == -1:
                self.image = self.dead_image
                if self.rect.y > 200:
                    self.rect.y -= 5

            #draw player onto screen
            screen.blit(self.image, self.rect)
            pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

            return game_over
        
        #reset function that allows to create the player from scratch
        def reset(self, x, y):
            self.images_right = []
            self.images_left = []
            self.index = 0
            self.counter = 0
            for num in range(1, 5):
                img_right = pygame.image.load(f'images/guy{num}.png')
                img_right = pygame.transform.scale(img_right, (40, 80))
                img_left = pygame.transform.flip(img_right, True, False)
                self.images_right.append(img_right)
                self.images_left.append(img_left)
            self.dead_image = pygame.image.load('images/ghost.png')
            self.dead_image = pygame.transform.scale(self.dead_image, (48, 49))
            self.image = self.images_right[self.index]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            self.vel_y = 0
            self.jumped = False
            self.direction = 0
            self.in_air = False
            



    class World():
        def __init__(self, data):
            self.tile_list = []

            #load images
            dirt_img = pygame.image.load('images/dirt.png')
            grass_img = pygame.image.load('images/grass.png')

            row_count = 0
            for row in data:
                col_count = 0
                for tile in row:
                    if tile == 1:
                        img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    if tile == 2:
                        img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    if tile == 3:
                        blob = Enemy(col_count * tile_size, row_count * tile_size - 8)
                        knight_group.add(blob)
                    if tile == 6:
                        water = Water(col_count * tile_size, row_count * tile_size + (tile_size // 2))
                        water_group.add(water)
                    col_count += 1
                row_count += 1
        def draw(self):
            for tile in self.tile_list:
                screen.blit(tile[0], tile[1])
                pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)



    class Enemy(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('images/blob1.png')
            self.image = pygame.transform.scale(self.image, (54, 60))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.move_direction = 1
            self.move_counter = 0
        
        def update(self):
            self.rect.x += self.move_direction
            self.move_counter += 1
            if abs(self.move_counter) > 50:
                self.move_direction *= -1
                self.move_counter *= -1 

    class Water(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('images/water.png')
            self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

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
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 2, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
    [1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1], 
    [1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]



    player = Player(100, screen_height - 130)
    knight_group = pygame.sprite.Group()
    water_group = pygame.sprite.Group()
    world = World(world_data)
    restart_button = Button(screen_width // 2 - 50, screen_height // 2 + 100, restart_img)
    start_button = Button(screen_width // 2 - 350, screen_height // 2, start_img)
    exit_button = Button(screen_width // 2 + 150, screen_height // 2, exit_img)

    run = True
    while run:
        #controls how fast the program runs
        clock.tick(fps)

        #imports images onto the screen
        screen.blit(bg_pic, (0, 0))
        screen.blit(sun_pic, (100, 100))

        if main_menu == True:
            if exit_button.draw():
                run = False
            if start_button.draw():
                main_menu = False


        else:

            world.draw()

            #if player is alive updates the knights to move
            if game_over == 0:
                knight_group.update()

            #draws the entities on the screen    
            water_group.draw(screen)

            knight_group.draw(screen)



            game_over = player.update(game_over)

            #if player has died
            if game_over == -1:
                if restart_button.draw():
                    player.reset(100, screen_height - 130)
                    game_over = 0 #allows us to reset the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

playGame()
pygame.quit()