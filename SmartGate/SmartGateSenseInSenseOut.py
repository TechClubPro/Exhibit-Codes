from Phygital_v0 import Phygital_v0 as pyro



pyro.pinMode('A0','dInput')
pyro.pinMode('A2','dInput')


pyro.init("COM6")

pyro.MoveServo(9,10)

while True:
    try:
        entrySensor = pyro.dRead('A0')
        exitSensor  = pyro.dRead('A2')
        
        
        if entrySensor==1 and exitSensor==0:         
            pyro.MoveServo(9,90)            
            
        if entrySensor==0 and exitSensor==1:           
            pyro.MoveServo(9,10)        
                    
            
    except:
        if KeyboardInterrupt:
            pyro.close()
            break
print("Closing")
                
        
        
        