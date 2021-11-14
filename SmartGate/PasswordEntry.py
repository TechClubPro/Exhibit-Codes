
from Phygital_v0 import Phygital_v0 as pyro
import time


pyro.pinMode('A4','dInput')
pyro.pinMode('A5','dInput')

pyro.init('COM6')
pyro.MoveServo(10,90)


UserData={"Abhilash":"PyRo",
          "Rohan":"Robotics",
          "Arya":"PyProg",
          "Mitali":"MyPasswd"}

invalidCount=0
while True:
    try:
        print("Smart Gate:: Ready to Authenticate your Vehicle")
        data1=pyro.dRead('A4')
        data2=pyro.dRead('A5')
#        print(data1,data2)
        if invalidCount<=3:
            if data1==0:
                username=input("Username: ")
                password=input("Password: ")
                
                if username in UserData:
                    if password==UserData[username]:
                        print("Authenticated")
                        pyro.MoveServo(10,135)
                        time.sleep(4)
                    else:
                        print("UnAuthorized password")
                        invalidCount+=1
                else:
                    print("Wrong Username")
                    invalidCount+=1
        else:
            print("You are blocked!!")
            print("Please remove your vehicle")
            if data1==1:
                invalidCount=0
                
            
            
        if data2==0:
            pyro.MoveServo(10,90)
            
            
            
        
    except:
        if KeyboardInterrupt:
            pyro.close()
            break

