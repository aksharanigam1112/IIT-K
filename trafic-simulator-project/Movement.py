import numpy as np
import random

x = np.chararray((25,3))
x[:] = ''

def arange(n, ch, x, rows, col):
    while(n>0):
        i = random.randint(0,rows-1)
        j = random.randint(0,col-1)
        if(x[i][j] == ''):
            x[i][j] = ch
            n -= 1
    return x

c = arange(10,'T',x,25,3)
print(c)

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

def movementStriaght():
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

