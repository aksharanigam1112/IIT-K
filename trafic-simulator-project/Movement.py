import numpy as np
import random

x = np.chararray((25,3), itemsize = 3 ,unicode =True)
x[:] = ''

def arange( ch, space, x, rows, col,dir):

    i = 0
    if(dir=='L'):
        j=0
    elif(dir=='S'):
        j=1
    elif(dir=='R'):
        j=2
    while(x[i][j]!='' and rows-i>=space):
        i+=1
        pass
    if(rows-i<space and j!=1):
        j=1
    elif(rows-i>=space):
        while(space>0):
            x[i][j]=ch
            i+=1
            space-=1
    else:
        j=2
    

def movementLeft():

    print("\n\n\t\t If 1st Row th vehicle moves left")
    print("\nJaam Causing Hindrances will occur in:- ")
    print("\n1 2 3")
    print("\nL R S")
    print("\nL S L")
    print("\n No Hinderances will occur in:- ")
    print("\n1 2 3")
    print("\nL S R")
    print("\nL R R")
    print("\nL S S")
    print("\nL L S")
    print("\nL L L")
                        
def movementRight():

    print("\n\n\t\t If 1st Row th vehicle moves right")
    print("\nJaam Causing Hindrances will occur in:- ")
    print("\n1 2 3")
    print("\nR S R")
    print("\nR R S")
    print("\nR S L")
    print("\nR L S")
    print("\nR L L")
    print("\n no Hinderances will occur in:- ")
    print("\n1 2 3")
    print("\nR R R")
    print("\nR S S")

def movementStraight():

    print("\n\n\t\t If 1st Row th vehicle moves straight")
    print("\nJaam Causing Hindrances will occur in:- ")
    print("\n1 2 3")
    print("\nS R S")
    print("\nS R R")
    print("\nS L L")
    print("\nS L S")
    print("\nS S L")
    print("\n No Hinderances will occur in:- ")
    print("\n1 2 3")
    print("\nS S S")
    print("\nS S R")
    print("\nS R R")

def movementLane(arr , rows , j):

    i=0
    speed =0
    while(i<rows):

        #For Cycle , Loaded Tanker & Loaded Troller

        if(arr[i][j]=='C2' or arr[i][j]=='T22' or arr[i][j]=='T32'):     
            i=rows
            speed =10
            print("\nTill the end the lane moves with the speed of ",speed)
        
        #For Truck & Unloaded Troller

        elif (arr[i][j]=='T1' or arr[i][j]=='T31'):
            i+=1
            while(i<rows):
                if(arr[i][j]=='C2' or arr[i][j]=='T22' or arr[i][j]=='T32'):
                    speed = 15
                    print("\nTill ",i-1," the lane moves with the speed of ",speed)
                    break
                i+=1
            if(i==rows):
                speed = 15
            	print("\nTill end the lane moves with the speed of ",speed)
        
        #For Bus , E-rickshaw & Loaded Tanker

        elif(arr[i][j]=='B1' or arr[i][j]=='E' or arr[i][j]=='T21'):
            i+=1
            while(i<rows):
                if(arr[i][j]=='C2' or arr[i][j]=='T22' or arr[i][j]=='T32' or arr[i][j]=='C2' or arr[i][j]=='T22' or arr[i][j]=='T32'):
                    speed = 20
                    print("\nTill ",i-1," the lane moves with the speed of ",speed)
                    break
                i+=1
            if(i==rows):
                speed = 20
            	print("\nTill end the lane moves with the speed of ",speed)
        
        #For Tempo

        elif(arr[i][j]=='T4'):
            i+=1
            while(i<rows):
                if(arr[i][j]=='C2' or arr[i][j]=='T22' or arr[i][j]=='T32' or arr[i][j]=='C2' or arr[i][j]=='T22' or arr[i][j]=='T32' or arr[i][j]=='B1' or arr[i][j]=='E' or arr[i][j]=='T21'):
                    speed = 25
                    print("\nTill ",i-1," the lane moves with the speed of ",speed)
                    break
                i+=1
            if(i==rows):
                speed = 25
            	print("\nTill end the lane moves with the speed of ",speed)
        
        #For Car

        elif(arr[i][j]=='C1'):
            i+=1
            while(i<rows):
                if(arr[i][j]=='C2' or arr[i][j]=='T22' or arr[i][j]=='T32' or arr[i][j]=='C2' or arr[i][j]=='T22' or arr[i][j]=='T32' or arr[i][j]=='B1' or arr[i][j]=='E' or arr[i][j]=='T21' or arr[i][j]=='T4'):
                    speed = 30
                    print("\nTill ",i-1," the lane moves with the speed of ",speed)
                    break
                i+=1
            if(i==rows):
                speed = 30
            	print("\nTill end the lane moves with the speed of ",speed)
        
        #For Bike
        
        elif(arr[i][j]=='B2'):
            i+=1
            while(i<rows):
                if(arr[i][j]=='C2' or arr[i][j]=='T22' or arr[i][j]=='T32' or arr[i][j]=='C2' or arr[i][j]=='T22' or arr[i][j]=='T32' or arr[i][j]=='B1' or arr[i][j]=='E' or arr[i][j]=='T21' or arr[i][j]=='T4' or arr[i][j]=='B2'):
                    speed = 35
                    print("\nTill ",i-1," the lane moves with the speed of ",speed)
                    break
                i+=1
            if(i==rows):
                speed = 35
            	print("\nTill end the lane moves with the speed of ",speed)
        else:
            i+=1

    # while(i<rows):

    #     if(arr[i][j]=='T'):
    #         i+=1
    #         while(i<rows):
    #             if(arr[i][j]=='c'):
    #                 print("\nTill ",i-1," the lane moves with the speed of Truck that is 15")
    #                 break
    #             i+=1
    #         if(i==rows):
    #         	print("\nTill end the lane moves with the speed of Truck that is 15")
        
    #     elif(arr[i][j]=='B' or arr[i][j]=='E'):
    #         pos = i
    #         i+=1
    #         while(i<rows):
    #             if(arr[i][j]=='c' or arr[i][j] == 'T'):
    #                 if(arr[pos][j]=='B'):
    #                     print("\nTill ",i-1," the lane moves with the speed of Bus that is 20")
    #                 else:
    #                      print("\nTill ",i-1," the lane moves with the speed of E-rickshaw that is 20")
    #                 break
    #             i+=1
    #         if(i==rows):
    #         	print("\nTill end the lane moves with the speed of Bus/E-rickshaw that is 20")
            
    #     elif(arr[i][j]=='C'):
    #         i+=1
    #         while(i<rows):
    #             if(arr[i][j]!='C' and arr[i][j]!='b'):
    #                 print("\nTill ",i-1," the lane moves with the speed of Car that is 30")
    #                 break
    #             i+=1
    #         if(i==rows):
    #         	print("\nTill end the lane moves with the speed of Car that is 30")
        
    #     elif(arr[i][j]=='b'):
    #         i+=1
    #         while(i<rows):
    #             if(arr[i][j]!='b'):
    #                 print("\nTill ",i-1," the lane moves with the speed of Bike that is 35")
    #                 break
    #             i+=1
    #         if(i==rows):
    #         	print("\nTill end the lane moves with the speed of bike that is 35")
        
    #     elif(arr[i][j]=='c'):
    #         i=rows
    #         print("\nTill the end the lane moves with the speed of a cycle that is 10")
            
    
    #     else:
    #         i+=1
