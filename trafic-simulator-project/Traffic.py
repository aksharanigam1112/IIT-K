import numpy as np
import math
import random
from Signal import mainSignal
from Movement import arange,  movementLane
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


        self.space = space

        self.truck = [5,15,0,0]
        self.truck[2]=data[0]
        self.truck[3]=data[0]*self.truck[0]

        self.utroller = [7,15,0,0]
        self.utroller[2] = data[1]
        self.utroller[3] = data[1]*self.utroller[0]

        self.ltroller = [7,10,0,0]
        self.ltroller[2] = data[2]
        self.ltroller[3] = data[2]*self.utroller[0]

        self.utanker = [6,20,0,0]
        self.utanker[2] = data[3]
        self.utanker[3] = data[3]*self.utanker[0]

        self.ltanker = [6,10,0,0]
        self.ltanker[2] = data[4]
        self.ltanker[3] = data[4]*self.ltanker[0]

        self.bus = [5,20,0,0]
        self.bus[2]=data[5]
        self.bus[3]=data[5]*self.bus[0]

        self.car = [2,30,0,0]
        self.car[2]=data[6]
        self.car[3]=data[6]*self.car[0]

        self.erick = [2,20,0,0]
        self.erick[2]=data[7]
        self.erick[3]=data[7]*self.erick[0]

        self.tempo = [2,25,0,0]
        self.tempo[2]=data[8]
        self.tempo[3]=data[8]*self.tempo[0]

        self.bike = [1,35,0,0]
        self.bike[2]=data[9]
        self.bike[3]=data[9]*self.bike[0]

        self.cycle = [1,10,0,0]
        self.cycle[2]=data[10]
        self.cycle[3]=data[10]*self.cycle[0]
        
        self.con = con
        self.vehicles=vehicles
        self.unplaced=[]
        
        i=0
        while(i<11):
            j=0
            while(j<data[i]):
                self.unplaced.append(i)
                j+=1
            i+=1
        
        random.shuffle(self.unplaced)

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
        print("\nTotal Vehicles = ", self.vehicles)
        print("\nCongestion = ", self.con)
        #print(self.unplaced)

    def fillGap(self , arr , i , j):
        while(i<24 and arr[i+1][j]!=''):
            arr[i][j] = arr[i+1][j]
            i+=1
        arr[i][j]=''
    
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

        
def main():

    r = []
    i=0
    while(i<4):

        print("\n\t\tEnter the details for road ",i+1)
        print("\n\tUnit of space occupied:- ")
        space = int(input())
        con = space / SIZE
        data=[0,0,0,0,0,0,0,0,0,0,0]
        while(space > 0):

            print("\n\tTruck...1")                  #T1
            print("\n\tUnloaded Troller...2")       #T31
            print("\n\tLoaded Troller...3")         #T32
            print("\n\tUnloaded Tanker...4")        #T21
            print("\n\tLoaded Tanker...5")          #T22
            print("\n\tBuses...6")                  #B1
            print("\n\tCars...7")                   #C1
            print("\n\tE-Rickshaw...8")             #E
            print("\n\tTempo...9")                  #T4
            print("\n\tBikes & Scooty...10")        #B2
            print("\n\tCycles...11")                #C2
            print("\nEnter your choice:- ")
            ch = int(input())

            if(ch == 1):

                print("\nEnter the number of trucks:- ")
                T1 = int(input())
                data[0]=T1
                space-=data[0]*5

            elif(ch == 2):

                print("\nEnter the number of Unloaded Trollers:- ")
                T31 = int(input())
                data[1]=T31
                space-=data[1]*7

            elif(ch == 3):

                print("\nEnter the number of Loaded Trollers:- ")
                T32 = int(input())
                data[2]=T32
                space-=data[2]*7

            elif(ch == 4):

                print("\nEnter the number of Unloaded Tankers:- ")
                T21 = int(input())
                data[3]=T21
                space-=data[3]*6

            elif(ch == 5):

                print("\nEnter the number of Loaded Tanker:- ")
                T22 = int(input())
                data[4]=T22
                space-=data[4]*6

            elif(ch == 6):

                print("\nEnter the number of buses:- ")
                B1 = int(input())
                data[5]=B1
                space-=data[5]*5
        
            elif(ch == 7):

                print("\nEnter the number of cars :- ")
                C1 = int(input())
                data[6]=C1
                space-=data[6]*2
                
            elif(ch == 8):

                print("\nEnter the number of E-rickshaw:- ")
                E = int(input())
                data[7]=E
                space-=data[7]*2
                
            elif(ch == 9):

                print("\nEnter the number of Tempos:- ")
                T4 = int(input())
                data[8]=T4
                space-=data[8]*2
               
            elif(ch == 10):

                print("\nEnter the number of Bikes & scooty:- ")
                B2 = int(input())
                data[9]=B2
                space-=data[9]*1
                
            elif(ch == 11):

                print("\nEnter the number of Cycles:- ")
                C2 = int(input())
                data[10]=C2
                space-=data[10]*1
                
        vehicles=0
        j=0
        while(j<11):

            vehicles+=data[j]
            j+=1
        
        r.append(road(space,con,vehicles,data))
        i+=1
    
    i=0 
    while(i<4):

        print("\n\n\t\tDetails for road ",i+1," are:- ")
        r[i].Display()
        i+=1

    # print("\n\nEnter source & destination :- ")
    # source = int(input())
    # destination = int(input())
    
    # print("\nEnter the total no. of psuedo-lanes (not more than 3):- ")
    # l = int(input())
    # mainSiganl(r
    i=0
    while(i<4):
        
        rows =24
        r[i].x[:] = ''
        v=[]
        k=0
        for j in r[i].unplaced:
            if(j==0):
                v.append(vehicle("T1",5))
                dir=v[k].direction()
                arange("T1",5,r[i].x,rows,dir)

            elif(j==1):
                v.append(vehicle("T31",6))
                dir=v[k].direction()
                arange("T31",7,r[i].x,rows,dir)
            
            elif(j==2):
                v.append(vehicle("T32",6))
                dir=v[k].direction()
                arange("T32",7,r[i].x,rows,dir)

            elif(j==3):
                v.append(vehicle("T21",7))
                dir=v[k].direction()
                arange("T21",6,r[i].x,rows,dir)
            
            elif(j==4):
                v.append(vehicle("T22",7))
                dir=v[k].direction()
                arange("T22",6,r[i].x,rows,dir)
            
            elif(j==5):
                v.append(vehicle("B1",5))
                dir=v[k].direction()
                arange("B1",5,r[i].x,rows,dir)
            
            elif(j==6):
                v.append(vehicle("C1",2))
                dir=v[k].direction()
                arange('C1',2,r[i].x,rows,dir)
            
            elif(j==7):
                v.append(vehicle("T4",2))
                dir=v[k].direction()
                arange("T4",2,r[i].x,rows,dir)
            
            elif(j==8):
                v.append(vehicle("E",2))
                dir=v[k].direction()
                arange("E",2,r[i].x,rows,dir)
        
            elif(j==9):
                v.append(vehicle("B2",1))
                dir=v[k].direction()
                arange("B2",1,r[i].x,rows,dir)
            
            elif(j==10):
                v.append(vehicle("C2",1))
                dir=v[k].direction()
                arange("C2",1,r[i].x,rows,dir)

            else:
                pass
            k+=1
            
        print("\n\tArrangement of road ",i+1," is :- ")
        print(r[i].x)
        r[i].Merge()
        print("\n\t After Merging Bikes & Cycles :- \n" , r[i].x)
        i+=1
    
    
    # if((source==1 and destination==2) or (source==2 and destination==3) or (source==3 and destination==4) or (source==4 and destination==2)):

    #     movementLeft()
    
    # if((source==1 and destination==3) or (source==2 and destination==4) or (source==3 and destination==1) or (source==4 and destination==2)):

    #     movementStraight()
    
    # if((source==1 and destination==4) or (source==2 and destination==1) or (source==3 and destination==2) or (source==4 and destination==3)):

    #     movementRight()
    
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
        i+=1
    mainSignal(r)
main()
