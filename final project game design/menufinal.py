import os, random, time, math, datetime, sys
import pygame 
from turtle import title, tiltangle
from decimal import ROUND_UP

os.system('clear')
name=input("What is your name? ")
from pygame.locals import * #imports important modules required to help run game
#initialize p
pygame.init()

#Declare constants, variables, list, dictionaries, any object
#scree size
WIDTH=1000
BACKCLR=False
HEIGHT=1000
xMs=50
yMs=250
wb=30
hb=30

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
background= colors.get('navy')
randColor=''
screen_width = 1000
screen_height = 1000
sqM_color=colors.get('pink')

#creates the window
screen = pygame.display.set_mode((screen_width, screen_height))
#sets the title for the window
pygame.display.set_caption('Final Project Game')

#game variables
tile_size = 50

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
            print(randColor)
            print(background)
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
    print(date.strftime('%m/%d/%Y'))
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
        print(i,stuff[i])
        # temp[i]=stuff
        temp[j]=stuff[i]
        j +=1
    for t in range(5):
        text=INST_FNT.render(stuff[i], 1, BLACK)
        screen.blit(text, (40,yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi+=50
    
def keepScore(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine='\n'+str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
 
    #open a file and write in it 
    # when y write it erases the prev 
    myFile=open('ClassStuff\CircleEatsSquare\sce.txt','a') 
    myFile.write(scoreLine)
    myFile.close()

def playGame():
    clock = pygame.time.Clock()
    fps = 60

    screen_width = 1000
    screen_height = 1000

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Platformer')

    #define game variables
    tile_size = 50
    game_over = 0  


    #load images
    sun_pic = pygame.image.load('images/sun1.png')
    bg_pic = pygame.image.load('images/sky.png')

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
                if key[pygame.K_SPACE] and self.jumped == False:
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

    run = True
    while run:
        clock.tick(fps)

        screen.blit(bg_pic, (0, 0))
        screen.blit(sun_pic, (100, 100))

        world.draw()

        if game_over == 0:
        
            knight_group.update()
            
        water_group.draw(screen)

        knight_group.draw(screen)

        game_over = player.update(game_over)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()





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
print(mouse_pos)
MAX=10
jumpCount=10
JUMP=False
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
    if screenNumber == 20:
        TitleMenu('Settings')
        MainMenu(SettingList)
    if screenNumber == 30:
        playGame()
    if keys[pygame.K_ESCAPE]:
        screenNumber = 100
    if screenNumber == 40:
        TitleMenu('Scoreboard')
    if screenNumber == 50:
        pygame.display.quit()
        pygame.quit() # stop p
        sys.exit()
    if screenNumber == 20 and not BACKCLR:
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