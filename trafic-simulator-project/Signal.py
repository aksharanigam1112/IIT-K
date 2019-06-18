import numpy as np
from Movement import movementLane
import math
from time import sleep

SIZE=75

class Signal:
    
    def __init__(self,colour):
        self.light  = np.chararray((4),unicode=True)
        self.dur = 30
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
        while(k<25 and r[m].x[k][j]!='' and time>0 and r[m].vehicles>=1):
            # time -= int(math.ceil(100/r[i].sp[k][j]))
            count+=1

            if(r[m].x[k][j]=='T1'or r[m].x[k][j]=='B1'):
                n = k
                while(n<(k+5)):
                    r[m].x[n][j] = ''
                    n+=1
                # if(r[m].x[k][j]=='T1'):
                #     r[m].truck[2]-=1
                #     r[m].truck[3]-=5
                # else:
                #     r[m].bus[2]-=1
                #     r[m].bus[3]-=5
                k+=5

            elif(r[m].x[k][j]=='T21'or r[m].x[k][j]=='T22'):
                n = k
                while(n<(k+6)):
                    r[m].x[n][j] = ''
                    n+=1
                # if(r[m].x[k][j]=='T21'):
                #         r[m].utanker[2]-=1
                #         r[m].utanker[3]-=6
                # else:
                #     r[m].ltanker[2]-=1
                #     r[m].ltanker[3]-=6
                k+=6

            elif(r[m].x[k][j]=='T31'or r[m].x[k][j]=='T32'):
                n = k
                while(n<(k+7)):
                    r[m].x[n][j] = ''
                    n+=1
                # if(r[m].x[k][j]=='T31'):
                #         r[m].utroller[2]-=1
                #         r[m].utroller[3]-=7
                # else:
                #     r[m].ltroller[2]-=1
                #     r[m].ltroller[3]-=7
                k+=7
                            
            elif(r[m].x[k][j]=='C1' or r[m].x[k][j]=='E' or r[m].x[k][j]=='T4'):
                n = k
                while(n<(k+2)):
                    r[m].x[n][j] = ''
                    n+=1
                # if(r[m].x[k][j]=='C1'):
                #     r[m].car[2]-=1
                #     r[m].car[3]-=2
                # elif(r[m].x[k][j]=='E'):
                #     r[m].erick[2]-=1
                #     r[m].erick[3]-=2
                # else:
                #     r[m].tempo[2]-=1
                #     r[m].tempo[3]-=2
                k+=2
                                          
            elif(r[m].x[k][j]=='B2' or r[m].x[k][j]=='C2' or r[m].x[k][j]=='B2B2' or r[m].x[k][j]=='C2C2C2' or r[m].x[k][j]=='B2C2' or r[m].x[i][j]=='C2B2'):
                
                if(r[m].x[k][j]=='C2C2' or r[m].x[k][j]=='C2B2' or r[m].x[k][j]=='B2C2' or r[m].x[k][j]=='B2B2'):
                    count+=1
                    # if(r[m].x[k][j]=='C2C2'):
                    #     r[m].cycle[2]-=2
                    #     r[m].cycle[3]-=2
                    # elif(r[m].x[k][j]=='C2B2' or r[m].x[k][j]=='B2C2'):
                    #     r[m].cycle[2]-=1
                    #     r[m].cycle[3]-=1
                    #     r[m].bike[2]-=1
                    #     r[m].bike[3]-=1
                    # elif(r[m].x[k][j]=='B2B2'):
                    #     r[m].bike[2]-=2
                    #     r[m].bike[3]-=2
                    
                elif(r[m].x[k][j]=='C2C2C2'):
                    count+=2
                    # r[m].cycle[2]-=3
                    # r[m].cycle[3]-=3
                
                else:
                    # if(r[m].x[k][j]=='C2'):
                    #     r[m].cycle[2]-=1
                    #     r[m].cycle[3]-=1
                    # elif(r[m].x[k][j]=='B2'):
                    #     r[m].bike[2]-=1
                    #     r[m].bike[3]-=1
                    pass

                n = k
                while(n<(k+1)):
                    r[m].x[n][j] = ''
                    n+=1
                k+=1

            if(r[m].sp[k-1][j]!=0):
                time1= int(math.ceil(k*scaling/r[m].sp[k-1][j]))
            else:
                time1=time-time2
            time2+=time1-time2
            time-=time2
            
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
        # r[m].countveh()
        # print("vehicle=",r[m].vehicles)
        # r[m].Display()
        # r[m].vehicles-=count
        # r[m].vehicles=r[m].truck[2]+r[m].utroller[2]+r[m].ltroller[2]+r[m].utanker[2]+r[m].ltanker[2]+r[m].bus[2]+r[m].car[2]+r[m].tempo[2]+r[m].erick[2]+r[m].bike[2]+r[m].cycle[2]
        # print("vehicle=",r[m].vehicles)
        sleep(2)
        #print("\n",r[m].sp)

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

        # print(arr)
        r[m].sp=np.zeros((25,3))
        for j in range(0,3):
            movementLane(self.arr,25,j,r[m].sp)
        #print("\n",r[m].sp)
        return arr

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
                            n = k
                            while(n<=(k+5)):
                                r[i].x[n][j] = ''
                                n+=1
                            k+=5
                            
                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T22' and j == 1):
                            print("Loaded Tanker from road ",i+1," and of straight lane will pass")
                            n = k
                            while(n<=(k+7)):
                                r[i].x[n][j] = ''
                                n+=1
                            k += 6

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T21' and j == 1):
                            print("Unloaded Tanker from road ",i+1," and of straight lane will pass")
                            n = k
                            while(n<=(k+7)):
                                r[i].x[n][j] = ''
                                n+=1
                            k += 6

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T32' and j == 1):
                            print("Loaded Troller from road ",i+1," and of straight lane will pass")
                            n = k
                            while(n<=(k+6)):
                                r[i].x[n][j] = ''
                                n+=1
                            k+=7

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T31' and j == 1):
                            print("Unloaded Tanker from road ",i+1," and of straight lane will pass")
                            n = k
                            while(n<=(k+6)):
                                r[i].x[n][j] = ''
                                n+=1
                            k+=7

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'B1' and j == 1):
                            print("Bus from road ",i+1," and of straight lane will pass")
                            n = k
                            while(n<=(k+5)):
                                r[i].x[n][j] = ''
                                n+=1
                            k+=5

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'C1' and j == 1):
                            print("Car from road ",i+1," and of straight lane will pass")
                            n = k
                            while(n<=(k+2)):
                                r[i].x[n][j] = ''
                                n+=1
                            k+=2

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'E' and j == 1):
                            print("E-Rickshaw from road ",i+1," and of straight lane will pass")
                            n = k
                            while(n<=(k+2)):
                                r[i].x[n][j] = ''
                                n+=1
                            k+=2

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T4' and j == 1):
                            print("Tempo from road ",i+1," and of straight lane will pass")
                            n = k
                            while(n<=(k+2)):
                                r[i].x[n][j] = ''
                                n+=1
                            k+=2

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'B2' and j == 1):
                            print("Bike/Scooty from road ",i+1," and of straight lane will pass")
                            n = k
                            while(n<=(k+1)):
                                r[i].x[n][j] = ''
                                n+=1
                            k+=1

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'C2' and j == 1):
                            print("Cycle from road ",i+1," and of straight lane will pass")
                            n = k
                            while(n<=(k+1)):
                                r[i].x[n][j] = ''
                                n+=1
                            k+=1

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T1' and j == 2):
                            print("Truck from road ",i+1," and of right lane will pass")
                            n = k
                            while(n<=(k+5)):
                                r[i].x[n][j] = ''
                                n+=1
                            k+=5

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T22' and j == 2):
                            print("Loaded Tanker from road ",i+1," and of right lane will pass")
                            n = k
                            while(n<=(k+7)):
                                r[i].x[n][j] = ''
                                n+=1
                            k += 6

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T21' and j == 2):
                            print("Unloaded Tanker from road ",i+1," and of right lane will pass")
                            n = k
                            while(n<=(k+7)):
                                r[i].x[n][j] = ''
                                n+=1
                            k += 6

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T32' and j == 2):
                            print("Loaded Troller from road ",i+1," and of right lane will pass")
                            n = k
                            while(n<=(k+6)):
                                r[i].x[n][j] = ''
                                n+=1
                            k+=7

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T31' and j == 2):
                            print("Unloaded Troller from road ",i+1," and of right lane will pass")
                            n = k
                            while(n<=(k+6)):
                                r[i].x[n][j] = ''
                                n+=1
                            k+=7

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'B1' and j == 2):
                            print("Bus from road ",i+1," and of right lane will pass")
                            n = k
                            while(n<=(k+5)):
                                r[i].x[n][j] = ''
                                n+=1
                            k+=5

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'C1' and j == 2):
                            print("Car from road ",i+1," and of right lane will pass")
                            n = k
                            while(n<=(k+2)):
                                r[i].x[n][j] = ''
                                n+=1
                            k+=2

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'E' and j == 2):
                            print("E-Rickshaw from road ",i+1," and of right lane will pass")
                            n = k
                            while(n<=(k+2)):
                                r[i].x[n][j] = ''
                                n+=1
                            k+=2

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T4' and j == 2):
                            print("Tempo from road ",i+1," and of right lane will pass")
                            n = k
                            while(n<=(k+2)):
                                r[i].x[n][j] = ''
                                n+=1
                            k+=2

                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'TB2' and j == 2):
                            print("Bike/Scooty from road ",i+1," and of right lane will pass")
                            n = k
                            while(n<=(k+1)):
                                r[i].x[n][j] = ''
                                n+=1
                            k+=1
                        
                        elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'TC2' and j == 2):
                            print("Cycle from road ",i+1," and of right lane will pass")
                            n = k
                            while(n<=(k+1)):
                                r[i].x[n][j] = ''
                                n+=1
                            k+=1

                        else:
                            pass
                    j += 1
                    self.moveForward(r[i].x,i,r)
                i += 1
            #i = 0
            #while(i<4):
                #j = 0
                #while(j<4):
                    #if(i == 0 and j == 2):
                       #print("vehicles from both the lane will pass simultaneously")
                    #if(i == 1 and j == 3):
                        #print("vehicles from both the lane will pass simultaneously")
                    #if(i == 2 and j == 0):
                        #print("vehicles from both the lane will pass simultaneously")
                    #if(i == 3 and j == 1):
                        #print("vehicles from both the lane will pass simultaneously")
                   # j+=1
                #i+=1


    def lightGreen(self,i ,r):
        j=1
        scaling=10
        while(j<3):

            count=0
            k=0
            time2=0
            time =self.dur
            while(k<25 and r[i].x[k][j]!='' and time>0 and r[i].vehicles>=1):
                count+=1
                
                if(r[i].x[k][j]=='T1'or r[i].x[k][j]=='B1'):
                    n = k
                    while(n<(k+5)):
                        r[i].x[n][j] = ''
                        n+=1
                    # if(r[i].x[k][j]=='T1'):
                    #     r[i].truck[2]-=1
                    #     r[i].truck[3]-=5
                    # else:
                    #     r[i].bus[2]-=1
                    #     r[i].bus[3]-=5
                    k+=5

                elif(r[i].x[k][j]=='T21'or r[i].x[k][j]=='T22'):
                    n = k
                    while(n<(k+6)):
                        r[i].x[n][j] = ''
                        n+=1
                    # if(r[i].x[k][j]=='T21'):
                    #     r[i].utanker[2]-=1
                    #     r[i].utanker[3]-=6
                    # else:
                    #     r[i].ltanker[2]-=1
                    #     r[i].ltanker[3]-=6
                    k+=6

                elif(r[i].x[k][j]=='T31'or r[i].x[k][j]=='T32'):
                    n = k
                    while(n<(k+7)):
                        r[i].x[n][j] = ''
                        n+=1
                    # if(r[i].x[k][j]=='T31'):
                    #     r[i].utroller[2]-=1
                    #     r[i].utroller[3]-=7
                    # else:
                    #     r[i].ltroller[2]-=1
                    #     r[i].ltroller[3]-=7
                    k+=7
                            
                elif(r[i].x[k][j]=='C1' or r[i].x[k][j]=='E' or r[i].x[k][j]=='T4'):
                    n = k
                    while(n<(k+2)):
                        r[i].x[n][j] = ''
                        n+=1
                    # if(r[i].x[k][j]=='C1'):
                    #     r[i].car[2]-=1
                    #     r[i].car[3]-=2
                    # elif(r[i].x[k][j]=='E'):
                    #     r[i].erick[2]-=1
                    #     r[i].erick[3]-=2
                    # else:
                    #     r[i].tempo[2]-=1
                    #     r[i].tempo[3]-=2
                    k+=2
                                          
                elif(r[i].x[k][j]=='B2' or r[i].x[k][j]=='C2' or r[i].x[k][j]=='C2C2C2' or r[i].x[k][j]=='C2C2' or r[i].x[k][j]=='C2B2' or r[i].x[k][j]=='B2C2' or r[i].x[k][j]=='B2B2'):
                    
                    if(r[i].x[k][j]=='C2C2' or r[i].x[k][j]=='C2B2' or r[i].x[k][j]=='B2C2' or r[i].x[k][j]=='B2B2'):
                        count+=1
                        # if(r[i].x[k][j]=='C2C2'):
                        #     r[i].cycle[2]-=2
                        #     r[i].cycle[3]-=2
                        # elif(r[i].x[k][j]=='C2B2' or r[i].x[k][j]=='B2C2'):
                        #     r[i].cycle[2]-=1
                        #     r[i].cycle[3]-=1
                        #     r[i].bike[2]-=1
                        #     r[i].bike[3]-=1
                        # elif(r[i].x[k][j]=='B2B2'):
                        #     r[i].bike[2]-=2
                        #     r[i].bike[3]-=2
                    elif(r[i].x[k][j]=='C2C2C2'):
                        count+=2
                        # r[i].cycle[2]-=3
                        # r[i].cycle[3]-=3
                    else:
                        # if(r[i].x[k][j]=='C2'):
                        #     r[i].cycle[2]-=1
                        #     r[i].cycle[3]-=1
                        # elif(r[i].x[k][j]=='B2'):
                        #     r[i].bike[2]-=1
                        #     r[i].bike[3]-=1
                        pass
                    n = k
                    while(n<(k+1)):
                        r[i].x[n][j] = ''
                        n+=1
                    
                    k+=1
                
                if(r[i].sp[k-1][j]!=0):
                    time1= int(math.ceil(k*scaling/r[i].sp[k-1][j]))
                else:
                    time1=time-time2
                time2+=time1-time2
                time-=time2
                    
            print("\nTime taken by the lane ",j," is ",(self.dur-time))  
            print("\nTotal Vehicles that crossed the round about from this lane ",count)                            
            # r[i].vehicles=r[i].truck[2]+r[i].utroller[2]+r[i].ltroller[2]+r[i].utanker[2]+r[i].ltanker[2]+r[i].bus[2]+r[i].car[2]+r[i].tempo[2]+r[i].erick[2]+r[i].bike[2]+r[i].cycle[2]
            # r[i].space=r[i].truck[3]+r[i].utroller[3]+r[i].ltroller[3]+r[i].utanker[3]+r[i].ltanker[3]+r[i].bus[3]+r[i].car[3]+r[i].tempo[3]+r[i].erick[3]+r[i].bike[3]+r[i].cycle[3]
            # r[i].con = r[i].space / SIZE
            j+=1
            # print("\nCount=",count)
        print("\n\t\tNew Arrangement for road ",(i+1),"\n")
        r[i].x=self.moveForward(r[i].x,i,r)
        # r[i].countveh()
        # count=0
        # k=0
        # while(k<25 and r[i].x[k][0]!='' and r[i].vehicles>=1):
        #     count+=1
        #     if(r[i].x[k][0]=='T1'or r[i].x[k][0]=='B1'):
        #         if(r[i].x[k][0]=='T1'):
        #             r[i].truck[2]-=1
        #             r[i].truck[3]-=5
        #         else:
        #             r[i].bus[2]-=1
        #             r[i].bus[3]-=5
        #         k+=5

        #     elif(r[i].x[k][0]=='T21'or r[i].x[k][0]=='T22'):
        #         if(r[i].x[k][0]=='T21'):
        #             r[i].utanker[2]-=1
        #             r[i].utanker[3]-=6
        #         else:
        #             r[i].ltanker[2]-=1
        #             r[i].ltanker[3]-=6
        #         k+=6

        #     elif(r[i].x[k][0]=='T31'or r[i].x[k][0]=='T32'):
        #         if(r[i].x[k][0]=='T31'):
        #             r[i].utroller[2]-=1
        #             r[i].utroller[3]-=7
        #         else:
        #             r[i].ltroller[2]-=1
        #             r[i].ltroller[3]-=7
        #         k+=7
                            
        #     elif(r[i].x[k][0]=='C1' or r[i].x[k][0]=='E' or r[i].x[k][0]=='T4'):
        #         if(r[i].x[k][0]=='C1'):
        #             r[i].car[2]-=1
        #             r[i].car[3]-=2
        #         elif(r[i].x[k][0]=='E'):
        #             r[i].erick[2]-=1
        #             r[i].erick[3]-=2
        #         else:
        #             r[i].tempo[2]-=1
        #             r[i].tempo[3]-=2
        #         k+=2
                                          
        #     elif(r[i].x[k][0]=='B2' or r[i].x[k][0]=='C2'):
        #         if(r[i].x[k][0]=='C2'):
        #             r[i].cycle[2]-=1
        #             r[i].cycle[3]-=1
        #         elif(r[i].x[k][0]=='B2'):
        #             r[i].bike[2]-=1
        #             r[i].bike[3]-=1
        #         k+=1
                
        #     elif(r[i].x[k][0]=='C2C2C2'):
        #         count+=2
        #         r[i].cycle[2]-=3
        #         r[i].cycle[3]-=3
        #         k+=1
                
        #     elif(r[i].x[k][0]=='C2B2' or r[i].x[k][0]=='B2C2' or r[i].x[k][0]=='B2B2' or r[i].x[k][0]=='C2C2'):
        #         count+=1
        #         if(r[i].x[k][0]=='C2C2'):
        #             r[i].cycle[2]-=2
        #             r[i].cycle[3]-=2
        #         elif(r[i].x[k][0]=='C2B2' or r[i].x[k][0]=='B2C2'):
        #             r[i].cycle[2]-=1
        #             r[i].cycle[3]-=1
        #             r[i].bike[2]-=1
        #             r[i].bike[3]-=1
        #         elif(r[i].x[k][0]=='B2B2'):
        #             r[i].bike[2]-=2
        #             r[i].bike[3]-=2
        #         k+=1
        #     else:
        #         pass
        # r[i].countveh()
        # r[i].Display()               
        # r[i].vehicles=r[i].truck[2]+r[i].utroller[2]+r[i].ltroller[2]+r[i].utanker[2]+r[i].ltanker[2]+r[i].bus[2]+r[i].car[2]+r[i].tempo[2]+r[i].erick[2]+r[i].bike[2]+r[i].cycle[2]
        # r[i].space=r[i].truck[3]+r[i].utroller[3]+r[i].ltroller[3]+r[i].utanker[3]+r[i].ltanker[3]+r[i].bus[3]+r[i].car[3]+r[i].tempo[3]+r[i].erick[3]+r[i].bike[3]+r[i].cycle[3]
        # r[i].con = r[i].space / SIZE
        print("\nVehicles remaining on these two lanes:- ",r[i].vehicles)


        
def mainSignal(p,time):
    s =[]
    colour = ['O','O','O','O']
    i=0
    while(i<4):
        s.append(Signal(colour))
        i+=1
    if(time>=6 and time<22):
        print("\n\t\tWhen Signal is given Clockwise")
        i=0
        while(i<4):                         # For Clockwise Signal behaviour
            print("\n\n\t\tSignal is Green for road ",(i+1),"\n")
            print("\n",p[i].x)
            #print("\n",p[i].sp)
            s[i].lightGreen(i,p)
            s[i].light[i] = 'G'
            x = (i+1)%4
            s[i].light[x]='O'
            x = (i+2)%4
            s[i].light[x] = 'R'
            x = (i+3)%4
            s[i].light[x] = 'R'
            print("\nSignal was as follows :-",s[i].light)
            i+=1
        

        print("\n\n\t\tLeft lane movements")
        i=0
        while(i<4):
            print("\n\tFor road ",i+1)
            s[i].MoveLeft(p[i].x,p[i].sp,i,p)
            print("\n\n",p[i].x)
            i+=1

    
        # print("\n\t\tWhen Signal is given Anticlockwise")
        # i=3
        # while(i>=0):                         # For Anti-Clockwise Signal behaviour
        #     print("\n\n\t\tSignal is Green for road ",(i+1),"\n")
        #     print("\n",p[i].x)
        #     #print("\n",p[i].sp)
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

        # print("\n\n\t\tLeft lane movements")
        # i=0
        # while(i<4):
        #     print("\n\tFor road ",i+1)
        #     s[i].MoveLeft(p[i].x,p[i].sp,i,p)
        #     print("\n\n",p[i].x)
        #     i+=1
    else:
        i=0
        while(i<4):
            s[i].FCFS(colour,p)
            i+=1
        print("call fcfs here")
