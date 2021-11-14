from Phygital_v0 import Phygital_v0 as pyro
import time
import vlc

pyro.pinMode('A3','dInput')
pyro.pinMode('A4','dInput')
pyro.pinMode('A5','dInput')

pyro.init("COM6")



VidDict={"001":['TajMahal','videos/tajmahal.mp4'],
                "100":['BurjKhalifa','videos/bk.mp4'],
                "110":['Buckinghum Palace','videos/bp.mp4'],
                "010":['brd','brd.mp4'],
                "111":['NoCard']}

mediaPlaying=False
media=vlc.MediaPlayer()

state="Read"
previousCode="444"

while True:
    try:
        
#       
        if state=="Read":
            data1=pyro.dRead('A3')
            data2=pyro.dRead('A4')
            data3=pyro.dRead('A5')
            
            print(data1,data2,data3)
            code=str(data1)+str(data2)+str(data3)
            time.sleep(1)
        
#            code=input("E:")
                      
            if code=="111":
                print("No Card Placed")
                if mediaPlaying==True:
                    media.stop()
                    mediaPlaying=False
            else:
                
                
                if code != previousCode:
                    if mediaPlaying==True:
                        media.stop()
                    state="Play"
                    previousCode=code
                
        if state=="Play":        
                # creating vlc media player object
                
                if code=="001":
                    media = vlc.MediaPlayer("videos/tajmahal.mp4")
                    media.play()
                    mediaPlaying=True
                    
                if code=="100":
                    media = vlc.MediaPlayer("videos/bk.mp4")
                    media.play()
                    mediaPlaying=True
                    
                if code=="110":
                    media = vlc.MediaPlayer("videos/bp.mp4")
                    media.play()
                    mediaPlaying=True
                    
                if code=="010":
                    media = vlc.MediaPlayer("videos/brd.mp4")
                    media.play()
                    mediaPlaying=True 
                
                
                state="Read"
        
                
            
            
           
        
        
    except:
        if KeyboardInterrupt:
            pyro.close()
            break
print("Closing")