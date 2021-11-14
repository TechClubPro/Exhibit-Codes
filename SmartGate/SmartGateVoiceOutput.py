from Phygital_v0 import Phygital_v0 as pyro
import time
import random
import pyttsx3

pyro.pinMode('A0','dInput')
pyro.pinMode('A2','dInput')
pyro.pinMode('A5','dInput')

pyro.init("COM6")



engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

pyro.MoveServo(9,10)

while True:
    try:
        entrySensor = pyro.dRead('A0')
        exitSensor  = pyro.dRead('A2')
        
        
        if entrySensor==1 and exitSensor==0:
           
            engine.say("Someone's at the entry,Opening the door")
            engine.runAndWait() 
            pyro.MoveServo(9,90)
            
            
        if entrySensor==0 and exitSensor==1:
           
            engine.say("Exit point, closing the door")
            engine.runAndWait() 
            pyro.MoveServo(9,10)        
                    
            
    except:
        if KeyboardInterrupt:
            pyro.close()
            break
print("Closing")
                
        
        
        