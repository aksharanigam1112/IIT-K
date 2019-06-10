import numpy as np
import random

def arange( ch, space, x, rows, col,dir):

    i = 0
    i1=0
    i2=0
    i3=0
    flag=1
    while(i<25):
        if(x[i][0]=='' and flag%2!=0):
            i1=i
            flag*=2
        if(x[i][1]=='' and flag%3!=0):
            i2=i
            flag*=3
        if(x[i][2]==''and flag%5!=0):
            i3=i
            flag*=5
        if(flag%30==0):
            break
        i+=1
    if(dir=='L'):
        i=0
        j=0
        if(rows-i1>=space):
            i=i1
            while(space>0):
                x[i][j]=ch
                space-=1
                i+=1
        else:
                print("wait till trafic moves")
            
    elif(dir=='S'):
        i=0
        j=1
        if(rows-i2>=space and i2<=i3):
            i=i2
            while(space>0):
                x[i][j]=ch
                space-=1
                i+=1
        elif(rows-i3>=space):
            j=2
            i=i3
            while(space>0):
                x[i][j]=ch
                space-=1
                i+=1
        else:
                print("wait till trafic moves")

    elif(dir=='R'):
        i=0
        j=2
        if(rows-i3>=space):
            i=i3
            while(space>0):
                x[i][j]=ch
                space-=1
                i+=1
        else:
                print("wait till trafic moves")
    
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

def movementLane(arr , rows , j,sp):

    i=0
    speed =0
    #print(arr)
    while(i<rows):

        #For Cycle , Loaded Tanker & Loaded Troller

        if(arr[i][j]=='C2' or arr[i][j]=='T22' or arr[i][j]=='T32' or arr[i][j]=='C2C2' or arr[i][j]=='C2C2C2' or arr[i][j]=='B2C2' or arr[i][j]=='C2B2'):     
            while(i<rows and arr[i][j]!=''):
                sp[i][j]=10
                i+=1
            speed =10
            print("\nTill the end the lane moves with the speed of ",speed)
        
        #For Truck & Unloaded Troller

        elif (arr[i][j]=='T1' or arr[i][j]=='T31'):
            sp[i][j]=15
            i+=1
            while(i<rows):
                if(arr[i][j]=='C2' or arr[i][j]=='C2C2C2' or arr[i][j]=='B2C2' or arr[i][j]=='C2B2' or arr[i][j]=='C2C2' or arr[i][j]=='T22' or arr[i][j]=='T32' or arr[i][j]==''):
                    speed = 15
                    print("\nTill ",i-1," the lane moves with the speed of ",speed)
                    break
                if(arr[i][j]!=''):
                    sp[i][j]=15
                i+=1
            if(i==rows):
                speed = 15
                print("\nTill end the lane moves with the speed of ",speed)
        
        #For Bus , E-rickshaw & Loaded Tanker

        elif(arr[i][j]=='B1' or arr[i][j]=='E' or arr[i][j]=='T21'):
            sp[i][j]=20
            i+=1
            while(i<rows):
                if(arr[i][j]=='C2' or arr[i][j]=='C2C2C2' or arr[i][j]=='B2C2' or arr[i][j]=='C2B2' or arr[i][j]=='C2C2' or arr[i][j]=='T22' or arr[i][j]=='T32' or arr[i][j]=='T1' or arr[i][j]=='T31'  or arr[i][j]==''):
                    speed = 20
                    print("\nTill ",i-1," the lane moves with the speed of ",speed)
                    break
                if(arr[i][j]!=''):
                    sp[i][j]=20
                i+=1
            if(i==rows):
                speed = 20
                print("\nTill end the lane moves with the speed of ",speed)
        
        #For Tempo

        elif(arr[i][j]=='T4'):
            sp[i][j]=25
            i+=1
            while(i<rows):
                if(arr[i][j]=='C2' or arr[i][j]=='C2C2C2' or arr[i][j]=='B2C2' or arr[i][j]=='C2B2' or arr[i][j]=='C2C2' or arr[i][j]=='T22' or arr[i][j]=='T32' or arr[i][j]=='T1' or arr[i][j]=='T31'  or arr[i][j]=='' or arr[i][j]=='B1' or arr[i][j]=='E' or arr[i][j]=='T21'):
                    speed = 25
                    print("\nTill ",i-1," the lane moves with the speed of ",speed)
                    break
                if(arr[i][j]!=''):
                    sp[i][j]=25
                i+=1
            if(i==rows):
                speed = 25
                print("\nTill end the lane moves with the speed of ",speed)
        
        #For Car

        elif(arr[i][j]=='C1'):
            sp[i][j]=30
            i+=1
            while(i<rows):
                if(arr[i][j]=='C2' or arr[i][j]=='C2C2C2' or arr[i][j]=='B2C2' or arr[i][j]=='C2B2' or arr[i][j]=='C2C2' or arr[i][j]=='T22' or arr[i][j]=='T32' or arr[i][j]=='T1' or arr[i][j]=='T31'  or arr[i][j]=='' or arr[i][j]=='B1' or arr[i][j]=='E' or arr[i][j]=='T21' or arr[i][j]=='T4'):
                    speed = 30
                    print("\nTill ",i-1," the lane moves with the speed of ",speed)
                    break
                if(arr[i][j]!=''):
                    sp[i][j]=30
                i+=1
            if(i==rows):
                speed = 30
                print("\nTill end the lane moves with the speed of ",speed)
        
        #For Bike
        
        elif(arr[i][j]=='B2' or arr[i][j]=='B2B2'):
            sp[i][j]=35
            i+=1
            while(i<rows):
                if(arr[i][j]=='C2' or arr[i][j]=='C2C2C2' or arr[i][j]=='B2C2' or arr[i][j]=='C2B2' or arr[i][j]=='C2C2' or arr[i][j]=='T22' or arr[i][j]=='T32' or arr[i][j]=='T1' or arr[i][j]=='T31'  or arr[i][j]=='' or arr[i][j]=='B1' or arr[i][j]=='E' or arr[i][j]=='T21' or arr[i][j]=='T4' or arr[i][j]=='C1'):
                    speed = 35
                    print("\nTill ",i-1," the lane moves with the speed of ",speed)
                    break
                if(arr[i][j]!=''):
                    sp[i][j]=35
                i+=1
            if(i==rows):
                speed = 35
                print("\nTill end the lane moves with the speed of ",speed)
        else:
            i+=1
            
