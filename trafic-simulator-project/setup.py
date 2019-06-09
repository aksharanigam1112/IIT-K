from os import system
import random
from time import sleep

while(1):
    i=random.randint(1,8)
    if(i==1):
        system("python Traffic.py <tests/test11.txt")
    elif(i==2):
        system("python Traffic.py <test/test12.txt")
    elif(i==3):
        system("python Traffic.py <test/test21.txt")
    elif(i==4):
        system("python Traffic.py <test/test22.txt")
    elif(i==5):
        system("python Traffic.py <test/test31.txt")
    elif(i==6):
        system("python Traffic.py <test/test32.txt")
    elif(i==7):
        system("python Traffic.py <test/test41.txt")
    else:
        system("python Traffic.py <test/test42.txt")
    sleep(10)

