from os import system

def recording(file):
    
    i = 0
    vehicles = 0
    con = 0
    prev = "x"
    file1 = open(file, "r")
    file2 = open("record.txt","a")
    data = []
    space = 0

    for x in file1 :
        
        if(x == "Road\n"):
        
            prev = x
        
            if(i != 0):
        
                file2.write("\nRoad ")
                file2.write(str(i))
                file2.write("\tSpace:- ")
                file2.write(str(space))
                i += 1
                shuffle = [0,0,0,0,0,0,0,0,0,0,0]
                vehicles = 0
                con = space / 75
                j = 0

                while(j < data.__len__() - 1):
                    
                    shuffle[data[j] - 1] = data[j + 1]
                    vehicles += data[j + 1]
                    j += 2

                file2.write("\t")
                file2.write(str(shuffle))
                file2.write("\tVehicles:- ")
                file2.write(str(vehicles))
                file2.write("\tCongession:- ")
                file2.write(str(con))
            
            else:
            
                i += 1
            
            data = []
            space = 0

        elif(prev == "Road\n"):
            
            space = int(x)
            prev = x

        else:

            data.append(int(x))

    file2.write("\nRoad ")
    file2.write(str(i))
    file2.write("\tSpace:- ")
    file2.write(str(space))
    vehicles = 0    
    shuffle = [0,0,0,0,0,0,0,0,0,0,0]        
    j = 0

    while(j < data.__len__() - 1):
        
        shuffle[data[j] - 1] = data[j + 1]
        vehicles += data[j + 1]
        j += 2
    
    con = space / 75

    file2.write("\t")
    file2.write(str(shuffle))
    file2.write("\tVehicles:- ")
    file2.write(str(vehicles))
    file2.write("\tCongession:- ")
    file2.write(str(con)) 
    file1.close()
    file2.close()