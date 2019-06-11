from os import system

def inflow():
    r = road()
    s = Signal()

    print("\nEnter the road inflow ... 1")
    print("\nTake default values as the inflow ... 2")
    ch = int(input("\nEnter your choice:- "))

    if(ch==1):
        r.takeInput()     # Take the exact input for the road
        i=0
        while(i<4):
            s.lightGreen(i,r)
            i+=1
    if(ch==2):
        takeDefault()
        
    
def takeDefault():
    time  = int(input("\nEnter time in 24hour format"))
    if(time>=6 and time<=10):
        Morning()
    elif(time>=10 and time<=13):
        Noon()
    elif(time>=13 and time<=17):
        Evening()
    elif(time>=17 and time <=22):
        Night()
    elif(time>=22 and time <=6):
        Early()
    
def Early():
    system("python Traffic.py <test cases/22-6a.txt")
def Morning():
    system("python Traffic.py <test cases/6-10a.txt")
def Noon():
    system("python Traffic.py <test cases/10-13a.txt")
def Evening():
    system("python Traffic.py <test cases/13-17a.txt")
def Night():
    system("python Traffic.py <test cases/17-22a.txt")
    

