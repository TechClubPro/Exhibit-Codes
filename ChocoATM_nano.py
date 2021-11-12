

import pygame, sys
import time
from Phygital_v0 import Phygital_v0 as phy

pygame.init()

WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
phy.init('COM7')


phy.MoveServo(9,90)

phy.MoveServo(10,45)



class Button():
    def __init__(self, txt, location, action, bg=WHITE, fg=BLACK, size=(80, 30), font_name="Segoe Print", font_size=16):
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.size = size

        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)

        self.call_back_ = action

    def draw(self):
        #self.mouseover()

        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)

    def mouseover(self):
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = GREY  # mouseover color

    def call_back(self):
        self.call_back_()

def wrongAns():

   global ans
   
   phy.MoveServo(9,170)
   time.sleep(0.5)
#   phy.MoveServo(1,169)
#   time.sleep(1)
   ans="wrong"
   return ans

def rightAns():

   global ans
   phy.MoveServo(9,10)

   ans="right"
   return ans

def Option_A():

   global state
   global ansGiven

   state="compare"
   ansGiven="A"

   print("A Pressed")
   return state

def Option_B():
    global state
    global ansGiven

    state="compare"
    ansGiven="B"

    print("B Pressed")
    return state

def Option_C():
    global state
    global ansGiven

    state="compare"
    ansGiven="C"


    print("C Pressed")
    return state

def Option_D():
    global state
    global ansGiven

    state="compare"
    ansGiven="D"


    print("D Pressed")
    return state

def mousebuttondown():
    pos = pygame.mouse.get_pos()
    for button in buttons:
        if button.rect.collidepoint(pos):
            button.call_back()

width=820
height=312

screen = pygame.display.set_mode( ( width, height) )

#Set a Title of Screen
pygame.display.set_caption('ChocoATM')

#Background = pygame.image.load("D:/Renuka/Python/.spyder-py3/images/backgroundimg.jpg").convert()
Background = pygame.image.load("images/backgroundimg.jpg").convert()
#Draw screen from location x=0,y=0
screen.blit(Background,(0,0))

RED = (255, 0, 0)
BLUE = (0, 0, 255)

button_01 = Button("A", (175, 250), Option_A,bg=(255,69,0))
button_02 = Button("B", (325, 250), Option_B, bg=(255,69,0))
button_03 = Button("C", (475, 250), Option_C, bg=(255,69,0))
button_04 = Button("D", (625, 250), Option_D, bg=(255,69,0))
buttons = [button_01, button_02,button_03,button_04]
global que
global ans
global state
global ansGiven
global AnsArray
global score
que=1
state="question"
ans="none"
ansGiven="none"
AnsArray=["C","D","D","A","A"]
score=0
eventstatus="none"
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            phy.close()
            pygame.quit()
            sys.exit()
            eventstaus="quit"
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousebuttondown()

    if eventstatus=="quit":
        break
    if(state=="question"):
        if(que<=5):
            if(que==1):
                screen.blit(Background,(0,0))
                #path = pygame.image.load("D:/Renuka/Python/.spyder-py3/images/ChocoATM Qs/1.png").convert_alpha()
                path = pygame.image.load("images/KidsQuestions/1.png").convert_alpha()
                screen.blit(path,(0,0))

            if(que==2):
                screen.blit(Background,(0,0))
                #path = pygame.image.load("D:/Renuka/Python/.spyder-py3/images/ChocoATM Qs/2.png").convert_alpha()
                path = pygame.image.load("images/KidsQuestions/2.png").convert_alpha()
                screen.blit(path,(0,0))

            if(que==3):
                screen.blit(Background,(0,0))
                #path = pygame.image.load("D:/Renuka/Python/.spyder-py3/images/ChocoATM Qs/3.png").convert_alpha()
                path = pygame.image.load("images/KidsQuestions/3.png").convert_alpha()
                screen.blit(path,(0,0))

            if(que==4):
                screen.blit(Background,(0,0))
                #path = pygame.image.load("D:/Renuka/Python/.spyder-py3/images/ChocoATM Qs/4.png").convert_alpha()
                path = pygame.image.load("images/KidsQuestions/4.png").convert_alpha()
                screen.blit(path,(0,0))

            if(que==5):
                screen.blit(Background,(0,0))
                #path = pygame.image.load("D:/Renuka/Python/.spyder-py3/images/ChocoATM Qs/5.png").convert_alpha()
                path = pygame.image.load("images/KidsQuestions/5.png").convert_alpha()
                screen.blit(path,(0,0))

            for button in buttons:
                button.draw()

            state="reading"

        else:
             state="result"

    if(state=="reading"):
        print("Waiting for Answers")

    if(state=="compare"):
        if(AnsArray[que-1]==ansGiven):
            ans="right"
            state="response"
        else:
            ans="wrong"
            state="response"

    if(state=="response"):

        if(ans=="right"):
            rightAns()
            #path = pygame.image.load("D:/Renuka/Python/.spyder-py3/images/ChocoATM Qs/7.png").convert_alpha()
            path = pygame.image.load("images/KidsQuestions/7.png").convert_alpha()
            screen.blit(path,(0,0))
            score+=1

        if(ans=="wrong"):
            wrongAns()
            #path = pygame.image.load("D:/Renuka/Python/.spyder-py3/images/ChocoATM Qs/6.png").convert_alpha()
            path = pygame.image.load("images/KidsQuestions/6.png").convert_alpha()
            screen.blit(path,(0,0))

        pygame.display.update()
        time.sleep(2)
        phy.MoveServo(9,90)
        state="question"
        que=que+1

    if(state=="result"):

        if(score>=4):
            #path = pygame.image.load("D:/Renuka/Python/.spyder-py3/images/ChocoATM Qs/8.png").convert_alpha()
            path = pygame.image.load("images/KidsQuestions/8.png").convert_alpha()
            screen.blit(path,(0,0))
            phy.MoveServo(10,135)
            time.sleep(1)
            phy.MoveServo(10,45)


        else:
            #path = pygame.image.load("D:/Renuka/Python/.spyder-py3/images/ChocoATM Qs/9.png").convert_alpha()
            path = pygame.image.load("images/KidsQuestions/9.png").convert_alpha()
            screen.blit(path,(0,0))

        state="none"

    pygame.display.update()
    time.sleep(0.05)
