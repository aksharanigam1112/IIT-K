import numpy as np
import math
"""import Signal"""
from Movement import arange, movementLeft, movementRight, movementStriaght

SIZE = 75

class road:
    x = np.chararray((25,3))

    def __init__(self, space, con,vehicles, data):
        self.space = space
        self.truck = [4,15,0,0]
        self.truck[2]=data[0]
        self.truck[3]=data[0]*self.truck[0]
        self.bus = [3,20,0,0]
        self.bus[2]=data[1]
        self.bus[3]=data[1]*self.bus[0]
        self.car = [2,30,0,0]
        self.car[2]=data[2]
        self.car[3]=data[2]*self.car[0]
        self.tempo = [2,25,0,0]
        self.tempo[2]=data[4]
        self.tempo[3]=data[4]*self.tempo[0]
        self.bike = [1,35,0,0]
        self.bike[2]=data[5]
        self.bike[3]=data[5]*self.bike[0]
        self.cycle = [1,10,0,0]
        self.cycle[2]=data[6]
        self.cycle[3]=data[6]*self.cycle[0]
        self.erick = [2,20,0,0]
        self.erick[2]=data[3]
        self.erick[3]=data[3]*self.erick[0]
        self.con = con
        self.vehicles=vehicles

        #light = 'G'

    def Display(self):

        if(self.truck[2] != 0):
            print("\nNo. of trucks = ",self.truck[2]," & space consumed = ",self.truck[3])
        
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
        
        self.vehicles = self.truck[2] + self.bus[2] + self.car[2] + self.tempo[2] + self.erick[2] + self.bike[2] + self.cycle[2]
        print("\nTotal Vehicles = ", self.vehicles)
        print("\nCongestion = ", self.con)

    """def calculateBenefit(self):
        
        ratio = []
        ratio[0] = road.truck[1] / road.truck[2]
        ratio[1] = road.bus[1] / road.bus[2]
        ratio[2] = road.car[1] / road.car[2]
        ratio[3] = road.tempo[1] / road.tempo[2]
        ratio[4] = road.erick[1] / road.erick[2]
        ratio[5] = road.cycle[1] / road.cycle[2]
        ratio[6] = road.bike[1] / road.bike[2]
        return ratio"""

def main():

    r = []
    for i in range(4):

        print("\n\t\tEnter the details for road ",i+1)
        print("\n\tUnit of space occupied:- ")
        space = int(input())
        con = space / SIZE
        data=[0,0,0,0,0,0,0]
        while(space > 0):
        
            print("\n\tTruck...1")
            print("\n\tBuses...2")
            print("\n\tCars...3")
            print("\n\tE-Rickshaw...4")
            print("\n\tTempo...5")
            print("\n\tBikes & Scooty...6")
            print("\n\tCycles...7")
            print("\nEnter your choice:- ")
            ch = int(input())
            
            if(ch == 1):
                print("\nEnter the number of trucks:- ")
                T = int(input())
                data[0]=T
                space-=data[0]*4

            elif(ch == 2):
                print("\nEnter the number of buses:- ")
                B = int(input())
                data[1]=B
                space-=data[1]*3

            elif(ch == 3):    
                print("\nEnter the number of cars :- ")
                C = int(input())
                data[2]=C
                space-=data[2]*2

            elif(ch == 4):
                print("\nEnter the number of E-rickshaw:- ")
                E = int(input())
                data[3]=E
                space-=data[3]*2

            elif(ch == 5):
                print("\nEnter the number of Tempos:- ")
                t = int(input())
                data[4]=t
                space-=data[4]*2

            elif(ch == 6):
                print("\nEnter the number of Bikes & scooty:- ")
                b = int(input())
                data[5]=b
                space-=data[5]*1

            elif(ch == 7):
                print("\nEnter the number of Cycles:- ")
                c = int(input())
                data[6]=c
                space-=data[6]*1
        vehicles=0
        for j in range(7):
            vehicles+=data[j]
        r.append(road(space,con,vehicles,data))
    
    for i in range(0,4):

        print("\n\n\t\tDetails for road ",i+1," are:- ")
        r[i].Display()


    print("\n\nEnter source & destination :- ")
    source = int(input())
    destination = int(input())
    
    print("\nEnter the total no. of psuedo-lanes (not more than 3):- ")
    l = int(input())
    
    print("\nTest 0")
    
    for i in range(4):
        
        print("\nTest 1")
        r[i].rows = math.ceil(r[i].vehicles/l)
        r[i].x[:] = ''
        
        print("\nTest 2")
        if(r[i].truck[2] > 0):
            arange(r[i].truck[2],'T',r[i].x,r[i].rows,l)
        
        print("\nTest 3")
        if(r[i].bus[2] > 0):
            arange(r[i].bus[2],'B',r[i].x,r[i].rows,l)
        
        print("\nTest 4")
        if(r[i].car[2] > 0):
            arange(r[i].car[2],'C',r[i].x,r[i].rows,l)
        
        print("\nTest 5")
        if(r[i].tempo[2] > 0):
            arange(r[i].tempo[2],'t',r[i].x,r[i].rows,l)
        
        print("\nTest 6")
        if(r[i].erick[2] > 0):
            arange(r[i].erick[2],'E',r[i].x,r[i].rows,l)
        
        print("\nTest 7")
        if(r[i].bike[2] > 0):
            arange(r[i].bike[2] , 'b', r[i].x , r[i].rows,l)
        
        print("\nTest 8")
        if(r[i].cycle[2] > 0):
            arange(r[i].cycle[2] , 'c', r[i].x , r[i].rows,l)

        print("\n\tarrangement of road ",i+1," is :- ")
        print(r[i].x)
    
    if((source==1 and destination==2) or (source==2 and destination==3) or (source==3 and destination==4) or (source==4 and destination==2)):
        movementLeft()
    
    if((source==1 and destination==3) or (source==2 and destination==4) or (source==3 and destination==1) or (source==4 and destination==2)):
        movementStriaght()
    
    if((source==1 and destination==4) or (source==2 and destination==1) or (source==3 and destination==2) or (source==4 and destination==3)):
        movementRight()

main()
