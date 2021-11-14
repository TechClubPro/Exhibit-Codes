# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 14:46:01 2020

@author: LearnLeap
"""

from Phygital_v0 import Phygital_v0 as pyro
import time
import pygame, sys
import random


pygame.init()

width=695
height=616

screen = pygame.display.set_mode((width, height) )

#Set a Title of Screen
pygame.display.set_caption('CodeReader')



pyro.pinMode('A3','dInput')
pyro.pinMode('A4','dInput')
pyro.pinMode('A5','dInput')

pyro.init("COM6")

CarDict={"001":['mitsubishi','OutlanderMit.jpg','PajeroMit.jpg','LancerMit.jpeg'],
                "100":['chevrolet','ChevCamero.jpg','ChevSUV.jpg','ChevTavera.jpg'],
                "110":['audi','AudiQ2.jpg','AudiQ8.jpg','AudiSportBack.jpg'],
                "010":['wolkswagon','VWJetta.jpg','VWPolo.jpg','VWWento.jpg'],
                "111":['NoCard']}

CarImageList=['OutlanderMit.jpg','PajeroMit.jpg','LancerMit.jpeg','ChevCamero.jpg','ChevSUV.jpg','ChevTavera.jpg','AudiQ2.jpg','AudiQ8.jpg','AudiSportBack.jpg','VWJetta.jpg','VWPolo.jpg','VWWento.jpg']
CarNamesList=['Outlander','Pajero','Lancer','Camero','SUV','Tavera','Q2','Q8','SportBack','Jetta','Polo','Wento']
GameState="Start"

prevNum=23
imageCount=0
score=0

eventstatus="none"

while True:
    pygame.display.update()
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pyro.close()
                pygame.quit()
                sys.exit()
                eventstaus="quit"
                break
        if eventstatus=="quit":
                break
            
        if GameState=="Start":
            numList=random.sample(range(0,11),5)
            print(numList)
            path = pygame.image.load("Images/start.png").convert_alpha()
            screen.blit(path,(0,0))
            pygame.display.update()
            GameState="ShowImage"
            time.sleep(5)
        if GameState=="ShowImage":
            
            if imageCount<=4:
                
                
            
                    path = pygame.image.load("Images/refresh.png").convert_alpha()
                    screen.blit(path,(0,0))
                    path1 = pygame.image.load("Images/"+CarImageList[numList[imageCount]]).convert_alpha()
                    screen.blit(path1,(100,210))
                    
                    font = pygame.font.SysFont("Eras Bold ITC",70)
                    text=font.render(CarNamesList[numList[imageCount]],True,(255,0,0),(255,255,255))
                    screen.blit(text,(250,500))
                   
                    pygame.display.update()
                    
                    GameState="ReadAnswer"
            else:
                GameState="Result"
                
        if GameState=="ReadAnswer":
            data1=pyro.dRead('A3')
            data2=pyro.dRead('A4')
            data3=pyro.dRead('A5')
            
            code=str(data1)+str(data2)+str(data3)
            print(code)
            if code!="111":
                GameState="CheckAnswer"
                
        if GameState=="CheckAnswer":
            if code in CarDict.keys():
                
                if CarImageList[numList[imageCount]] in CarDict[code]:
                    score+=1
                    ans="right"
                    path = pygame.image.load("Images/refresh.png").convert_alpha()
                    screen.blit(path,(0,0))
                    path1 = pygame.image.load("Images/RightAnswer.png").convert_alpha()
                    screen.blit(path1,(0,0))
                    pygame.display.update()
                    Dash= pygame.mixer.Sound('Audio/Right.wav')
                    Dash.play()
                    time.sleep(2)
                else:
                    ans="wrong"
                    path = pygame.image.load("Images/refresh.png").convert_alpha()
                    screen.blit(path,(0,0))
                    path1 = pygame.image.load("Images/WrongAnswer.png").convert_alpha()
                    screen.blit(path1,(0,0))
                    Dash= pygame.mixer.Sound('Audio/Wrong.wav')
                    Dash.play()
                    pygame.display.update()
                    time.sleep(2)
                print(ans)
                GameState="RemoveCard"
            else:
                    path = pygame.image.load("Images/refresh.png").convert_alpha()
                    screen.blit(path,(0,0))
                    
                    font = pygame.font.SysFont("Eras Bold ITC",70)
                    text=font.render("Not a Valid Card!!",True,(255,0,0),(255,255,255))
                    screen.blit(text,(50,310))
                    
                    GameState="ReadAnswer"
            
        if GameState=="RemoveCard":
            data1=pyro.dRead('A0')
            data2=pyro.dRead('A1')
            data3=pyro.dRead('A2')
            
            code=str(data1)+str(data2)+str(data3)
            
            if code=="111":
                imageCount+=1
                GameState="ShowImage"
            else:
                path = pygame.image.load("Images/refresh.png").convert_alpha()
                screen.blit(path,(0,0))
                path1 = pygame.image.load("Images/RemoveCard.png").convert_alpha()
                screen.blit(path1,(0,0))
                pygame.display.update()
                
        if GameState=="Result":
            print(score)
            print("Game Over")
            
            path = pygame.image.load("Images/refresh.png").convert_alpha()
            screen.blit(path,(0,0))
           
           
            
            if score>=4:
               
                path1 = pygame.image.load("Images/threeStar.png").convert_alpha()
                screen.blit(path1,(0,0))
                pygame.display.update()
                
            elif score>=2:
                
                path1 = pygame.image.load("Images/twoStar.png").convert_alpha()
                screen.blit(path1,(0,0))
                pygame.display.update()
            elif score==1:
                
                path1 = pygame.image.load("Images/oneStar.png").convert_alpha()
                screen.blit(path1,(0,0))
                pygame.display.update()
            else:
              
                
                font = pygame.font.SysFont("Eras Bold ITC",70)
                text=font.render("Cars are not for You !!",True,(255,0,0),(255,255,255))
                screen.blit(text,(10,310))
               
                
                pygame.display.update()
            font = pygame.font.SysFont("Eras Bold ITC",70)
            text=font.render("Score: "+str(score),True,(255,0,0),(255,255,255))
            screen.blit(text,(360,150))
            
            pygame.display.update()   
                
            time.sleep(5)
            pyro.close()
            pygame.quit()
            sys.exit()
            break
            
            
            
                
        time.sleep(0.1)
    except:
        if KeyboardInterrupt:
            pyro.close()
            pygame.quit()
            break
        
print("Closing")
        
    

