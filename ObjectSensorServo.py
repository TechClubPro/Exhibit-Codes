"""
Program to Read the State of Object Sensor 
and Display it on Console.
"""

from Phygital_v0 import Phygital_v0 as pyro
import time


# Pin Initialization
pyro.pinMode('A0','dInput')
pyro.pinMode('A3','dInput')
pyro.pinMode('A4','dInput')
pyro.pinMode('A5','dInput')
#Communication Init
pyro.init("COM7")

while True:
    try:
           
        #Read State of Sensor
        data1=pyro.dRead('A3')
        data2=pyro.dRead('A4')
        data3=pyro.dRead('A5')
        print("Sensor State: "+ str(data1) + str(data2)+ str(data3))
       
     
      
        if data1==0:# Object Sensed
            print("Object Sensed")
	       
            pyro.MoveServo(9,175)
            time.sleep(1)   
        else:
            print("No Object")
	        
            pyro.MoveServo(9,5) 
            time.sleep(1)
            
            
        if data2==0:# Object Sensed
            print("Object Sensed")
	       
            pyro.MoveServo(10,5)
            time.sleep(1)   
        else:
            print("No Object")
	        
            pyro.MoveServo(10,175) 
            time.sleep(1)
      
        
    
    
    except:
        if KeyboardInterrupt:
            pyro.close()
            break
print("Closing")