from Phygital_v0 import Phygital_v0 as pyro
import time
import random

pyro.pinMode('A3','dInput')
pyro.pinMode('A4','dInput')
pyro.pinMode('A5','dInput')

pyro.init("COM6")

state="Start"
PointerServo=[10,90,170]
Score=0
time.sleep(1)
while True:
    try:
        if state=="Start":
            pyro.MoveServo(10,90)
            _bin=random.randint(1,3)
            pyro.MoveServo(11,PointerServo[_bin-1])
            print(_bin)
            
            time.sleep(3)
            
            state="Read"
        if state=="Read":
            time.sleep(1)
            data1=pyro.dRead('A3')
            data2=pyro.dRead('A4')
            data3=pyro.dRead('A5')
            
            print(data1,data2,data3)
            
            if data1==0 :
                ballSensedAt=1
                state="Check"
            if data2==0 :
                ballSensedAt=2
                state="Check"
            if data3==0:
                ballSensedAt=3
                state="Check"
        if state=="Check":
            if ballSensedAt==_bin:
                pyro.MoveServo(10,170)
                print("Superb!!You are a real Athlete!!")
                
            else:
                pyro.MoveServo(10,10)
                print("Better Luck Next Time!!")
            
         
                                    
            state="Continue"
        if state=="Continue":
            cont=input("Do you wish to play again? y/n")
            if cont=='y':
                state="Start"
            else:
                break
        
        
        
    except:
        if KeyboardInterrupt:
            pyro.close()
            break
print("Closing")