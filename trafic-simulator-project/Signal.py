# from Traffic import *
import numpy as np
from movement import movementLane
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
        while(i<3):
            movementLane(r[j].x , r , i )
            



def mainSiganl(p):
    s =[]
    colour = ['O','O','O','O']
    i=0
    while(i<4):
        s.append(Signal(colour))
        i+=1
    
    i=0
    while(i<4):
        print("\n")
        s[i].lightGreen(24,3)
        print(p[i].x)
        i+=1
