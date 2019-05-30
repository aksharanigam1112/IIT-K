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
/*void movement3()
{

}*/

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
