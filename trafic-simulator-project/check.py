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
        r.takeDefault(vehicles)
        
    
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
    # run the test case for this time slot
def Morning():
    # run the test case for this time slot
def Noon():
    # run the test case for this time slot
def Evening():
    # run the test case for this time slot
def Night():
    # run the test case for this time slot
    

