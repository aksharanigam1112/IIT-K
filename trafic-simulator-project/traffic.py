import random
from Movement import arange,movementLane
from Signal import mainSignal
from time import sleep
import numpy as np
import math
from datetime import datetime
from default import takeDefault,inflow
from test import recording

SIZE = 75

class MainWindow:

    def ButtonClick(self ,i , r, s):

        if(r[i].con>0.7):
            s.dur+=10

        elif(r[i].con<0.2):
            i=0
            x=0
            while(i<4):
                if(s[i].direction == "clockwise" and s.colour[i]=='O'):
                    s.colour[i] = 'G'
                    if(i>0):
                        x = (i-1)%4
                    else:
                        x=1
                    s.colour[x] = 'R'
                    x = (i+1)%4
                    s.colour[x] = 'O'
                elif(s[i].direction=="anticlockwise" and s.colour[i]=='O'):
                    s.colour[i] = 'G'
                    x = (i+1)%4
                    s.colour[x] = 'R'
                    if(i>0):
                        x = (i-1)%4
                    else:
                        x = 3
                    s.colour[x] = 'O'

                i+=1

class vehicle:

    def __init__(self,type,space):
            self.type = type
            self.space=space

    def direction(self):
        dir = ['L', 'S', 'R']
        i=random.randint(0,2)
        return dir[i]

class road:

    def __init__(self, space, con,vehicles, data):

        self.x = np.chararray((25,3),itemsize = 6 , unicode=True)
        self.sp=np.zeros((25,3))
        
        self.data=[0,0,0,0,0,0,0,0,0,0,0]

        self.space = space

        self.truck = [5,15,0,0]

        self.utroller = [7,15,0,0]

        self.ltroller = [7,10,0,0]

        self.utanker = [6,20,0,0]

        self.ltanker = [6,10,0,0]

        self.bus = [5,20,0,0]

        self.car = [2,30,0,0]

        self.erick = [2,20,0,0]

        self.tempo = [2,25,0,0]

        self.bike = [1,35,0,0]

        self.cycle = [1,10,0,0]
        
        self.con = con
        self.vehicles=vehicles
        self.unplaced=[]
        self.waitL=[]
        self.waitS=[]
        self.waitR=[]
        
        # i=0
        # while(i<11):
        #     j=0
        #     while(j<data[i]):
        #         self.unplaced.append(i)
        #         j+=1
        #     i+=1
        
        # random.shuffle(self.unplaced)

    # @classmethod
    # def defaultConst(self):
    #     pass

    def Display(self):

        if(self.truck[2] != 0):
            print("\nNo. of trucks = ",self.truck[2]," & space consumed = ",self.truck[3])

        if(self.utroller[2] != 0):
            print("\nNo. of unloaded trollers = ",self.utroller[2]," & space consumed = ",self.utroller[3])
        
        if(self.ltroller[2] != 0):
            print("\nNo. of loaded trollers = ",self.ltroller[2]," & space consumed = ",self.ltroller[3])

        if(self.utanker[2] != 0):
            print("\nNo. of unloaded tankers = ",self.utanker[2]," & space consumed = ",self.utanker[3])
        
        if(self.ltanker[2] != 0):
            print("\nNo. of loaded tankers = ",self.ltanker[2]," & space consumed = ",self.ltanker[3])
        
        if(self.bus[2] != 0):
            print("\nNo. of buses = ",self.bus[2]," & space consumed = ",self.bus[3])
        
        if(self.car[2] != 0):
            print("\nNo. of cars = ",self.car[2]," & space consumed = ",self.car[3])
        
        if(self.tempo[2] != 0):
            print("\nNo. of tempo = ",self.tempo[2]," & space consumed = ",self.tempo[3])
        
        if(self.erick[2] != 0):
            print("\nNo. of erickshaw = ",self.erick[2]," & space consumed = ",self.erick[3])
        
        if(self.bike[2] != 0):
            print("\nNo. of bikes & scooties = ",self.bike[2]," & space consumed = ",self.bike[3])
        
        if(self.cycle[2] !=0):
            print("\nNo. of cycles = ",self.cycle[2]," & space consumed = ",self.cycle[3])  
        
        self.vehicles = self.truck[2]+self.ltroller[2]+self.utroller[2]+self.ltanker[2]+self.utanker[2]+self.bus[2]+self.car[2]+self.tempo[2]+self.erick[2]+self.bike[2]+self.cycle[2]
        self.space = self.truck[3]+self.ltroller[3]+self.utroller[3]+self.ltanker[3]+self.utanker[3]+self.bus[3]+self.car[3]+self.tempo[3]+self.erick[3]+self.bike[3]+self.cycle[3]
        self.con = self.space / SIZE
        print("\nTotal Vehicles = ", self.vehicles)
        print("\nCongestion = ", self.con)
        #print(self.unplaced)

    def fillGap(self , arr , i , j):
        while(i<24 and arr[i+1][j]!=''):
            arr[i][j] = arr[i+1][j]
            i+=1
        arr[i][j]=''
    
    def countveh(self):
        j=0
        k=0
        self.truck[2]=0
        self.truck[3]=0
        self.utroller[2]=0
        self.utroller[3]=0
        self.ltroller[2]=0
        self.ltroller[3]=0
        self.utanker[2]=0
        self.utanker[3]=0
        self.ltanker[2]=0
        self.ltanker[3]=0
        self.bus[2]=0
        self.bus[3]=0
        self.car[2]=0
        self.car[3]=0
        self.erick[2]=0
        self.erick[3]=0
        self.tempo[2]=0
        self.tempo[3]=0
        self.bike[2]=0
        self.bike[3]=0
        self.cycle[2]=0
        self.cycle[3]=0
        while(k<3):
            j=0
            # print("test3")
            while(j<25 and self.x[j][k]!=''):
                # print("j=",j)
                print(self.x[j][k])
                if(self.x[j][k]=='T1'):
                    self.truck[2]+=1
                    self.truck[3]+=self.truck[0]
                    j+=self.truck[0]
                elif(self.x[j][k]=='T31'):
                    self.utroller[2]+=1
                    self.utroller[3]+=self.utroller[0]
                    j+=self.utroller[0]
                elif(self.x[j][k]=='T32'):
                    self.ltroller[2]+=1
                    self.ltroller[3]+=self.ltroller[0]
                    j+=self.ltroller[0]
                elif(self.x[j][k]=='T21'):
                    self.utanker[2]+=1
                    self.utanker[3]+=self.utanker[0]
                    j+=self.utanker[0]
                elif(self.x[j][k]=='T22'):
                    self.ltanker[2]+=1
                    self.ltanker[3]+=self.ltanker[0]
                    j+=self.ltanker[0]
                elif(self.x[j][k]=='B1'):
                    self.bus[2]+=1
                    self.bus[3]+=self.bus[0]
                    j+=self.bus[0]
                elif(self.x[j][k]=='C1'):
                    self.car[2]+=1
                    self.car[3]+=self.car[0]
                    j+=self.car[0]
                elif(self.x[j][k]=='T4'):
                    self.tempo[2]+=1
                    self.tempo[3]+=self.tempo[0]
                    j+=self.tempo[0]
                elif(self.x[j][k]=='E'):
                    self.erick[2]+=1
                    self.erick[3]+=self.erick[0]
                    j+=self.erick[0]
                elif(self.x[j][k]=='B2'):
                    self.bike[2]+=1
                    self.bike[3]+=self.bike[0]
                    j+=self.bike[0]
                elif(self.x[j][k]=='C2'):
                    self.cycle[2]+=1
                    self.cycle[3]+=self.cycle[0]
                    j+=self.cycle[0]
                elif(self.x[j][k]=='C2C2'):
                    self.cycle[2]+=2
                    self.cycle[3]+=self.cycle[0]
                    j+=self.cycle[0]
                elif(self.x[j][k]=='C2C2C2'):
                    self.cycle[2]+=3
                    self.cycle[3]+=self.cycle[0]
                    j+=self.cycle[0]
                elif(self.x[j][k]=='B2B2'):
                    self.bike[2]+=2
                    self.bike[3]+=self.bike[0]
                    j+=self.bike[0]
                elif(self.x[j][k]=='B2C2' or self.x[j][k]=='C2B2'):
                    self.bike[2]+=1
                    self.bike[3]+=self.bike[0]
                    self.cycle[2]+=1
                    # self.cycle[3]+=self.cycle[0]
                    j+=self.bike[0]
                # else:
                #     j=25
            k+=1
        self.vehicles=self.truck[2]+self.utroller[2]+self.ltroller[2]+self.utanker[2]+self.ltanker[2]+self.bus[2]+self.car[2]+self.tempo[2]+self.erick[2]+self.bike[2]+self.cycle[2]
        self.space=self.truck[3]+self.utroller[3]+self.ltroller[3]+self.utanker[3]+self.ltanker[3]+self.bus[3]+self.car[3]+self.tempo[3]+self.erick[3]+self.bike[3]+self.cycle[3]
        self.con = self.space / SIZE
        self.Display()

    def Merge(self):       
        j=0
        while(j<3):
            i=0
            while(i<25 and self.x[i][j]!=''):

                if(i<24 and self.x[i][j] != '' and self.x[i][j]=='B2' and (self.x[i+1][j] =='B2' or self.x[i+1][j]=='C2')):
                    self.x[i][j] += self.x[i+1][j]
                    self.x[i+1][j] = ''
                    self.fillGap( self.x , i+1 , j ) 
                    i+=1
                
                elif(i<24 and self.x[i][j] != '' and self.x[i][j]=='C2' and (self.x[i+1][j] =='B2' or self.x[i+1][j]=='C2')):
                    self.x[i][j] += self.x[i+1][j]
                    self.x[i+1][j] = ''
                    self.fillGap( self.x , i+1 , j ) 
                    i+=1

                elif(i<23 and self.x[i][j] != '' and self.x[i][j]=='C2' and self.x[i+1][j]=='C2' and self.x[i+2][j]=='C2'):
                    self.x[i][j] += self.x[i+1][j] + self.x[i+2][j]
                    self.x[i+1][j] =''
                    self.x[i+2][j] =''
                    self.fillGap(self.x , i+2 , j)
                    self.fillGap(self.x , i+1 , j)
                    i+=1 

                else:
                    i+=1
            j+=1
def getvehicle(v,wait,dir,rows,i):
    k=0
    veh=0
    sp=0
    for j in wait:
        flag=True
        if(j==0):
            v.append(vehicle("T1",5))
            if(dir=="N"):
                dir=v[k].direction()
            else:
                pass
            flag=arange(r,j,"T1",5,r[i].x,rows,dir,i)
            if(flag==False):
                if(flag==False):
                    if(dir=='L'):
                        r[i].waitL.append(j)
                    elif(dir=='S'):
                        r[i].waitS.append(j)
                    else:
                        r[i].waitR.append(j)
                    # r[i].truck[2]-=1
                    # r[i].truck[3]-=5
            else:
                sp +=5
                veh+=1
        elif(j==1):
            v.append(vehicle("T31",7))
            if(dir=="N"):
                dir=v[k].direction()
            else:
                pass
            flag=arange(r,j,"T31",7,r[i].x,rows,dir,i)
            if(flag==False):
                if(dir=='L'):
                    r[i].waitL.append(j)
                elif(dir=='S'):
                    r[i].waitS.append(j)
                else:
                    r[i].waitR.append(j)
                # r[i].utroller[2]-=1
                # r[i].utroller[3]-=7
            else:
                sp +=7
                veh+=1
                    
        elif(j==2):
            v.append(vehicle("T32",7))
            if(dir=="N"):
                dir=v[k].direction()
            else:
                pass
            flag=arange(r,j,"T32",7,r[i].x,rows,dir,i)
            if(flag==False):
                if(dir=='L'):
                    r[i].waitL.append(j)
                elif(dir=='S'):
                    r[i].waitS.append(j)
                else:
                    r[i].waitR.append(j)
                # r[i].ltroller[2]-=1
                # r[i].ltroller[3]-=7
            else:
                sp +=7
                veh+=1

        elif(j==3):
            v.append(vehicle("T21",6))
            if(dir=="N"):
                dir=v[k].direction()
            else:
                pass
            flag=arange(r,j,"T21",6,r[i].x,rows,dir,i)
            if(flag==False):
                if(dir=='L'):
                    r[i].waitL.append(j)
                elif(dir=='S'):
                    r[i].waitS.append(j)
                else:
                    r[i].waitR.append(j)
                # r[i].utanker[2]-=1
                # r[i].utanker[3]-=6
            else:
                sp +=6
                veh+=1
                    
        elif(j==4):
            v.append(vehicle("T22",6))
            if(dir=="N"):
                dir=v[k].direction()
            else:
                pass
            flag=arange(r,j,"T22",6,r[i].x,rows,dir,i)
            if(flag==False):
                if(dir=='L'):
                    r[i].waitL.append(j)
                elif(dir=='S'):
                    r[i].waitS.append(j)
                else:
                    r[i].waitR.append(j)
                # r[i].ltanker[2]-=1
                # r[i].ltanker[3]-=6
            else:
                sp +=6
                veh+=1
                    
        elif(j==5):
            v.append(vehicle("B1",5))
            if(dir=="N"):
                dir=v[k].direction()
            else:
                pass
            flag=arange(r,j,"B1",5,r[i].x,rows,dir,i)
            if(flag==False):
                if(dir=='L'):
                    r[i].waitL.append(j)
                elif(dir=='S'):
                    r[i].waitS.append(j)
                else:
                    r[i].waitR.append(j)
                # r[i].bus[2]-=1
                # r[i].bus[3]-=5
            else:
                sp +=5
                veh+=1
                    
        elif(j==6):
            v.append(vehicle("C1",2))
            if(dir=="N"):
                dir=v[k].direction()
            else:
                pass
            flag=arange(r,j,'C1',2,r[i].x,rows,dir,i)
            if(flag==False):
                if(dir=='L'):
                    r[i].waitL.append(j)
                elif(dir=='S'):
                    r[i].waitS.append(j)
                else:
                    r[i].waitR.append(j)
                # r[i].car[2]-=1
                # r[i].car[3]-=2
            else:
                sp +=2
                veh+=1
                    
        elif(j==7):
            v.append(vehicle("T4",2))
            if(dir=="N"):
                dir=v[k].direction()
            else:
                pass
            flag=arange(r,j,"T4",2,r[i].x,rows,dir,i)
            if(flag==False):
                if(dir=='L'):
                    r[i].waitL.append(j)
                elif(dir=='S'):
                    r[i].waitS.append(j)
                else:
                    r[i].waitR.append(j)
                # r[i].tempo[2]-=1
                # r[i].tempo[3]-=2
            else:
                sp +=2
                veh+=1
                    
        elif(j==8):
            v.append(vehicle("E",2))
            if(dir=="N"):
                dir=v[k].direction()
            else:
                pass
            flag=arange(r,j,"E",2,r[i].x,rows,dir,i)
            if(flag==False):
                if(dir=='L'):
                    r[i].waitL.append(j)
                elif(dir=='S'):
                    r[i].waitS.append(j)
                else:
                    r[i].waitR.append(j)
                # r[i].erick[2]-=1
                # r[i].erick[3]-=2
            else:
                sp +=2
                veh+=1
                
        elif(j==9):
            v.append(vehicle("B2",1))
            if(dir=="N"):
                dir=v[k].direction()
            else:
                pass
            flag=arange(r,j,"B2",1,r[i].x,rows,dir,i)
            if(flag==False):
                if(dir=='L'):
                    r[i].waitL.append(j)
                elif(dir=='S'):
                    r[i].waitS.append(j)
                else:
                    r[i].waitR.append(j)
                # r[i].bike[2]-=1
                # r[i].bike[3]-=1
            else:
                sp +=1
                veh+=1
                    
        elif(j==10):
            v.append(vehicle("C2",1))
            if(dir=="N"):
                dir=v[k].direction()
            else:
                pass
            flag=arange(r,j,"C2",1,r[i].x,rows,dir,i)
            if(flag==False):
                if(dir=='L'):
                    r[i].waitL.append(j)
                elif(dir=='S'):
                    r[i].waitS.append(j)
                else:
                    r[i].waitR.append(j)
                # r[i].cycle[2]-=1
                # r[i].cycle[3]-=1
            else:
                sp +=1
                veh+=1
        else:
            pass
        k+=1
    # print("test2")
    # r[i].countveh()
    # r[i].vehicles=r[i].truck[2]+r[i].utroller[2]+r[i].ltroller[2]+r[i].utanker[2]+r[i].ltanker[2]+r[i].bus[2]+r[i].car[2]+r[i].tempo[2]+r[i].erick[2]+r[i].bike[2]+r[i].cycle[2]
    # r[i].space=r[i].truck[3]+r[i].utroller[3]+r[i].ltroller[3]+r[i].utanker[3]+r[i].ltanker[3]+r[i].bus[3]+r[i].car[3]+r[i].tempo[3]+r[i].erick[3]+r[i].bike[3]+r[i].cycle[3]
    # r[i].con = r[i].space / SIZE

def userInput():
    print("\n\tEnter the values in following format:- ")
    print("\n1) Write the word \'Road\' before the beginning of a new road followed by the space consumed by vehicles")
    print("\nTruck...1")                  #T1
    print("\nUnloaded Troller...2")       #T31
    print("\nLoaded Troller...3")         #T32
    print("\nUnloaded Tanker...4")        #T21
    print("\nLoaded Tanker...5")          #T22
    print("\nBuses...6")                  #B1
    print("\nCars...7")                   #C1
    print("\nE-Rickshaw...8")             #E
    print("\nTempo...9")                  #T4
    print("\nBikes & Scooty...10")        #B2
    print("\nCycles...11")                #C2
    print("\n2) The first number gives the vehicle value and the number followed tells the quantity of that vehicle consumed on a road")
    print("\n\nStart Entering:- ")

    file = open("user-input.txt","w")
    x = input()
    while(len(x)>0):
        file.write(x)
        file.write("\n")
        x = input()
    file.close()

    file = open("user-input.txt","r+")
    for x in file:
        if(x=='\n'):
            x = x.replace(x,"")
    file.close()    
    
    return ("user-input.txt")

def main():
    # print("in main")
    now = datetime.now()
    current_time = now.strftime("%H")
    time=int(current_time)
    ch=0
    print("\nEnter the values ... 1")
    print("\nTake Default values...2")
    print("\nTo terminate ...0")
    ch = int(input("\nEnter your choice"))
    if(ch==1):
        file = open("record.txt","a")
        file.write("\n")
        file.write(str(current_time))
        file.close()
        file2 = userInput()
        inflow(r,file2)
        recording(file2)
    elif(ch==2):
        time=takeDefault(r)
    else:
        print("Hope you liked it")
        quit()
    # print("place r[i].data into r[i].unplaced and shuffle it")
    a=0
    i=0
    while(a<4):
        i=0
        while(i<11):
            j=0
            while(j<r[a].data[i]):
                print("a=",a," j=",j," i=",i)
                r[a].unplaced.append(i)
                j+=1
            random.shuffle(r[a].unplaced)
            i+=1
        a+=1
    # print("parse r[i].unplaced and pop the 0th index and give that a direction using vehicle class")
    i=0 
    while(i<4):

        print("\n\n\t\tDetails for road ",i+1," are:- ")
        r[i].Display()
        i+=1

    i=0
    while(i<4):
            
        rows =24
        v=[]
        k=0
        print("arrange left waiting")
        wait=r[i].waitL
        r[i].waitL=[]
        # print(wait)
        sleep(2)
        # print("test")
        getvehicle(v,wait,"L",rows,i)
        print("arrange straight waiting")
        wait=r[i].waitS
        r[i].waitS=[]
        # print(wait)
        sleep(2)
        getvehicle(v,wait,"S",rows,i)
        print("arrange right waiting")
        wait=r[i].waitR
        r[i].waitR=[]
        # print(wait)
        sleep(2)
        getvehicle(v,wait,"R",rows,i)
        # if(r[i].waitL.__len__()==0 and r[i].waitS.__len__()==0 and r[i].waitR.__len__()==0):
        print("arranging new")
        getvehicle(v,r[i].unplaced,"N",rows,i)
                
        print("\n\tArrangement of road ",i+1," is :- ")
        print(r[i].x)
        r[i].Merge()
        print("\n\t After Merging Bikes & Cycles :- \n" , r[i].x)
        # r[i].countveh()
        i+=1
    i=0
    while(i<4):

        print("\n\tFor road ",(i+1))

        j=0
        while(j<3):

            if(j==0):
                print("\n\t\tFor Lane Moving Left")
            elif(j==1):
                print("\n\t\tFor Lane Moving Straight")
            elif(j==2):
                print("\n\t\tFor Lane Moving Right")

            movementLane(r[i].x,rows ,j,r[i].sp)
            j+=1
        # r[i].countveh()
        i+=1
    mainSignal(r,time)
    i=0
    while(i<4):
        print("for road ",i+1)
        r[i].countveh()
        print(r[i].x)
        i+=1
    # print("sp successfully defined")
    # print("traffic moved successfully")
    # print("to continue press y")
    # cv=input()
    # if(cv=='y'):ice"))
    sleep(5)
    main()
r=[]
data=[0,0,0,0,0,0,0,0,0,0,0]
vehicles=0
con=0
space=0
i=0
while(i<4):
    r.append(road(space,con,vehicles,data))
    i+=1
main()