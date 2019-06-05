import numpy as np
from Movement import movementLane

class Signal:
    
    direction = "clockwise"
    light  = np.chararray((4),unicode=True)
    
    def __init__(self,colour):
        self.dur = 60
        i=0
        while(i<4):
            self.light[i] = colour[i]
            i+=1
    
    def lightGreen(self,j , r):
        
        i=1
        

def mainSiganl(p):
    s =[]
    colour = ['O','O','O','O']
    i=0
    while(i<4):
        s.append(Signal(colour))
        i+=1
    i=0
    while(i<4):
        s[i].lightGreen(24,3)
        print("for road ",i+1)
        print(p[i].sp)
        i+=1