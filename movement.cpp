#include<iostream>
#include<bits/stdc++.h>
#include<time.h>
#include<stdlib.h>
using namespace std;
int hinder,rows=8;
//array<array<char,3>,8 > arr;
void arrange(int n , char ch)
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
void display()
{
    for(int i=0;i<rows;i++)
    {
        for(int j=0;j<3;j++)
            cout<<" "<<arr[i][j];
        cout<<endl;
    }
}
void movement3()
{

}

int main()
{ 
    arrange(15,'T');
    arrange(9,'C');
    display();
    return 0;
}