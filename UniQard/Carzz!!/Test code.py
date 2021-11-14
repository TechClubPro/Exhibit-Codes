from Phygital_v0 import Phygital_v0 as pyro
import time

pyro.pinMode('A3','dInput')
pyro.pinMode('A4','dInput')
pyro.pinMode('A5','dInput')

pyro.init("COM6")

while True:
    try:
        
        data1=pyro.dRead('A3')
        data2=pyro.dRead('A4')
        data3=pyro.dRead('A5')
                
        code=str(data1)+str(data2)+str(data3)
        print(code)
        
    except:
        if KeyboardInterrupt:
            pyro.close()
           
            break