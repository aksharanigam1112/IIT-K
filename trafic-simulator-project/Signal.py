import numpy as np
from Movement import movementLane
import math

class Signal:
    
    def __init__(self,colour):
        self.light  = np.chararray((4),unicode=True)
        self.dur = 30
        i=0
        while(i<4):
            self.light[i] = colour[i]
            i+=1
    
    def moveForward(self,arr):
        self.arr = arr
        i=0
        j=1
        while(j<3):
            while(i<25 and arr[i][j]==''):
                i+=1

            k = i            
            i=0

            while(k<25 and arr[k][j]!=''):
                arr[i][j] = arr[k][j]
                arr[k][j]=''
                k+=1
                i+=1

            j+=1
        print(arr)
        return arr

    def lightGreen(self,i ,r):
        j=1
        while(j<3):

            count=0
            k=0
            time =self.dur
            while(k<25 and r[i].x[k][j]!='' and time>0 and r[i].vehicles>=1):

                time -= int(math.ceil(100/r[i].sp[k][j]))
                count+=1

                if(r[i].x[k][j]=='T1'or r[i].x[k][j]=='B1'):
                    n = k
                    while(n<=(k+5)):
                        r[i].x[n][j] = ''
                        n+=1
                    k+=5

                elif(r[i].x[k][j]=='T21'or r[i].x[k][j]=='T22'):
                    n = k
                    while(n<=(k+7)):
                        r[i].x[n][j] = ''
                        n+=1
                    k+=7

                elif(r[i].x[k][j]=='T31'or r[i].x[k][j]=='T32'):
                    n = k
                    while(n<=(k+6)):
                        r[i].x[n][j] = ''
                        n+=1
                    k+=6
                            
                elif(r[i].x[k][j]=='C1' or r[i].x[k][j]=='E' or r[i].x[k][j]=='T4'):
                    n = k
                    while(n<=(k+2)):
                        r[i].x[n][j] = ''
                        n+=1
                    k+=2
                                          
                elif(r[i].x[k][j]=='B2' or r[i].x[k][j]=='C2'):
                    n = k
                    while(n<=(k+1)):
                        r[i].x[n][j] = ''
                        n+=1
                    k+=1
                    
            print("\nTime taken by the lane ",j," is ",(self.dur-time))  
            print("\nTotal Vehicles that crossed the round about from this lane ",count)                            
            r[i].vehicles-=count
            j+=1

        print("\n\t\tNew Arrangement for road ",(i+1),"\n")
        r[i].x=self.moveForward(r[i].x)
        
        
        count=0
        k=0
        while(k<25 and r[i].x[k][0]!='' and r[i].vehicles>=1):
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
    
    def FCFS(self,colour,r):
    
        self.r = r
        self.colour = colour
        if(colour == ['O','O','O','O']):
            i = 0
            while(i < 4):
                j = 1
                while(j<3):
                    k = 0
                    while(k<25):
                        if(r[i].x[k][j] != '' and r[i].x[k][j] == 'T1' and j == 1):
                            print("Truck from road ",i+1," and of straight lane will pass")
                            k += 5

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T22' and j == 1):
                            print("Loaded Tanker from road ",i+1," and of straight lane will pass")
                            k += 6

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T21' and j == 1):
                            print("Unloaded Tanker from road ",i+1," and of straight lane will pass")
                            k += 6

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T32' and j == 1):
                            print("Loaded Troller from road ",i+1," and of straight lane will pass")
                            k += 7

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T31' and j == 1):
                            print("Unloaded Tanker from road ",i+1," and of straight lane will pass")
                            k += 7

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'B1' and j == 1):
                            print("Bus from road ",i+1," and of straight lane will pass")
                            k += 5

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'C1' and j == 1):
                            print("Car from road ",i+1," and of straight lane will pass")
                            k += 2

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'E' and j == 1):
                            print("E-Rickshaw from road ",i+1," and of straight lane will pass")
                            k += 2

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T4' and j == 1):
                            print("Tempo from road ",i+1," and of straight lane will pass")
                            k += 2

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'B2' and j == 1):
                            print("Bike/Scooty from road ",i+1," and of straight lane will pass")
                            k += 1

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'C2' and j == 1):
                            print("Cycle from road ",i+1," and of straight lane will pass")
                            k += 1

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T1' and j == 2):
                            print("Truck from road ",i+1," and of right lane will pass")
                            k += 5

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T22' and j == 2):
                            print("Loaded Tanker from road ",i+1," and of right lane will pass")
                            k += 6

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T21' and j == 2):
                            print("Unloaded Tanker from road ",i+1," and of right lane will pass")
                            k += 6

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T32' and j == 2):
                            print("Loaded Troller from road ",i+1," and of right lane will pass")
                            k += 7

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T31' and j == 2):
                            print("Unloaded TrollerTruck from road ",i+1," and of right lane will pass")
                            k += 7

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'B1' and j == 2):
                            print("Bus from road ",i+1," and of right lane will pass")
                            k += 5

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'C1' and j == 2):
                            print("Car from road ",i+1," and of right lane will pass")
                            k += 2

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'E' and j == 2):
                            print("E-Rickshaw from road ",i+1," and of right lane will pass")
                            k += 2

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T4' and j == 2):
                            print("Tempo from road ",i+1," and of right lane will pass")
                            k += 2

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'TB2' and j == 2):
                            print("Bike/Scooty from road ",i+1," and of right lane will pass")
                            k += 1
                        
                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'TC2' and j == 2):
                            print("Cycle from road ",i+1," and of right lane will pass")
                            k += 1
                        
                        else:
                            continue
                    j += 1
                i += 1

def mainSignal(p):
    s =[]
    colour = ['O','O','O','O']
    i=0
    while(i<4):
        s.append(Signal(colour))
        i+=1

    print("\n\t\tWhen Signal is given Clockwise")
    i=0
    while(i<4):                         # For Clockwise Signal behaviour
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

    print("\n\t\tWhen Signal is given Anticlockwise")
    i=3
    while(i>=0):                         # For Anti-Clockwise Signal behaviour
        print("\n\n\t\tSignal is Green for road ",(i+1),"\n")
        print(p[i].x,"\n")
        print(p[i].sp,"\n")
        s[i].lightGreen(i,p)
        s[i].light[i] = 'G'
        x = (i-1)%4
        s[i].light[x]='O'
        x = (i-2)%4
        s[i].light[x] = 'R'
        x = (i-3)%4
        s[i].light[x] = 'R'
        print("\n\tSignal was as follows :-",s[i].light)
        i-=1
