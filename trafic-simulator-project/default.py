from test import recording
import numpy as np
import os
import math
from time import sleep
# for files in os.listdir()
SIZE= 75
def inflow(road,file):
    i=0
    files=open(file,"r")
    while(i<4):
        
        print("\n\t\tEnter the details for road ",i+1)
        print("\n\tUnit of space occupied:- ")
        
        q=files.readline()
        space = int(files.readline())
        road[i].space+=space
        print(i)
        print(road[i].data)
        road[i].con = road[i].space / SIZE
        road[i].data=[0,0,0,0,0,0,0,0,0,0,0]
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
            ch = int(files.readline())
        
            if(ch == 1):

                print("\nEnter the number of trucks:- ")
                T1 = int(files.readline())
                road[i].data[0]=T1
                road[i].truck[2]=T1
                road[i].truck[3]=T1*5
                space-=road[i].data[0]*5

            elif(ch == 2):

                print("\nEnter the number of Unloaded Trollers:- ")
                T31 = int(files.readline())
                road[i].data[1]=T31
                road[i].utroller[2]=T31
                road[i].utroller[3]=T31*7
                space-=road[i].data[1]*7

            elif(ch == 3):

                print("\nEnter the number of Loaded Trollers:- ")
                T32 = int(files.readline())
                road[i].data[2]=T32
                road[i].ltroller[2]=T32
                road[i].ltroller[3]=T32*7
                space-=road[i].data[2]*7

            elif(ch == 4):

                print("\nEnter the number of Unloaded Tankers:- ")
                T21 = int(files.readline())
                road[i].data[3]=T21
                road[i].utanker[2]=T21
                road[i].utanker[3]=T21*6
                space-=road[i].data[3]*6

            elif(ch == 5):

                print("\nEnter the number of Loaded Tanker:- ")
                T22 = int(files.readline())
                road[i].data[4]=T22
                road[i].ltanker[2]=T22
                road[i].ltanker[3]=T22*6
                space-=road[i].data[4]*6

            elif(ch == 6):

                print("\nEnter the number of buses:- ")
                B1 = int(files.readline())
                road[i].data[5]=B1
                road[i].bus[2]=B1
                road[i].bus[3]=B1*5
                space-=road[i].data[5]*5
            
            elif(ch == 7):

                print("\nEnter the number of cars :- ")
                C1 = int(files.readline())
                road[i].data[6]=C1
                road[i].car[2]=C1
                road[i].car[3]=C1*2
                space-=road[i].data[6]*2
                    
            elif(ch == 8):

                print("\nEnter the number of E-rickshaw:- ")
                E = int(files.readline())
                road[i].data[7]=E
                road[i].erick[2]=E
                road[i].erick[3]=E*5
                space-=road[i].data[7]*2
                    
            elif(ch == 9):

                print("\nEnter the number of Tempos:- ")
                T4 = int(files.readline())
                road[i].data[8]=T4
                road[i].tempo[2]=T4
                road[i].tempo[3]=T4*2
                space-=road[i].data[8]*2
                
            elif(ch == 10):

                print("\nEnter the number of Bikes & scooty:- ")
                B2 = int(files.readline())
                road[i].data[9]=B2
                road[i].bike[2]=B2
                road[i].bike[3]=B2*5
                space-=road[i].data[9]*1
                    
            elif(ch == 11):

                print("\nEnter the number of Cycles:- ")
                C2 = int(files.readline())
                road[i].data[10]=C2
                road[i].cycle[2]=C2
                road[i].cycle[3]=C2*5
                space-=road[i].data[10]*1
       
        vehicles=0
        data=road[i].data
        print(road[i].data)
        sleep(3)
        j=0
        while(j<11):

            vehicles+=data[j]
            j+=1
        road[i].vehicles=vehicles
        i+=1
    files.close()

def takeDefault(road):
    time  = int(input("\nEnter time in 24hour format:- "))
    if(time>=6 and time<=10):
        Morning(road)
        return 8
    elif(time>=10 and time<=13):
        Noon(road)
        return 12
    elif(time>=13 and time<=17):
        Evening(road)
        return 15
    elif(time>=17 and time <=22):
        Night(road)
        return 20
    elif((time>=22 and time<=24) or (time >=1 and time<6)):
        Early(road)
        return 2

    
def Early(road):
    file = "test-cases/22-6a.txt"
    inflow(road,file)
    file1 = open("record.txt","a")
    file1.write("\n22-6")
    file1.close()
    recording(file)

def Morning(road):
    file= "test-cases/6-10a.txt"
    inflow(road,file)
    file1 = open("record.txt","a")
    file1.write("\n6-10")
    file1.close()
    recording(file)

def Noon(road):
    file="test-cases/10-13a.txt"
    inflow(road,file)
    file1 = open("record.txt","a")
    file1.write("\n10-13")
    file1.close()
    recording(file)

def Evening(road):
    file="test-cases/13-17a.txt"
    inflow(road,file)
    file1 = open("record.txt","a")
    file1.write("\n13-17")
    file1.close()
    recording(file)

def Night(road):
    file="test-cases/17-22a.txt"
    inflow(road,file)
    file1 = open("record.txt","a")
    file1.write("\n17-22")
    file1.close()
    recording(file)