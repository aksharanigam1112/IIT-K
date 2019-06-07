import numpy as np
from Movement import movementLane
import math

class Signal:
    
    def __init__(self,colour):
        self.light  = np.chararray((4),unicode=True)
        self.dur = 10
        i=0
        while(i<4):
            self.light[i] = colour[i]
            i+=1
    
    def MoveLeft(self,arr,sp,m,r):
        count=0
        k=0
        i=0
        time =self.dur*4
        j=0
        time2=0
        scaling=10
        while(k<25 and r[i].x[k][j]!='' and time>0 and r[i].vehicles>=1):

            # time -= int(math.ceil(100/r[i].sp[k][j]))
            count+=1

            if(r[i].x[k][j]=='T1'or r[i].x[k][j]=='B1'):
                n = k
                while(n<(k+5)):
                    r[i].x[n][j] = ''
                    n+=1
                k+=5

            elif(r[i].x[k][j]=='T21'or r[i].x[k][j]=='T22'):
                n = k
                while(n<(k+7)):
                    r[i].x[n][j] = ''
                    n+=1
                k+=7

            elif(r[i].x[k][j]=='T31'or r[i].x[k][j]=='T32'):
                n = k
                while(n<(k+6)):
                    r[i].x[n][j] = ''
                    n+=1
                k+=6
                            
            elif(r[i].x[k][j]=='C1' or r[i].x[k][j]=='E' or r[i].x[k][j]=='T4'):
                n = k
                while(n<(k+2)):
                    r[i].x[n][j] = ''
                    n+=1
                k+=2
                                          
            elif(r[i].x[k][j]=='B2' or r[i].x[k][j]=='C2'):
                n = k
                while(n<(k+1)):
                    r[i].x[n][j] = ''
                    n+=1
                k+=1
            if(r[i].sp[k-1][j]!=0):
                time1= int(math.ceil(k*scaling/r[i].sp[k-1][j]))
                time2+=time1-time2
                time-=time2
            else:
                break
        r[m].sp=np.zeros((25,3))
        while(i<25 and arr[i][j]==''):
            i+=1

        k = i
        i=0

        while(k<25 and arr[k][j]!=''):
            arr[i][j] = arr[k][j]
            arr[k][j]=''
            k+=1
            i+=1
            
        while(i<25 and arr[i][j]==''):
            i+=1
        k=i
        while(k<25 and arr[k][j]!=''):
            arr[i][j] = arr[k][j]
            arr[k][j]=''
            k+=1
            i+=1
        r[m].sp=np.zeros((25,3))
        for j in range(0,3):
            movementLane(self.arr,25,j,r[m].sp)
        print(r[m].sp)

    def moveForward(self,arr,m,r):
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
            
            while(i<25 and arr[i][j]==''):
                i+=1
            k=i
            while(k<25 and arr[k][j]!=''):
                arr[i][j] = arr[k][j]
                arr[k][j]=''
                k+=1
                i+=1

            k = i
            i=0

            j+=1
        print(arr)
        r[m].sp=np.zeros((25,3))
        for j in range(0,3):
            movementLane(self.arr,25,j,r[m].sp)
        print(r[m].sp)
        return arr

    def lightGreen(self,i ,r):
        j=1
        scaling=10
        while(j<3):

            count=0
            k=0
            time2=0
            time =self.dur
            while(k<25 and r[i].x[k][j]!='' and time>0 and r[i].vehicles>=1):

                # time -= int(math.ceil(100/r[i].sp[k][j]))
                count+=1

                if(r[i].x[k][j]=='T1'or r[i].x[k][j]=='B1'):
                    n = k
                    while(n<(k+5)):
                        r[i].x[n][j] = ''
                        n+=1
                    k+=5

                elif(r[i].x[k][j]=='T21'or r[i].x[k][j]=='T22'):
                    n = k
                    while(n<(k+7)):
                        r[i].x[n][j] = ''
                        n+=1
                    k+=7

                elif(r[i].x[k][j]=='T31'or r[i].x[k][j]=='T32'):
                    n = k
                    while(n<(k+6)):
                        r[i].x[n][j] = ''
                        n+=1
                    k+=6
                            
                elif(r[i].x[k][j]=='C1' or r[i].x[k][j]=='E' or r[i].x[k][j]=='T4'):
                    n = k
                    while(n<(k+2)):
                        r[i].x[n][j] = ''
                        n+=1
                    k+=2
                                          
                elif(r[i].x[k][j]=='B2' or r[i].x[k][j]=='C2'):
                    n = k
                    while(n<(k+1)):
                        r[i].x[n][j] = ''
                        n+=1
                    k+=1
                time1= int(math.ceil(k*scaling/r[i].sp[k-1][j]))
                time2+=time1-time2
                time-=time2
                    
            print("\nTime taken by the lane ",j," is ",(self.dur-time))  
            print("\nTotal Vehicles that crossed the round about from this lane ",count)                            
            r[i].vehicles-=count
            j+=1
            print("count=",count)
        print("\n\t\tNew Arrangement for road ",(i+1),"\n")
        r[i].x=self.moveForward(r[i].x,i,r)
        
        
        
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
    print("left lane movement")
    i=0
    while(i<4):
        print("for road ",i+1)
        s[i].MoveLeft(p[i].x,p[i].sp,i,p)
        print(p[i].x)
        i+=1
    # print("\n\t\tWhen Signal is given Anticlockwise")
    # i=3
    # while(i>=0):                         # For Anti-Clockwise Signal behaviour
    #     print("\n\n\t\tSignal is Green for road ",(i+1),"\n")
    #     print(p[i].x,"\n")
    #     print(p[i].sp,"\n")
    #     s[i].lightGreen(i,p)
    #     s[i].light[i] = 'G'
    #     x = (i-1)%4
    #     s[i].light[x]='O'
    #     x = (i-2)%4
    #     s[i].light[x] = 'R'
    #     x = (i-3)%4
    #     s[i].light[x] = 'R'
    #     print("\n\tSignal was as follows :-",s[i].light)
    #     i-=1
