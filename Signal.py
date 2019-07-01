import numpy as np
from Movement import movementLane
import math
from time import sleep

SIZE = 75


class Signal:

    def __init__(self, colour):
        self.light = np.chararray((4), unicode=True)
        self.dur = 30
        i = 0
        while (i < 4):
            self.light[i] = colour[i]
            i += 1

    def MoveLeft(self, arr, sp, m, r):
        count = 0
        k = 0
        i = 0
        time = self.dur * 4
        j = 0
        time2 = 0
        scaling = 10
        while (k < 25 and r[m].x[k][j] != '' and time > 0 and r[m].vehicles >= 1):
            count += 1

            if (r[m].x[k][j] == 'T1' or r[m].x[k][j] == 'B1'):
                n = k
                while (n < (k + 5)):
                    r[m].x[n][j] = ''
                    n += 1
                k += 5

            elif (r[m].x[k][j] == 'T21' or r[m].x[k][j] == 'T22'):
                n = k
                while (n < (k + 6)):
                    r[m].x[n][j] = ''
                    n += 1
                k += 6

            elif (r[m].x[k][j] == 'T31' or r[m].x[k][j] == 'T32'):
                n = k
                while (n < (k + 7)):
                    r[m].x[n][j] = ''
                    n += 1
                k += 7

            elif (r[m].x[k][j] == 'C1' or r[m].x[k][j] == 'E' or r[m].x[k][j] == 'T4'):
                n = k
                while (n < (k + 2)):
                    r[m].x[n][j] = ''
                    n += 1
                k += 2

            elif (r[m].x[k][j] == 'B2' or r[m].x[k][j] == 'C2' or r[m].x[k][j] == 'B2B2' or r[m].x[k][j] == 'C2C2C2' or
                  r[m].x[k][j] == 'B2C2' or r[m].x[i][j] == 'C2B2'):

                if (r[m].x[k][j] == 'C2C2' or r[m].x[k][j] == 'C2B2' or r[m].x[k][j] == 'B2C2' or r[m].x[k][
                    j] == 'B2B2'):
                    count += 1

                elif (r[m].x[k][j] == 'C2C2C2'):
                    count += 2

                else:
                    pass

                n = k
                while (n < (k + 1)):
                    r[m].x[n][j] = ''
                    n += 1
                k += 1

            if (r[m].sp[k - 1][j] != 0):
                time1 = int(math.ceil(k * scaling / r[m].sp[k - 1][j]))
            else:
                time1 = time - time2
            time2 += time1 - time2
            time -= time2

        r[m].sp = np.zeros((25, 3))
        while (i < 25 and arr[i][j] == ''):
            i += 1

        k = i
        i = 0

        while (k < 25 and arr[k][j] != ''):
            arr[i][j] = arr[k][j]
            arr[k][j] = ''
            k += 1
            i += 1

        while (i < 25 and arr[i][j] == ''):
            i += 1
        k = i
        while (k < 25 and arr[k][j] != ''):
            arr[i][j] = arr[k][j]
            arr[k][j] = ''
            k += 1
            i += 1
        r[m].sp = np.zeros((25, 3))
        for j in range(0, 3):
            movementLane(self.arr, 25, j, r[m].sp)
        sleep(2)

    def moveForward(self, arr, m, r):
        self.arr = arr
        i = 0
        j = 1
        while (j < 3):
            while (i < 25 and arr[i][j] == ''):
                i += 1

            k = i
            i = 0

            while (k < 25 and arr[k][j] != ''):
                arr[i][j] = arr[k][j]
                arr[k][j] = ''
                k += 1
                i += 1

            while (i < 25 and arr[i][j] == ''):
                i += 1
            k = i
            while (k < 25 and arr[k][j] != ''):
                arr[i][j] = arr[k][j]
                arr[k][j] = ''
                k += 1
                i += 1

            k = i
            i = 0
            j += 1

        r[m].sp = np.zeros((25, 3))
        for j in range(0, 3):
            movementLane(self.arr, 25, j, r[m].sp)
        return arr

    def FCFS(self, colour, r):

        self.r = r
        self.colour = colour
        if (colour == ['O', 'O', 'O', 'O']):
            i = 0
            while (i < 4):
                j = 1
                while (j < 3):
                    k = 0
                    while (k < 25):
                        if (r[i].x[k][j] != '' and r[i].x[k][j] == 'T1'):
                            print("Truck from road ", i + 1, " and of straight lane will pass")
                            n = k
                            while (n <= (k + 5)):
                                r[i].x[n][j] = ''
                                n += 1
                            k += 5

                        elif (r[i].x[k][j] != '' and r[i].x[k][j] == 'T22'):
                            print("Loaded Tanker from road ", i + 1, " and of straight lane will pass")
                            n = k
                            while (n <= (k + 6)):
                                r[i].x[n][j] = ''
                                n += 1
                            k += 6

                        elif (r[i].x[k][j] != '' and r[i].x[k][j] == 'T21'):
                            print("Unloaded Tanker from road ", i + 1, " and of straight lane will pass")
                            n = k
                            while (n <= (k + 6)):
                                r[i].x[n][j] = ''
                                n += 1
                            k += 6

                        elif (r[i].x[k][j] != '' and r[i].x[k][j] == 'T32'):
                            print("Loaded Troller from road ", i + 1, " and of straight lane will pass")
                            n = k
                            while (n <= (k + 7)):
                                r[i].x[n][j] = ''
                                n += 1
                            k += 7

                        elif (r[i].x[k][j] != '' and r[i].x[k][j] == 'T31'):
                            print("Unloaded Tanker from road ", i + 1, " and of straight lane will pass")
                            n = k
                            while (n <= (k + 7)):
                                r[i].x[n][j] = ''
                                n += 1
                            k += 7

                        elif (r[i].x[k][j] != '' and r[i].x[k][j] == 'B1'):
                            print("Bus from road ", i + 1, " and of straight lane will pass")
                            n = k
                            while (n <= (k + 5)):
                                r[i].x[n][j] = ''
                                n += 1
                            k += 5

                        elif (r[i].x[k][j] != '' and r[i].x[k][j] == 'C1'):
                            print("Car from road ", i + 1, " and of straight lane will pass")
                            n = k
                            while (n <= (k + 2)):
                                r[i].x[n][j] = ''
                                n += 1
                            k += 2

                        elif (r[i].x[k][j] != '' and r[i].x[k][j] == 'E'):
                            print("E-Rickshaw from road ", i + 1, " and of straight lane will pass")
                            n = k
                            while (n <= (k + 2)):
                                r[i].x[n][j] = ''
                                n += 1
                            k += 2

                        elif (r[i].x[k][j] != '' and r[i].x[k][j] == 'T4'):
                            print("Tempo from road ", i + 1, " and of straight lane will pass")
                            n = k
                            while (n <= (k + 2)):
                                r[i].x[n][j] = ''
                                n += 1
                            k += 2

                        elif (r[i].x[k][j] != '' and r[i].x[k][j] == 'B2'):
                            print("Bike/Scooty from road ", i + 1, " and of straight lane will pass")
                            n = k
                            while (n <= (k + 1)):
                                r[i].x[n][j] = ''
                                n += 1
                            k += 1

                        elif (r[i].x[k][j] != '' and r[i].x[k][j] == 'C2'):
                            print("Cycle from road ", i + 1, " and of straight lane will pass")
                            n = k
                            while (n <= (k + 1)):
                                r[i].x[n][j] = ''
                                n += 1
                            k += 1

                        # elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T1' and j == 2):
                        #     print("Truck from road ",i+1," and of right lane will pass")
                        #     n = k
                        #     while(n<=(k+5)):
                        #         r[i].x[n][j] = ''
                        #         n+=1
                        #     k+=5

                        # elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T22' and j == 2):
                        #     print("Loaded Tanker from road ",i+1," and of right lane will pass")
                        #     n = k
                        #     while(n<=(k+6)):
                        #         r[i].x[n][j] = ''
                        #         n+=1
                        #     k += 6

                        # elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T21' and j == 2):
                        #     print("Unloaded Tanker from road ",i+1," and of right lane will pass")
                        #     n = k
                        #     while(n<=(k+6)):
                        #         r[i].x[n][j] = ''
                        #         n+=1
                        #     k += 6

                        # elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T32' and j == 2):
                        #     print("Loaded Troller from road ",i+1," and of right lane will pass")
                        #     n = k
                        #     while(n<=(k+7)):
                        #         r[i].x[n][j] = ''
                        #         n+=1
                        #     k+=7

                        # elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T31' and j == 2):
                        #     print("Unloaded Troller from road ",i+1," and of right lane will pass")
                        #     n = k
                        #     while(n<=(k+7)):
                        #         r[i].x[n][j] = ''
                        #         n+=1
                        #     k+=7

                        # elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'B1' and j == 2):
                        #     print("Bus from road ",i+1," and of right lane will pass")
                        #     n = k
                        #     while(n<=(k+5)):
                        #         r[i].x[n][j] = ''
                        #         n+=1
                        #     k+=5

                        # elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'C1' and j == 2):
                        #     print("Car from road ",i+1," and of right lane will pass")
                        #     n = k
                        #     while(n<=(k+2)):
                        #         r[i].x[n][j] = ''
                        #         n+=1
                        #     k+=2

                        # elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'E' and j == 2):
                        #     print("E-Rickshaw from road ",i+1," and of right lane will pass")
                        #     n = k
                        #     while(n<=(k+2)):
                        #         r[i].x[n][j] = ''
                        #         n+=1
                        #     k+=2

                        # elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'T4' and j == 2):
                        #     print("Tempo from road ",i+1," and of right lane will pass")
                        #     n = k
                        #     while(n<=(k+2)):
                        #         r[i].x[n][j] = ''
                        #         n+=1
                        #     k+=2

                        # elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'TB2' and j == 2):
                        #     print("Bike/Scooty from road ",i+1," and of right lane will pass")
                        #     n = k
                        #     while(n<=(k+1)):
                        #         r[i].x[n][j] = ''
                        #         n+=1
                        #     k+=1

                        # elif(r[i].x[k][j] != '' and r[i].x[k][j] == 'TC2' and j == 2):
                        #     print("Cycle from road ",i+1," and of right lane will pass")
                        #     n = k
                        #     while(n<=(k+1)):
                        #         r[i].x[n][j] = ''
                        #         n+=1
                        #     k+=1

                        # else:
                        #     pass
                    j += 1
                self.moveForward(r[i].x, i, r)
                i += 1

    def lightGreen(self, i, r):
        j = 13
        scaling = 10
        while (j < 3):

            count = 0
            k = 0
            time2 = 0
            time = self.dur
            while (k < 25 and r[i].x[k][j] != '' and time > 0 and r[i].vehicles >= 1):
                count += 1

                if (r[i].x[k][j] == 'T1' or r[i].x[k][j] == 'B1'):
                    n = k
                    while (n < (k + 5)):
                        r[i].x[n][j] = ''
                        n += 1
                    k += 5

                elif (r[i].x[k][j] == 'T21' or r[i].x[k][j] == 'T22'):
                    n = k
                    while (n < (k + 6)):
                        r[i].x[n][j] = ''
                        n += 1
                    k += 6

                elif (r[i].x[k][j] == 'T31' or r[i].x[k][j] == 'T32'):
                    n = k
                    while (n < (k + 7)):
                        r[i].x[n][j] = ''
                        n += 1
                    k += 7

                elif (r[i].x[k][j] == 'C1' or r[i].x[k][j] == 'E' or r[i].x[k][j] == 'T4'):
                    n = k
                    while (n < (k + 2)):
                        r[i].x[n][j] = ''
                        n += 1
                    k += 2

                elif (r[i].x[k][j] == 'B2' or r[i].x[k][j] == 'C2' or r[i].x[k][j] == 'C2C2C2' or r[i].x[k][
                    j] == 'C2C2' or r[i].x[k][j] == 'C2B2' or r[i].x[k][j] == 'B2C2' or r[i].x[k][j] == 'B2B2'):

                    if (r[i].x[k][j] == 'C2C2' or r[i].x[k][j] == 'C2B2' or r[i].x[k][j] == 'B2C2' or r[i].x[k][
                        j] == 'B2B2'):
                        count += 1
                    elif (r[i].x[k][j] == 'C2C2C2'):
                        count += 2
                    else:
                        pass
                    n = k
                    while (n < (k + 1)):
                        r[i].x[n][j] = ''
                        n += 1

                    k += 1

                if (r[i].sp[k - 1][j] != 0):
                    time1 = int(math.ceil(k * scaling / r[i].sp[k - 1][j]))
                else:
                    time1 = time - time2
                time2 += time1 - time2
                time -= time2

            print("\nTime taken by the lane ", j, " is ", (self.dur - time))
            print("\nTotal Vehicles that crossed the round about from this lane ", count)
            j += 1
        print("\n\t\tNew Arrangement for road ", (i + 1), "\n")
        r[i].x = self.moveForward(r[i].x, i, r)
        # print("\nVehicles remaining on these two lanes:- ",r[i].vehicles)


def mainSignal(p, time):
    s = []
    colour = ['O', 'O', 'O', 'O']
    i = 0
    while (i < 4):
        s.append(Signal(colour))
        i += 1
    # if(time>=6 and time<22):
    print("\n\t\tWhen Signal is given Clockwise")
    i = 0

    while (i < 4):
        sleep(3)  # For Clockwise Signal behaviour
        print("\n\n\t\tSignal is Green for road ", (i + 1), "\n")
        print("\n", p[i].x)
        # print("\n",p[i].sp)
        s[i].lightGreen(i, p)
        s[i].light[i] = 'G'
        x = (i + 1) % 4
        s[i].light[x] = 'O'
        x = (i + 2) % 4
        s[i].light[x] = 'R'
        x = (i + 3) % 4
        s[i].light[x] = 'R'
        print("\nSignal was as follows :-", s[i].light)
        i += 1

    print("\n\n\t\tLeft lane movements")
    i = 0
    while (i < 4):
        sleep(2)
        print("\n\tFor road ", i + 1)
        s[i].MoveLeft(p[i].x, p[i].sp, i, p)
        print("\n\n", p[i].x)
        i += 1
    # else:
    #     i=0
    #     while(i<4):
    #         s[i].FCFS(colour,p)
    #         i+=1
    # print("call fcfs here")
