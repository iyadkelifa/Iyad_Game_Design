import os, random, time, math, datetime, sys, pickle
import pygame 
from turtle import title, tiltangle
from decimal import ROUND_UP
from tkinter import W
from pygame.locals import *
from os import path
from pygame import mixer

os.system('clear')
name=input("What is your name? ")
from pygame.locals import * #imports important modules required to help run game
#initialize p
pygame.init()

#Declare constants, variables, list, dictionaries, any object
#scree size
WIDTH=750
BACKCLR=False
HEIGHT=750
xMs=50
yMs=250
wb=30
hb=30
score = 0
MAIN=True
INSTR=False
SETT=False
BACKCLR=False
CRCLR=False
SIZE=False
LEV_1=False
LEV_2=False
LEV_3=False
PSCORE1=False
SCOREBOARD=False
EXIT=False

#gives values for screen width and screen height

screenNumber = 100

clock = pygame.time.Clock()
fps = 60 


#List f messages
MenuList=['Instructions','Settings', "Play Game" ,'Scoreboard','Exit']
SettingList=['Screen Size','Background Color']
check=True #for the while loop

clock=pygame.time.Clock()

#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}
#Get colors
BackColorList=['aqua',"purple", "white", "orange"]
CrClrList=['red', "navy", "pink", "white"]
SizeList=['800x800', '1000x1000', 'Original']
background= colors.get('navy')
randColor=''
sqM_color=colors.get('pink')
white = (255, 255, 255)

#creates the window
screen = pygame.display.set_mode((HEIGHT, WIDTH))
#sets the title for the window
pygame.display.set_caption('Final Project Game')

#game variables
tile_size = HEIGHT/20

#load neccesary images
sun_pic = pygame.image.load('images/sun1.png')
bg_pic = pygame.image.load('images/sky.png')
bg_pic = pygame.transform.scale(bg_pic, (WIDTH, HEIGHT)) 
sun_pic = pygame.transform.scale(sun_pic, (150, 150))

BLACK=(0,0,0)
#create fifferent type 
TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 30)
#Create square fr menu

squareM=pygame.Rect(xMs,yMs,wb,hb)
#Create Title
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
def TitleMenu(Message):
    text=TITLE_FNT.render(Message, 1, (255,0,0))
    screen.fill((255,255,255))
    #get the width  the text 
    #x value = WIDTH/2 - wText/2
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text,(xt,50))
#This is a function uses a parameter
def MainMenu(Mlist):
    txty=243
    squareM.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,(51,131,51))
        screen.blit(text,(90,txty))
        pygame.draw.rect(screen,sqM_color, squareM )
        squareM.y +=50
        txty+=50
    pygame.display.update()
    pygame.time.delay(10)

def changeColor():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        if colors.get(randColor)==background:
            # print(randColor)
            # print(background)
            randColor=random.choice(list(colors))
        else:
            colorCheck=False
def instr():  
    txt=INST_FNT.render("Move the player with the arrow keys", 1,(5, 31, 64))
    screen.blit(txt,(90,200))
    txt=INST_FNT.render("Jump by pressing the space button", 1, (5, 31, 64))
    screen.blit(txt,(90,240))
    txt=INST_FNT.render("Avoid enemies and acid",1, (5, 31, 64))
    screen.blit(txt, (90,280))
    txt=INST_FNT.render("Finish all 3 levels get to the diaomond",1, (5, 31, 64))
    screen.blit(txt, (90,320))
    txt=INST_FNT.render("And try to do it as fast as you can",1, (5, 31, 64))
    screen.blit(txt, (90,360))
    pygame.display.update()
    
def keepScore(score):
    date=datetime.datetime.now()
    # print(date.strftime('%m/%d/%Y'))
    scoreLine=str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
 
    #open a file and write in it 
    # when y write it erases the prev 
    myFile=open('ClassStuff\sce.txt','a') 
    myFile.write(scoreLine)
    myFile.close()

def scoreBoard():
    myFile=open('ClassStuff\CircleEatsSquare\sce.txt', 'r')
    yi=150
    stuff= myFile.readlines()
    myFile.close()
    stuff.sort()
    N=len(stuff)-1
    temp=[]
    j=0
    for i in range(N, -1, -1):
        # print(i,stuff[i])
        # temp[i]=stuff
        temp[j]=stuff[i]
        j +=1
    for t in range(5):
        text=INST_FNT.render(stuff[i], 1, BLACK)
        screen.blit(text, (40,yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi+=50
def screensizeChange():
    global HEIGHT, WIDTH, screen
    if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290)):
        HEIGHT=800
        WIDTH=800
        print('here!')

    if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340)):
        HEIGHT=1000
        WIDTH=1000
        
    if ((mouse_pos[0] >0 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <390)):
        HEIGHT=700
        WIDTH=700
    screen=pygame.display.set_mode((WIDTH,HEIGHT))

    






#sq_color=colors.get('navy')
#Making a rand c f the square
changeColor()

#==============================================
#
#Beginning  main prram
sq_color=colors.get(randColor)
keys=pygame.key.get_pressed()
mouse_pos=(0,0)
screCk=True
first=True
# print(mouse_pos)
MAX=10
jumpCount=10
JUMP=False
flat=False


while check:
    if BACKCLR:
        if ((mouse_pos[0] >306 and mouse_pos[0] <393) and (mouse_pos[1] >560 and mouse_pos[1] <595)):
            screenNumber == 100
            mouse_pos(0, 0)
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290)):
            background=colors.get('aqua')  
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340)):
            background=colors.get('purple')    
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <390)):
            background=colors.get('yellow')
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <440)):
            background=colors.get('orange')
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
        if case.type ==pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            xm= mouse_pos[0]
            ym= mouse_pos[1]
        # print(mouse_pos)
    keys=pygame.key.get_pressed() #this returns a list
    if keys[pygame.K_ESCAPE]:
        screenNumber = 100
    if screenNumber == 100:
        TitleMenu('Main Menu')
        MainMenu(MenuList)
    if screenNumber == 10:
        TitleMenu('Instructions')
        instr()
    if screenNumber == 20 and flat == False:
        TitleMenu('Settings')
        MainMenu(SettingList)
    if screenNumber == 30:
        pygame.mixer.pre_init(44100, -16, 2, 512)
        mixer.init()
        pygame.init()


        clock = pygame.time.Clock()
        fps = 60

        screen_width = 700
        screen_height = 700

        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Platformer')

        #define the font
        font = pygame.font.SysFont('Bauhaus 93', 70)
        font_score = pygame.font.SysFont('Bahaus 93', 30)

        #define game variables
        tile_size = screen_height/20
        game_over = 0  
        main_menu = True
        level = 1
        max_levels = 6
        score = 0

        #define colors
        white = (255, 255, 255)
        blue = (0, 0, 255)

        #load images
        sun_pic = pygame.image.load('images/sun1.png')
        bg_pic = pygame.image.load('images/sky.png')
        restart_img = pygame.image.load('images/restart_btn.png')
        start_img = pygame.image.load('images/start_btn.png')
        exit_img = pygame.image.load('images/exit_btn.png')

        #load sounds
        pygame.mixer.music.load('images/music.wav')
        pygame.mixer.music.play(-1, 0.0, 5000)
        coin_sfx = pygame.mixer.Sound('images/coin.wav.wav')
        coin_sfx.set_volume(0.5)
        jump_sfx = pygame.mixer.Sound('images/jump.wav.wav')
        jump_sfx.set_volume(0.5)
        game_over_sfx = pygame.mixer.Sound('images/game_over.wav.wav')
        game_over_sfx.set_volume(0.5)


        knight_group = pygame.sprite.Group()
        platform_group = pygame.sprite.Group()
        water_group = pygame.sprite.Group()
        coin_group = pygame.sprite.Group()
        exit_group = pygame.sprite.Group()

    
        def draw_text(text, font, text_col, x, y):
            img = font.render(text, True, text_col)
            screen.blit(img, (x, y))



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
                self.reset(x, y)

            def update(self, game_over):
                dx = 0
                dy = 0
                walk_cooldown = 5
                col_thresh = 20

                if game_over == 0:
                    #get keypresses
                    key = pygame.key.get_pressed()
                    if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
                        jump_sfx.play()
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
                    self.in_air = True
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
                        game_over_sfx.play()

                    #check for collision with lava
                    if pygame.sprite.spritecollide(self, water_group, False):
                        game_over = -1
                        game_over_sfx.play()

                    #check for collision with exit
                    if pygame.sprite.spritecollide(self, exit_group, False):
                        game_over = 1


                    #check for collision with platforms
                    for platform in platform_group:
                        #collision in the x direction
                        if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                            dx = 0
                        #collision in the y direction
                        if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                            #check if below platform
                            if abs((self.rect.top + dy) - platform.rect.bottom) < col_thresh:
                                self.vel_y = 0
                                dy = platform.rect.bottom - self.rect.top
                            #check if above platform
                            elif abs((self.rect.bottom + dy) - platform.rect.top) < col_thresh:
                                self.rect.bottom = platform.rect.top - 1
                                self.in_air = False
                                dy = 0
                            #move sideways with the platform
                            if platform.move_x != 0:
                                self.rect.x += platform.move_direction


                    #update player coordinates
                    self.rect.x += dx
                    self.rect.y += dy


                elif game_over == -1:
                    self.image = self.dead_image
                    draw_text('GAME OVER!', font, blue, (screen_width // 2) - 200, screen_height // 2)
                    if self.rect.y > 200:
                        self.rect.y -= 5
                    file=open("score.txt","a")
                    file.write(str(score)+","+name+"\n")
                    file.close()
                    
                    file = open("score.txt", "r")
                    readthefile = file.readlines()
                    sortedData = sorted(readthefile,reverse=True)

                    # print("Top 3 Scores")
                    # print("Pos\tPoints, Name")
                    
                    # for line in range(3):
                    #     print(str(line+1)+"\t"+str(sortedData[line]))
                    if screenNumber == 40:
                        TitleMenu('Scoreboard')
                        # print('joe mama')

                #draw player onto screen
                screen.blit(self.image, self.rect)

                return game_over


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
                self.dead_image = pygame.image.load('images/ghost1.png')
                self.image = self.images_right[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.width = self.image.get_width()
                self.height = self.image.get_height()
                self.vel_y = 0
                self.jumped = False
                self.direction = 0
                self.in_air = True

                



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
                        if tile == 4:
                            platform = Platform(col_count * tile_size, row_count * tile_size, 1, 0)
                            platform_group.add(platform)
                        if tile == 5:
                            platform = Platform(col_count * tile_size, row_count * tile_size,0 ,1)
                            platform_group.add(platform)
                        if tile == 6:
                            water = Water(col_count * tile_size, row_count * tile_size + (tile_size // 2))
                            water_group.add(water)
                        if tile == 7:
                            coin = Coin(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
                            coin_group.add(coin)
                        if tile == 8:
                            exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size // 2))
                            exit_group.add(exit)
                        col_count += 1
                    row_count += 1
            def draw(self):
                for tile in self.tile_list:
                    screen.blit(tile[0], tile[1])


        def reset_level(level):
                player.reset(100, screen_height - 130)
                knight_group.empty()
                water_group.empty()
                exit_group.empty()
                platform_group.empty()


                if path.exists(f'level{level}_data'):
                    pickle_in = open(f'level{level}_data', 'rb')
                    world_data = pickle.load(pickle_in)
                world = World(world_data)

                return world


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

        class Platform(pygame.sprite.Sprite):
            def __init__(self, x, y, move_x, move_y):
                pygame.sprite.Sprite.__init__(self)
                img = pygame.image.load('images/platform.png')
                self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.move_counter = 0
                self.move_direction = 1
                self.move_x = move_x
                self.move_y = move_y


            def update(self):
                self.rect.x += self.move_direction * self.move_x
                self.rect.y += self.move_direction * self.move_y
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
                self.rect = self.image.get_rect()
                self.rect.center = (x, y)

        class Coin(pygame.sprite.Sprite):
            def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                img = pygame.image.load('images/coin.png')
                self.image = pygame.transform.scale(img, (tile_size // 2, tile_size // 2))
                self.rect = self.image.get_rect()
                self.rect.center = (x, y)


        class Exit(pygame.sprite.Sprite):
            def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                img = pygame.image.load('images/exit.png')
                self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y





        player = Player(100, screen_height - 130)
        knight_group = pygame.sprite.Group()
        platform_group = pygame.sprite.Group()
        water_group = pygame.sprite.Group()
        coin_group = pygame.sprite.Group()
        exit_group = pygame.sprite.Group()

        #dummy coin for the score counter
        score_coin = Coin(tile_size // 2, tile_size // 2)
        coin_group.add(score_coin)

        #load world data
        if path.exists(f'level{level}_data'):
            pickle_in = open(f'level{level}_data', 'rb')
            world_data = pickle.load(pickle_in)
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

            if level == 4:
                    bg_pic = pygame.image.load('images/hell.png')
                    bg_pic = pygame.transform.scale(bg_pic, (WIDTH, HEIGHT)) 
                    dirt_img = pygame.image.load('images/magma.png')
                    dirt_img = pygame.transform.scale(dirt_img, (21, 21)) 
                    grass_img = pygame.image.load('images/stone.png')
                    grass_img = pygame.transform.scale(grass_img, (21, 21))

            else:

                world.draw()

                

                #if player is alive updates the knights to move
                if game_over == 0:
                    knight_group.update()
                    platform_group.update()
                    #updates score and check if coins are collected
                    if pygame.sprite.spritecollide(player, coin_group, True):
                        score += 1
                        coin_sfx.play()
                    draw_text('X ' + str(score), font_score, white, tile_size - 10, 10)
                    
                

                #draws the entities on the screen    
                water_group.draw(screen)
                platform_group.draw(screen)
                coin_group.draw(screen)
                knight_group.draw(screen)
                exit_group.draw(screen)

        



                game_over = player.update(game_over)

                #if player has died
                if game_over == -1:
                    if restart_button.draw():
                        world_data = []
                        world = reset_level(level)
                        game_over = 0 #allows us to reset the game
                        score = 0
                        updateScores()
                #player completed level
                if game_over == 1:
                    #reset game and go to next level
                    level += 1
                    if level <= max_levels:
                        world_data = []
                        world = reset_level(level)
                        game_over = 0
                    else:
                        draw_text('Well done :0', font, blue, (screen_width // 2) - 140, screen_height //2)
                        if restart_button.draw():
                            level = 1
                            world_data = []
                            world = reset_level(level)
                            game_over = 0
                            score = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()
    def updateScores(): #Funvtion to update scores

        myScoreboard=open('score.txt','a')

        myScoreboard.write('Highscore: '+str(score))

        myScoreboard.close()

    def displayScoreboard():

        height = 170

        myScoreboard=open('score.txt','r') #opens the file
        print (len(myScoreboard.readlines()))
        for line in myScoreboard.readlines():   #Reads the file and prints each letter on the screen

            text = INST_FNT.render(line,1, (0, 0, 0))

            # print(line)

            screen.blit(text, (300, 300))

            

            pygame.display.update()

            pygame.time.delay(100)

            height+=60

        myScoreboard.close()
    if keys[pygame.K_ESCAPE]:
        screenNumber = 100
    if screenNumber == 40:
        TitleMenu('Scoreboard')
        displayScoreboard()
        
    if screenNumber == 50:
        pygame.display.quit()
        pygame.quit() # stop p
        sys.exit()
    if screenNumber == 20 and flat == True:
        if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <330)):
            TitleMenu('Background Colors')
            MainMenu(BackColorList)
            BACKCLR = True
        


    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290)):
        screenNumber = 10
        mouse_pos = (0, 0)
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <330)):
        screenNumber = 20
        mouse_pos = (0, 0)
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <380)):
        screenNumber = 30
        mouse_pos = (0, 0) 
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <430)):
        screenNumber = 40
        mouse_pos = (0, 0) 
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >450 and mouse_pos[1] <480)):
        screenNumber = 50
        mouse_pos = (0,0)   
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >500 and mouse_pos[1] <530)):
        screenNumber = 60
        mouse_pos = (0, 0)
        
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >550 and mouse_pos[1] <580)) :
        screen.fill(background)
        
        keepScore(121) 
        text=INST_FNT.render("Make sure you update the score file", 1, BLACK)
        screen.blit(text, (40,200))
        text=INST_FNT.render("before you exit", 1, BLACK)
        screen.blit(text, (40,300))
        text=INST_FNT.render("Thank you for playing", 1, BLACK)
        screen.blit(text, (40,400))
        pygame.display.update()
        pygame.time.delay(50)
        MAIN=False
        SCORE=False 
        pygame.time.delay(3000)
        check=False


    pygame.display.update()
    pygame.time.delay(10)
clock.tick(30)


os.system('clear')
pygame.quit()