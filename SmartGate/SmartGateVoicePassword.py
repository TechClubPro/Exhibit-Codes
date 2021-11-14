from Phygital_v0 import Phygital_v0 as pyro


import pyttsx3
import speech_recognition as sr

pyro.pinMode('A0','dInput')
pyro.pinMode('A2','dInput')


pyro.init("COM6")

def parse_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    command=r.recognize_google(audio)
    return command



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
           
            engine.say("Please enter the voice password")
            engine.runAndWait()
            
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Speak:")
                audio = r.listen(source)
                command=r.recognize_google(audio)
                print("You said " + command )

            if 'python' in command:
                pyro.MoveServo(9,90)
            
            
        if entrySensor==0 and exitSensor==1:
           
            engine.say("Exit point, closing the door")
            engine.runAndWait() 
            pyro.MoveServo(9,10)        
                    
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))        
    except:
        if KeyboardInterrupt:
            pyro.close()
            break
print("Closing")
                
        
        
        