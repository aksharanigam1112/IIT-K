from test import recording

def takeDefault():
    time  = int(input("\nEnter time in 24hour format:- "))
    if(time>=6 and time<=10):
        Morning()
    elif(time>=10 and time<=13):
        Noon()
    elif(time>=13 and time<=17):
        Evening()
    elif(time>=17 and time <=22):
        Night()
    elif((time>=22 and time<=24) or (time >=1 and time<6)):
        Early()
    
def Early():
    file = "test cases/22-6a.txt"
    file1 = open("record.txt","a")
    file1.write("\n22-6")
    file1.close()
    recording(file)
def Morning():
    file= "test cases/6-10a.txt"
    file1 = open("record.txt","a")
    file1.write("\n6-10")
    file1.close()
    recording(file)
def Noon():
    file="test cases/10-13a.txt"
    file1 = open("record.txt","a")
    file1.write("\n10-13")
    file1.close()
    recording(file)
def Evening():
    file="test cases/13-17a.txt"
    file1 = open("record.txt","a")
    file1.write("\n13-17")
    file1.close()
    recording(file)
def Night():
    file="test cases/17-22a.txt"
    file1 = open("record.txt","a")
    file1.write("\n17-22")
    file1.close()
    recording(file)
    
takeDefault()
