import numpy as np
from Movement import movementLane
import math

class Signal:
    
    direction = "clockwise"

    def __init__(self,colour):
        self.light  = np.chararray((4),unicode=True)
        self.dur = 30
        i=0
        while(i<4):
            self.light[i] = colour[i]
            i+=1

    def lightGreen(self,i ,r):
        j=1
        while(j<3):

            count=0
            k=0
            time =self.dur
            while(r[i].x[k][j]!='' and time>0):

                time -= int(math.ceil(100/r[i].sp[k][j]))
                count+=1

                if(r[i].x[k][j]=='T1'or r[i].x[k][j]=='B1'):
                    k+=5

                elif(r[i].x[k][j]=='T21'or r[i].x[k][j]=='T22'):
                    k+=7

                elif(r[i].x[k][j]=='T31'or r[i].x[k][j]=='T32'):
                    k+=6
                            
                elif(r[i].x[k][j]=='C1' or r[i].x[k][j]=='E' or r[i].x[k][j]=='T4'):
                    k+=2
                                          
                elif(r[i].x[k][j]=='B2' or r[i].x[k][j]=='C2'):
                    k+=1
            print("\nTime taken by the lane ",j," is ",(self.dur-time))  
            print("\nTotal Vehicles that crossed the round about from this lane ",count)                            
            r[i].vehicles-=count
            j+=1
        
        count=0
        k=0
        while(r[i].x[k][0]!=''):
            count+=1
            if(r[i].x[k][0]=='T1'or r[i].x[k][0]=='B1'):
                k+=5

            elif(r[i].x[k][0]=='T21'or r[i].x[k][0]=='T22'):
                k+=7

            elif(r[i].x[k][0]=='T31'or r[i].x[k][0]=='T32'):
                k+=6
                            
            elif(r[i].x[k][0]=='C1' or r[i].x[k][0]=='E' or r[i].x[k][0]=='T4'):
                k+=2
                                          
            elif(r[i].x[k][0]=='B2' or r[i].x[k][0]=='C2'):
                k+=1

        r[i].vehicles-=count
        print("\nVehicles remaining for this road:- ",r[i].vehicles)


def mainSignal(p):
    s =[]
    colour = ['O','O','O','O']
    i=0
    while(i<4):
        s.append(Signal(colour))
        i+=1

    i=0
    while(i<4):
        print("\n\n\t\tSignal is Green for road ",(i+1),"\n")
        print(p[i].x,"\n")
        print(p[i].sp,"\n")
        s[i].lightGreen(i,p)
        s[i].light[i] = 'G'
        x = (i+1)%4
        s[i].light[x]='O'
        x = (i+2)%4
        s[i].light[x] = 'R'
        x = (i+3)%4
        s[i].light[x] = 'R'
        print("\n\tSignal was as follows :-",s[i].light)
        i+=1
