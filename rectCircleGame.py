import os, time, random, math, sys
from this import d
from secrets import randbelow
import pygame as p
from pygame.locals import *
#controls
# K_UP      up arrow
# K_Down    down arrow
# K_RIGHT   right arrow
# K_LEFT    left arrow
# K_W       up square
# K_A       left square
# K_S       down square
# K_D       right square
# K_SPACE   jump square
# K_RSHIFT  right shift
# K_LSHIFT  left shift

p.init()
p.display.set_caption('game base')
screen = p.display.set_mode((500, 500),0,32)

font = p.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.lbit(textobj, textrect)

click = False

def main_menu():
    while True:
        screen.fill(0,124,255)
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20 )

        mx, my =p.mouse.get_pos()

        button_1 = p.Rect(50, 100, 200, 50)
        button_2 = p.Rect(50, 100, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        p.draw.rect(screen, (255, 0, 0), button_1)
        p.draw.rect(screen, (255, 0, 0), button_2)

        click = False
        for event in p.event.get():
            if event.type == QUIT:
                p.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    p.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        p.display.update()

def options ():
    running = True
    while running:
        screen.fill((0,0,0))
        draw_text('options', font, (255, 255, 255), screen, 20, 20 )
        for event in p.event.get():
                if event.type == QUIT:
                    p.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                       running = False

def game ():
    running = True
    while running:
        screen.fill((0,0,0))
        colors={'red' :[255,0,0], 'white' :[255,255,255], 'mag' :[255,0,255], 'aqua' :[51, 153,255], 'm' :[47,192,299]}
    move=8 #pixels
    WIDTH=700
    HEIGHT=700
    Y=25
    X=15
    xc=random.randint(50, WIDTH-50)
    yc=random.randint(50, HEIGHT-50)
    wbox=20
    hbox=20
    rad=10
    check=True
    screen=p.display.set_mode((WIDTH,HEIGHT))
    square=p.Rect(X,Y,hbox,wbox)
    randColor=random.choice(list(colors))
    backround=colors.get('white')
    sq_color=colors.get(randColor)
    cr_color=colors.get('mag')
    randColor=''
    def changeClr():
        print(backround)
        global sq_color
        colorCheck=True
        randColor=random.choice(list(colors))
        while colorCheck:
            if colors.get(randColor) == backround:
                randColor=random.choice(list(colors))
            else:
                colorCheck=False
        sq_color=colors.get(randColor)
    JUMPSQ=False
    JUMPCR=False
    jumpCount=7
    COUNT=10    
    CIRCUMFERENCE= 2 *math.pi* rad
    p.display.set_caption("Circle Eats Square")
    p.display.set_mode((WIDTH,HEIGHT))

    changeClr()

    while check:
        screen.fill(backround)
        for case in p.event.get():
            if case.type==p.QUIT:
                check=False
        #square movements
        keys=p.key.get_pressed()
        if keys[p.K_a] and square.x>move:
            square.x-=move
        if keys[p.K_d] and square.x<=WIDTH-wbox:
            square.x+=move
    
        #jump code
        if not JUMPSQ:
            if keys[p.K_w] and square.y>move:
                square.y-=move
            if keys[p.K_s] and square.y<=HEIGHT-hbox:
                square.y+=move
            if keys[p.K_SPACE]:
                JUMPSQ=True
        else:
            if jumpCount >= -COUNT:
                square.y-= jumpCount*abs(jumpCount)/2
                jumpCount -=1
            else:
                jumpCount=COUNT
                JUMPSQ=False
    
        #circle movements
        if keys[p.K_LEFT] and xc>rad:
            xc-=move
        if keys[p.K_RIGHT] and xc<WIDTH-rad:
            xc+=move
    
        if not JUMPCR:
            if keys[p.K_UP] and yc>rad+move:
                yc-=move
            if keys[p.K_DOWN] and yc<HEIGHT-rad:
                yc+=move
            if keys[p.K_RSHIFT] or keys[p.K_LSHIFT]:
                JUMPCR=True
        else:      
            if jumpCount >= -COUNT:
                yc-= jumpCount*abs(jumpCount)/2
                jumpCount -=1
            else:
                jumpCount=COUNT
                JUMPCR=False
    
        p.draw.rect(screen, sq_color, square)
        p.draw.circle(screen, cr_color, (xc,yc), rad)
        p.display.update()
        boolB=square.collidepoint(xc,yc)
    
        if boolB:
            square.x=random.randint(50, WIDTH-50)
            square.y=random.randint(50, WIDTH-50)
            changeClr()
            rad +=move
    
        p.draw.rect(screen, sq_color, square)
        p.draw.circle(screen, cr_color, (xc,yc), rad)
        p.display.update()
        p.time.delay(30)

        for event in p.event.get():
                if event.type == QUIT:
                    p.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                       running = False

    

main_menu ()