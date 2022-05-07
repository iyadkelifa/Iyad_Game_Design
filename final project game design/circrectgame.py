#learning how to draw circles and rectangles
#use keys to move objects
#Using Dictionaries

#Objective of the game is for the rect to run away fom the circle, if they collide the circle etas the square, 
#circle will  get larger, and a new rect should appear somewhere on the screen
# K_UP                  up circle
# K_DOWN                down circle
# K_RIGHT               right circle
# K_LEFT                left circle
# K_a                   left square
# K_d                   right square
# K_w                   up square
# K_s                   down square
# K_SPACE               jump
#initialize pygame

import os, random, time, pygame, math, datetime
from decimal import ROUND_UP
os.system('clear')
name=input("What is your name? ")
#initialize pygame
pygame.init()

#Declare constants, variables, list, dictionaries, any object
#scree size
WIDTH=700
HEIGHT=700
xMs=50
yMs=250
wb=30
hb=30
eaten=0
MAIN=True
INST=False
SETT=False
BACKCLR=False
CRCLR=False
LEV_I=False
LEV_II=False
LEV_III=False
PSCORE1=False
PSCORE2=False
PSCORE3=False
SCORE=False

#List f messages
MenuList=['Instructions','Settings', "Level I","Level II",'Level III','Scoreboard','Exit']
SettingList=['Screen Size','Backgrnd Color','Icon','']
check=True #for the while loop

clock=pygame.time.Clock()

#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats Square')

#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}
#Get colors
BackColorList=['aqua',"purple", "white", "orange"]
CrClrList=['red', "navy", "pink", "white"]
background= colors.get('navy')
randColor=''
cr_color=colors.get('orange')
sqM_color=colors.get('pink')
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
    txt=INST_FNT.render("Control the circle with the arrow keys", 1,(5, 31, 64))
    screen.blit(txt,(90,200))
    txt=INST_FNT.render("and absorb the square. If there is a ", 1, (5, 31, 64))
    screen.blit(txt,(90,240))
    txt=INST_FNT.render("second player, control the square with",1, (5, 31, 64))
    screen.blit(txt, (90,280))
    txt=INST_FNT.render("the wasd keys. You got to be quick!",1, (5, 31, 64))
    screen.blit(txt, (90,320))
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
    eaten=0
    move=5 #pixels
    #square variables
    xs=20
    ys=20
    wbox=30
    hbox=30
    #circle variables
    rad=15
    xc=random.randint(rad, WIDTH-rad)
    yc=random.randint(rad, HEIGHT-rad)
    #inscribed Square:
    ibox=int(rad*math.sqrt(2))
    startpoint = (int(xc-ibox/2),int(yc-ibox/2))
    print(startpoint[0]-ibox,startpoint[1])
    insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
    #creating the rect object
    square=pygame.Rect(xs,ys,wbox,hbox)
    global MAIN
    global LEV_I
    startpoint = (int(xc-ibox/2),int(yc-ibox/2))
    insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
    sq_color=colors.get(randColor)
    MAX=10
    jumpCount=MAX
    JUMP=False
    run=True
    while run:
        eaten=0
        screen.fill(background)
        keys=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                MAIN=True
                LEV_I=False
                
                
        if keys[pygame.K_ESCAPE]:
            run=False        
        if keys[pygame.K_a] and square.x >=move:
                square.x -= move #substract 5 from the x value
        if keys[pygame.K_d] and square.x <WIDTH-wbox:
            square.x += move  
        #Jumping part
        if not JUMP:
            if keys[pygame.K_w]:
                square.y -= move
            if keys[pygame.K_s]:
                square.y += move   
            if keys[pygame.K_SPACE]:
                JUMP=True
        else:
            if jumpCount >=-MAX:
                square.y -= jumpCount*abs(jumpCount)/2
                jumpCount-=1
            else:
                jumpCount=MAX
                JUMP=False

    #Finish circle
        if keys[pygame.K_LEFT] and xc >=rad+move:
            xc -= move #substract 5 from the x value
            insSquare.x -= move
        if keys[pygame.K_RIGHT] and xc <=WIDTH -(rad+move):
            xc += move #substract 5 from the x value  
            insSquare.x += move
        if keys[pygame.K_DOWN] and yc <=HEIGHT-(rad+move):
            yc += move #substract 5 from the x value
            insSquare.y += move
        if keys[pygame.K_UP] and yc >=rad+move:
            yc -= move #substract 5 from the x value  
            insSquare.y -= move
            
        checkCollide = square.colliderect(insSquare)
        if checkCollide:
            square.x=random.randint(wbox, WIDTH-wbox)
            square.y=random.randint(hbox, HEIGHT-hbox)   
            changeColor()
            sq_color=colors.get(randColor)
            rad +=move
            eaten+=1
            ibox=int(rad*math.sqrt(2))
            startpoint = (int(xc-ibox/2),int(yc-ibox/2))
            insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
        pygame.draw.rect(screen, sq_color, square)
        pygame.draw.rect(screen,cr_color, insSquare )
        pygame.draw.circle(screen, cr_color, (xc,yc), rad)

        if eaten>=10:
            LEV_I=False
            MAIN=True
  

        pygame.display.update()
        pygame.time.delay(10)

def ReturnBut(message):
    txt=MENU_FNT.render(message, 1, (255, 255, 255))
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,550))


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
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
        if case.type ==pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            xm= mouse_pos[0]
            ym= mouse_pos[1]
        # print(mouse_pos)
    keys=pygame.key.get_pressed() #this returns a list
    if MAIN:
        eaten=0
        screen.fill(background)
        TitleMenu("MENU")
        MainMenu(MenuList)
    if INST and first:
        screen.fill(background)
        TitleMenu("INSTRUCTIONS")
        instr()
        first=False
    if INST:
        if keys[pygame.K_ESCAPE]:
            INST=False
            MAIN=True
            first=True
    if SETT:
        screen.fill(background)
        TitleMenu("SETTINGS")
        MainMenu(SettingList)
        if keys[pygame.K_ESCAPE]:
            SETT=False
            MAIN=True
    if BACKCLR:
        screen.fill(background)
        TitleMenu("Background Color")
        ReturnBut("Back")
        MainMenu(BackColorList)
    if LEV_I:
        ReturnBut("Return to Menu")
        screen.fill(background)
        playGame()
        LEV_I=False
        MAIN=True
        if eaten>10:
            LEV_I=False
            MAIN=True
    if LEV_II:
        ReturnBut("Return to Menu")
        screen.fill(background)
        TitleMenu("LEVEL II")
        if keys[pygame.K_ESCAPE]:
            LEV_II=False
            MAIN=True
    if LEV_III:
        screen.fill(background)
        TitleMenu("LEVEL III")
        if keys[pygame.K_ESCAPE]:
            LEV_III=False
            MAIN=True
    if SETT:
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290))or BACKCLR:
            SETT=False
            screen.fill(background)
            BACKCLR=True
            pygame.time.delay(300)
            mouse_pos=(0,0)
        if((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340))or CRCLR:
            SETT=False
            CRCLR=True
            pygame.time.delay(300)
            mouse_pos=(0,0)

    if BACKCLR:
        if ((mouse_pos[0] >306 and mouse_pos[0] <393) and (mouse_pos[1] >560 and mouse_pos[1] <595)) or SETT:
            BACKCLR=False
            SETT=True
            pygame.time.delay(300)
            mouse_pos=(0,0)
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290)):
            background=colors.get('aqua')  
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340)):
            background=colors.get('purple')    
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <390)):
            background=colors.get('yellow')
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <440)):
            background=colors.get('orange')
    if CRCLR:
        screen.fill(background)
        TitleMenu("Circle Color")
        ReturnBut("Back")
        MainMenu(CrClrList)
    
    if CRCLR:
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290)):
            cr_color=colors.get('red')
            inscribSq_color=colors.get('red')  
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340)):
            cr_color=colors.get('navy')
            inscribSq_color=colors.get('navy')  
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <390)):
            cr_color=colors.get('pink')  
            inscribSq_color=colors.get('pink')  
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <440)):
            cr_color=colors.get('white')  
            inscribSq_color=colors.get('white')  
        if ((mouse_pos[0] >306 and mouse_pos[0] <393) and (mouse_pos[1] >560 and mouse_pos[1] <595)) or SETT:
            CRCLR=False
            SETT=True
            pygame.time.delay(300)
            mouse_pos=(0,0)
    
    if not MAIN and not LEV_I:
        if ((mouse_pos[0] >210 and mouse_pos[0] <490) and (mouse_pos[1] >561 and mouse_pos[1] <595))or MAIN:
            if INSTR:
                INSTR=False
                MAIN=True
            if SETT:
                SETT=False
                MAIN=True
            if PSCORE1:
                PSCORE1=False
                MAIN=True
        
    if SCORE and screCk:
        screen.fill(background)
        TitleMenu("SCOREBOARD")
        scoreBoard()
        #call funct t print scres
        screCk=False
    if SCORE:
        if keys[pygame.K_ESCAPE]:
            SCORE=False
            MAIN=True
            screCk=True
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290))or INST :
        MAIN=False
        INST=True
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <330))or SETT :
        MAIN=False
        SETT=True  
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <380))or LEV_I :
        MAIN=False
        LEV_I=True   
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <430))or LEV_II :
        MAIN=False
        LEV_II=True   
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >450 and mouse_pos[1] <480))or LEV_III :
        MAIN=False
        LEV_III=True   
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >500 and mouse_pos[1] <530))or SCORE :
        MAIN=False
        SCORE=True 
        
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