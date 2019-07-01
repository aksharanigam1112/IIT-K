import random
from Movement import arange, movementLane, inRightLaneMovingStraight, inCenterLaneMovingRight
from Signal import mainSignal
from time import sleep
import numpy as np
import math
from datetime import datetime
from default import takeDefault, inflow
from test import recording

SIZE = 75

class MainWindow:

    def ButtonClick(self, i, r, s):

        if (r[i].con > 0.7):
            s.dur += 10

        elif (r[i].con < 0.2):
            i = 0
            x = 0
            while (i < 4):
                if (s[i].direction == "clockwise" and s.colour[i] == 'O'):
                    s.colour[i] = 'G'
                    if (i > 0):
                        x = (i - 1) % 4
                    else:
                        x = 1
                    s.colour[x] = 'R'
                    x = (i + 1) % 4
                    s.colour[x] = 'O'
                elif (s[i].direction == "anticlockwise" and s.colour[i] == 'O'):
                    s.colour[i] = 'G'
                    x = (i + 1) % 4
                    s.colour[x] = 'R'
                    if (i > 0):
                        x = (i - 1) % 4
                    else:
                        x = 3
                    s.colour[x] = 'O'

                i += 1


class vehicle:

    def __init__(self, type, space):
        self.type = type
        self.space = space

    def direction(self):
        dir = ['L', 'S', 'R']
        i = random.randint(0, 2)
        return dir[i]


class road:

    def __init__(self, space, con, vehicles, data):

        self.x = np.chararray((25, 3), itemsize=6, unicode=True)
        self.sp = np.zeros((25, 3))

        self.data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.space = space

        self.truck = [5, 15, 0, 0]

        self.utroller = [7, 15, 0, 0]

        self.ltroller = [7, 10, 0, 0]

        self.utanker = [6, 20, 0, 0]

        self.ltanker = [6, 10, 0, 0]

        self.bus = [5, 20, 0, 0]

        self.car = [2, 30, 0, 0]

        self.erick = [2, 20, 0, 0]

        self.tempo = [2, 25, 0, 0]

        self.bike = [1, 35, 0, 0]

        self.cycle = [1, 10, 0, 0]

        self.con = con
        self.vehicles = vehicles
        self.unplaced = []
        self.waitL = []
        self.waitS = []
        self.waitR = []

    def Display(self, filename=None):

        if (filename != None):
            file = open(filename, "a")

            if (self.truck[2] != 0):
                print("\nNo. of trucks = ", self.truck[2], " & space consumed = ", self.truck[3])
                file.write("\nNo. of trucks = ")
                file.write(str(self.truck[2]))
                file.write(" & space consumed = ")
                file.write(str(self.truck[3]))

            if (self.utroller[2] != 0):
                print("\nNo. of unloaded trollers = ", self.utroller[2], " & space consumed = ", self.utroller[3])
                file.write("\nNo. of unloaded trollers = ")
                file.write(str(self.utroller[2]))
                file.write(" & space consumed = ")
                file.write(str(self.utroller[3]))

            if (self.ltroller[2] != 0 and filename != None):
                print("\nNo. of loaded trollers = ", self.ltroller[2], " & space consumed = ", self.ltroller[3])
                file.write("\nNo. of loaded trollers = ")
                file.write(str(self.ltroller[2]))
                file.write(" & space consumed = ")
                file.write(str(self.ltroller[3]))

            if (self.utanker[2] != 0 and filename != None):
                print("\nNo. of unloaded tankers = ", self.utanker[2], " & space consumed = ", self.utanker[3])
                file.write("\nNo. of unloaded tankers = ")
                file.write(str(self.utanker[2]))
                file.write(" & space consumed = ")
                file.write(str(self.utanker[3]))

            if (self.ltanker[2] != 0 and filename != None):
                print("\nNo. of loaded tankers = ", self.ltanker[2], " & space consumed = ", self.ltanker[3])
                file.write("\nNo. of loaded tankers = ")
                file.write(str(self.ltanker[2]))
                file.write(" & space consumed = ")
                file.write(str(self.ltanker[3]))

            if (self.bus[2] != 0 and filename != None):
                print("\nNo. of buses = ", self.bus[2], " & space consumed = ", self.bus[3])
                file.write("\nNo. of buses = ")
                file.write(str(self.bus[2]))
                file.write(" & space consumed = ")
                file.write(str(self.bus[3]))

            if (self.car[2] != 0 and filename != None):
                print("\nNo. of cars = ", self.car[2], " & space consumed = ", self.car[3])
                file.write("\nNo. of cars = ")
                file.write(str(self.car[2]))
                file.write(" & space consumed = ")
                file.write(str(self.car[3]))

            if (self.tempo[2] != 0 and filename != None):
                print("\nNo. of tempo = ", self.tempo[2], " & space consumed = ", self.tempo[3])
                file.write("\nNo. of tempo = ")
                file.write(str(self.tempo[2]))
                file.write(" & space consumed = ")
                file.write(str(self.tempo[3]))

            if (self.erick[2] != 0 and filename != None):
                print("\nNo. of erickshaw = ", self.erick[2], " & space consumed = ", self.erick[3])
                file.write("\nNo. of erickshaw = ")
                file.write(str(self.erick[2]))
                file.write(" & space consumed = ")
                file.write(str(self.erick[3]))

            if (self.bike[2] != 0 and filename != None):
                print("\nNo. of bikes & scooties = ", self.bike[2], " & space consumed = ", self.bike[3])
                file.write("\nNo. of bikes & scooties = ")
                file.write(str(self.bike[2]))
                file.write(" & space consumed = ")
                file.write(str(self.bike[3]))

            if (self.cycle[2] != 0 and filename != None):
                print("\nNo. of cycles = ", self.cycle[2], " & space consumed = ", self.cycle[3])
                file.write("\nNo. of cycles = ")
                file.write(str(self.cycle[2]))
                file.write(" & space consumed = ")
                file.write(str(self.cycle[3]))

            self.vehicles = self.truck[2] + self.ltroller[2] + self.utroller[2] + self.ltanker[2] + self.utanker[2] + \
                            self.bus[2] + self.car[2] + self.tempo[2] + self.erick[2] + self.bike[2] + self.cycle[2]
            self.space = self.truck[3] + self.ltroller[3] + self.utroller[3] + self.ltanker[3] + self.utanker[3] + \
                         self.bus[3] + self.car[3] + self.tempo[3] + self.erick[3] + self.bike[3] + self.cycle[3]
            self.con = self.space / SIZE

            print("\nTotal Vehicles = ", self.vehicles)
            file.write("\nTotal Vehicles = ")
            file.write(str(self.vehicles))

            print("\nCongestion = ", self.con)
            file.write("\nCongestion = ")
            file.write(str(self.con))

            file.close()
        else:
            pass

    def fillGap(self, arr, i, j):
        while (i < 24 and arr[i + 1][j] != ''):
            arr[i][j] = arr[i + 1][j]
            i += 1
        arr[i][j] = ''

    def countveh(self, filename=None):
        j = 0
        k = 0
        self.truck[2] = 0
        self.truck[3] = 0
        self.utroller[2] = 0
        self.utroller[3] = 0
        self.ltroller[2] = 0
        self.ltroller[3] = 0
        self.utanker[2] = 0
        self.utanker[3] = 0
        self.ltanker[2] = 0
        self.ltanker[3] = 0
        self.bus[2] = 0
        self.bus[3] = 0
        self.car[2] = 0
        self.car[3] = 0
        self.erick[2] = 0
        self.erick[3] = 0
        self.tempo[2] = 0
        self.tempo[3] = 0
        self.bike[2] = 0
        self.bike[3] = 0
        self.cycle[2] = 0
        self.cycle[3] = 0
        while (k < 3):
            j = 0

            while (j < 25 and self.x[j][k] != ''):

                if (self.x[j][k] == 'T1'):
                    self.truck[2] += 1
                    self.truck[3] += self.truck[0]
                    j += self.truck[0]

                elif (self.x[j][k] == 'T31'):
                    self.utroller[2] += 1
                    self.utroller[3] += self.utroller[0]
                    j += self.utroller[0]

                elif (self.x[j][k] == 'T32'):
                    self.ltroller[2] += 1
                    self.ltroller[3] += self.ltroller[0]
                    j += self.ltroller[0]

                elif (self.x[j][k] == 'T21'):
                    self.utanker[2] += 1
                    self.utanker[3] += self.utanker[0]
                    j += self.utanker[0]

                elif (self.x[j][k] == 'T22'):
                    self.ltanker[2] += 1
                    self.ltanker[3] += self.ltanker[0]
                    j += self.ltanker[0]

                elif (self.x[j][k] == 'B1'):
                    self.bus[2] += 1
                    self.bus[3] += self.bus[0]
                    j += self.bus[0]

                elif (self.x[j][k] == 'C1'):
                    self.car[2] += 1
                    self.car[3] += self.car[0]
                    j += self.car[0]

                elif (self.x[j][k] == 'T4'):
                    self.tempo[2] += 1
                    self.tempo[3] += self.tempo[0]
                    j += self.tempo[0]

                elif (self.x[j][k] == 'E'):
                    self.erick[2] += 1
                    self.erick[3] += self.erick[0]
                    j += self.erick[0]

                elif (self.x[j][k] == 'B2'):
                    self.bike[2] += 1
                    self.bike[3] += self.bike[0]
                    j += self.bike[0]

                elif (self.x[j][k] == 'C2'):
                    self.cycle[2] += 1
                    self.cycle[3] += self.cycle[0]
                    j += self.cycle[0]

                elif (self.x[j][k] == 'C2C2'):
                    self.cycle[2] += 2
                    self.cycle[3] += self.cycle[0]
                    j += self.cycle[0]

                elif (self.x[j][k] == 'C2C2C2'):
                    self.cycle[2] += 3
                    self.cycle[3] += self.cycle[0]
                    j += self.cycle[0]

                elif (self.x[j][k] == 'B2B2'):
                    self.bike[2] += 2
                    self.bike[3] += self.bike[0]
                    j += self.bike[0]

                elif (self.x[j][k] == 'B2C2' or self.x[j][k] == 'C2B2'):
                    self.bike[2] += 1
                    self.bike[3] += self.bike[0]
                    self.cycle[2] += 1
                    j += self.bike[0]
            k += 1
        self.vehicles = self.truck[2] + self.utroller[2] + self.ltroller[2] + self.utanker[2] + self.ltanker[2] + \
                        self.bus[2] + self.car[2] + self.tempo[2] + self.erick[2] + self.bike[2] + self.cycle[2]
        self.space = self.truck[3] + self.utroller[3] + self.ltroller[3] + self.utanker[3] + self.ltanker[3] + self.bus[
            3] + self.car[3] + self.tempo[3] + self.erick[3] + self.bike[3] + self.cycle[3]
        self.con = self.space / SIZE
        if (filename != None):
            self.Display(filename)
        else:
            self.Display()

    def Merge(self):
        j = 0
        while (j < 3):
            i = 0
            while (i < 25 and self.x[i][j] != ''):

                if (i < 24 and self.x[i][j] != '' and self.x[i][j] == 'B2' and (
                        self.x[i + 1][j] == 'B2' or self.x[i + 1][j] == 'C2')):
                    self.x[i][j] += self.x[i + 1][j]
                    self.x[i + 1][j] = ''
                    self.fillGap(self.x, i + 1, j)
                    i += 1

                elif (i < 24 and self.x[i][j] != '' and self.x[i][j] == 'C2' and (
                        self.x[i + 1][j] == 'B2' or self.x[i + 1][j] == 'C2')):
                    self.x[i][j] += self.x[i + 1][j]
                    self.x[i + 1][j] = ''
                    self.fillGap(self.x, i + 1, j)
                    i += 1

                elif (i < 23 and self.x[i][j] != '' and self.x[i][j] == 'C2' and self.x[i + 1][j] == 'C2' and
                      self.x[i + 2][j] == 'C2'):
                    self.x[i][j] += self.x[i + 1][j] + self.x[i + 2][j]
                    self.x[i + 1][j] = ''
                    self.x[i + 2][j] = ''
                    self.fillGap(self.x, i + 2, j)
                    self.fillGap(self.x, i + 1, j)
                    i += 1

                else:
                    i += 1
            j += 1


def getvehicle(v, wait, dir, rows, i):
    k = 0
    veh = 0
    flag1 = False
    sp = 0
    if (dir == 'N'):
        flag1 = True

    for j in wait:

        if (flag1 == True):
            dir = 'N'

        flag = True
        if (j == 0):
            v.append(vehicle("T1", 5))
            if (dir == "N"):
                dir = v[k].direction()
            else:
                pass
            flag = arange(r, j, "T1", 5, r[i].x, rows, dir, i)
            if (flag == False):
                if (flag == False):
                    if (dir == 'L'):
                        r[i].waitL.append(j)
                    elif (dir == 'S'):
                        r[i].waitS.append(j)
                    else:
                        r[i].waitR.append(j)
            else:
                sp += 5
                veh += 1
        elif (j == 1):
            v.append(vehicle("T31", 7))
            if (dir == "N"):
                dir = v[k].direction()
            else:
                pass
            flag = arange(r, j, "T31", 7, r[i].x, rows, dir, i)
            if (flag == False):
                if (dir == 'L'):
                    r[i].waitL.append(j)
                elif (dir == 'S'):
                    r[i].waitS.append(j)
                else:
                    r[i].waitR.append(j)
            else:
                sp += 7
                veh += 1

        elif (j == 2):
            v.append(vehicle("T32", 7))
            if (dir == "N"):
                dir = v[k].direction()
            else:
                pass
            flag = arange(r, j, "T32", 7, r[i].x, rows, dir, i)
            if (flag == False):
                if (dir == 'L'):
                    r[i].waitL.append(j)
                elif (dir == 'S'):
                    r[i].waitS.append(j)
                else:
                    r[i].waitR.append(j)
            else:
                sp += 7
                veh += 1

        elif (j == 3):
            v.append(vehicle("T21", 6))
            if (dir == "N"):
                dir = v[k].direction()
            else:
                pass
            flag = arange(r, j, "T21", 6, r[i].x, rows, dir, i)
            if (flag == False):
                if (dir == 'L'):
                    r[i].waitL.append(j)
                elif (dir == 'S'):
                    r[i].waitS.append(j)
                else:
                    r[i].waitR.append(j)
            else:
                sp += 6
                veh += 1

        elif (j == 4):
            v.append(vehicle("T22", 6))
            if (dir == "N"):
                dir = v[k].direction()
            else:
                pass
            flag = arange(r, j, "T22", 6, r[i].x, rows, dir, i)
            if (flag == False):
                if (dir == 'L'):
                    r[i].waitL.append(j)
                elif (dir == 'S'):
                    r[i].waitS.append(j)
                else:
                    r[i].waitR.append(j)
            else:
                sp += 6
                veh += 1

        elif (j == 5):
            v.append(vehicle("B1", 5))
            if (dir == "N"):
                dir = v[k].direction()
            else:
                pass
            flag = arange(r, j, "B1", 5, r[i].x, rows, dir, i)
            if (flag == False):
                if (dir == 'L'):
                    r[i].waitL.append(j)
                elif (dir == 'S'):
                    r[i].waitS.append(j)
                else:
                    r[i].waitR.append(j)
            else:
                sp += 5
                veh += 1

        elif (j == 6):
            v.append(vehicle("C1", 2))
            if (dir == "N"):
                dir = v[k].direction()
            else:
                pass
            flag = arange(r, j, 'C1', 2, r[i].x, rows, dir, i)
            if (flag == False):
                if (dir == 'L'):
                    r[i].waitL.append(j)
                elif (dir == 'S'):
                    r[i].waitS.append(j)
                else:
                    r[i].waitR.append(j)
            else:
                sp += 2
                veh += 1

        elif (j == 7):
            v.append(vehicle("T4", 2))
            if (dir == "N"):
                dir = v[k].direction()
            else:
                pass
            flag = arange(r, j, "T4", 2, r[i].x, rows, dir, i)
            if (flag == False):
                if (dir == 'L'):
                    r[i].waitL.append(j)
                elif (dir == 'S'):
                    r[i].waitS.append(j)
                else:
                    r[i].waitR.append(j)
            else:
                sp += 2
                veh += 1

        elif (j == 8):
            v.append(vehicle("E", 2))
            if (dir == "N"):
                dir = v[k].direction()
            else:
                pass
            flag = arange(r, j, "E", 2, r[i].x, rows, dir, i)
            if (flag == False):
                if (dir == 'L'):
                    r[i].waitL.append(j)
                elif (dir == 'S'):
                    r[i].waitS.append(j)
                else:
                    r[i].waitR.append(j)
            else:
                sp += 2
                veh += 1

        elif (j == 9):
            v.append(vehicle("B2", 1))
            if (dir == "N"):
                dir = v[k].direction()
            else:
                pass
            flag = arange(r, j, "B2", 1, r[i].x, rows, dir, i)
            if (flag == False):
                if (dir == 'L'):
                    r[i].waitL.append(j)
                elif (dir == 'S'):
                    r[i].waitS.append(j)
                else:
                    r[i].waitR.append(j)
            else:
                sp += 1
                veh += 1

        elif (j == 10):
            v.append(vehicle("C2", 1))
            if (dir == "N"):
                dir = v[k].direction()
            else:
                pass
            flag = arange(r, j, "C2", 1, r[i].x, rows, dir, i)
            if (flag == False):
                if (dir == 'L'):
                    r[i].waitL.append(j)
                elif (dir == 'S'):
                    r[i].waitS.append(j)
                else:
                    r[i].waitR.append(j)
            else:
                sp += 1
                veh += 1
        else:
            pass
        k += 1


def userInput():
    print("\n\tEnter the values in following format:- ")
    print("\n1) Write the word \'Road\' before the beginning of a new road followed by the space consumed on that road")
    print(
        "\n2) Then enter the option that explains the kind of the vehicle and the number followed tells the quantity of that vehicle consumed on a road")
    print("\n3) Make sure that the space entered by you is correct and exact else you will expeience a crash")
    print("\nOptions are as follows:- \n")
    print("\nPress 1 for Truck that consumes 5 units of space")  # T1
    print("\nPress 2 for Unloaded Troller that consumes 7 units of space")  # T31
    print("\nPress 3 for Loaded Troller that consumes 7 units of space")  # T32
    print("\nPress 4 for Unloaded Tanker that consumes 6 units of space")  # T21
    print("\nPress 5 for Loaded Tanker that consumes 6 units of space")  # T22
    print("\nPress 6 for Buses that consumes 5 units of space")  # B1
    print("\nPress 7 for Cars that consumes 2 units of space")  # C1
    print("\nPress 8 for E-Rickshaw that consumes 2 units of space")  # E
    print("\nPress 9 for Tempo that consumes 2 units of space")  # T4
    print("\nPress 10 for Bikes & Scooty that consumes 1 units of space")  # B2
    print("\nPress 11 for Cycles that consumes 1 units of space")  # C2

    print("\n\nStart Entering:- ")

    file = open("user-input.txt", "w")
    x = input()
    while (len(x) > 0):
        file.write(x)
        file.write("\n")
        x = input()
    file.close()

    file = open("user-input.txt", "r+")
    for x in file:
        if (x == '\n'):
            x = x.replace(x, "")
    file.close()

    return ("user-input.txt")


def main():
    now = datetime.now()
    current_time = now.strftime("%H")
    time = int(current_time)
    ch = 0
    print("\nPress 1 to Enter the values of Traffic for each road of the round about")
    print("\nPress 2 to Enter Default values of Traffic for each road of the round about")
    print("\nPress any key to Terminate")
    ch = int(input("\nEnter your choice:- "))
    if (ch == 1):
        file = open("record.txt", "a")
        file.write("\n")
        file.write(str(current_time))
        file.close()
        file2 = userInput()
        inflow(r, file2)
        recording(file2)
    elif (ch == 2):
        time = takeDefault(r)
    else:
        print("\n\n\tHope you liked it")
        quit()
    a = 0
    i = 0
    while (a < 4):
        i = 0
        while (i < 11):
            j = 0
            while (j < r[a].data[i]):
                r[a].unplaced.append(i)
                j += 1
            random.shuffle(r[a].unplaced)
            i += 1
        a += 1
    i = 0
    file = open("input.txt", "w")
    while (i < 4):
        sleep(2)
        print("\n\n\t\tDetails for road ", i + 1, " are:- ")
        file.write("\n\n\t\tDetails for road ")
        file.write(str(i + 1))
        file.write(" are:- \n")
        file.close()
        r[i].Display("input.txt")
        i += 1
        file = open("input.txt", "a")
    file.close()

    sleep(1.5)
    print("\n\nNomenclature of the vehicles for various Roads\n")
    print("\nT1 \t\tTruck")
    print("\nT21\t\tUnloaded Tanker")
    print("\nT22\t\tLoaded Tanker")
    print("\nT31\t\tUnloaded Troller")
    print("\nT32\t\tLoaded Troller")
    print("\nB1 \t\tBus")
    print("\nC1 \t\tCar")
    print("\nE  \t\tE-rickshaw")
    print("\nT4\t\tTempos")
    print("\nB2\t\tBikes & Scooties")
    print("\nC2\t\tCycles")
    sleep(5)

    i = 0
    while (i < 4):
        rows = 24
        v = []
        k = 0
        print("\nArranging the left lane waiting traffic")
        wait = r[i].waitL
        r[i].waitL = []
        sleep(2)
        getvehicle(v, wait, "L", rows, i)
        print("\nArranging the center lane waiting traffic")
        wait = r[i].waitS
        r[i].waitS = []
        sleep(2)
        getvehicle(v, wait, "S", rows, i)
        print("\nArranging the right lane waiting traffic")
        wait = r[i].waitR
        r[i].waitR = []
        sleep(2)
        getvehicle(v, wait, "R", rows, i)
        print("\nArranging the incoming traffic")
        getvehicle(v, r[i].unplaced, "N", rows, i)
        r[i].Merge()
        print("\n\tArrangement of road ", i + 1, " :-\n", r[i].x)
        i += 1

    print("\n\tIf Center Lane is moving Right\n")
    inCenterLaneMovingRight()
    print("\n\tRight Lane is Moving Straight\n")
    inRightLaneMovingStraight()

    i = 0
    while (i < 4):

        sleep(2)
        print("\n\n\n\n\t\tFor road ", (i + 1))
        j = 0
        while (j < 3):
            movementLane(r[i].x, rows, j, r[i].sp)
            j += 1
        i += 1

    mainSignal(r, time)
    i = 0
    file = open("output.txt", "w")
    while (i < 4):
        sleep(1.5)
        print("\n\tFor road ", i + 1)
        file.write("\n\tFor road ")
        file.write(str(i + 1))
        file.close()
        r[i].countveh("output.txt")
        file = open("output.txt", "a")
        print(r[i].x)
        file.write("\n")
        file.write(str(r[i].x))
        i += 1
    file.close()

    sleep(5)
    main()


r = []
data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
vehicles = 0
con = 0
space = 0
i = 0
while (i < 4):
    r.append(road(space, con, vehicles, data))
    i += 1
main()
