#include<iostream>
#include<bits/stdc++.h>
#include<time.h>
#include<stdlib.h>
using namespace std;

void define(char arr[25][3])
{
    for(int i=0;i<25;i++)
    {
        for(int j=0;j<3;j++)
            arr[i][j] = ' ';
    }
}
void arrange(int n , char ch , char arr[25][3] , int rows)
{
    int i , j;
    srand(time(NULL));
    while(n>0)
    {
        i = rand()%rows;
        j = rand()%3;
        if(arr[i][j]==' ')
        {
            arr[i][j] = ch;
            n--;
        }
    }
    
}
void display(char arr[25][3],int rows)
{
    for(int i=0;i<rows;i++)
    {
        for(int j=0;j<3;j++)
            cout<<" "<<arr[i][j];
        cout<<endl;
    }
}
void movementLeft()
{
    cout<<"\n\n\t\t If 1st Row th vehicle moves left";
    cout<<"\nJaam Causing Hindrances will occur in:- ";
    cout<<"\n1 2 3";
    cout<<"\nL R S";
    cout<<"\nL S L";
    cout<<"\n No Hinderances will occur in:- ";
    cout<<"\n1 2 3";
    cout<<"\nL S R";
    cout<<"\nL R R";
    cout<<"\nL S S";
    cout<<"\nL L S";
    cout<<"\nL L L";
}

void movementRight()
{
    cout<<"\n\n\t\t If 1st Row th vehicle moves right";
    cout<<"\nJaam Causing Hindrances will occur in:- ";
    cout<<"\n1 2 3";
    cout<<"\nR S R";
    cout<<"\nR R S";
    cout<<"\nR S L";
    cout<<"\nR L S";
    cout<<"\nR L L";
    cout<<"\n No Hinderances will occur in:- ";
    cout<<"\n1 2 3";
    cout<<"\nR R R";
    cout<<"\nR S S";
}

void movementStriaght()
{
    cout<<"\n\n\t\t If 1st Row th vehicle moves straight";
    cout<<"\nJaam Causing Hindrances will occur in:- ";
    cout<<"\n1 2 3";
    cout<<"\nS R S";
    cout<<"\nS R R";
    cout<<"\nS L L";
    cout<<"\nS L S";
    cout<<"\nS S L";
    cout<<"\n No Hinderances will occur in:- ";
    cout<<"\n1 2 3";
    cout<<"\nS S S";
    cout<<"\nS S R";
    cout<<"\nS R R";
}


/*int main()
{ 
    srand(time(NULL));
    char arr[25][3];
    define(arr);
    arrange(15,'T',arr,8);
    arrange(9,'C',arr,8);
    display(arr,8);
    return 0;
}*/
