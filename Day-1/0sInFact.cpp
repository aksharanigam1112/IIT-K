#include<iostream>
#include<math.h>
using namespace std;

int main()
{
    long long num;
    cout<<"\nEnter a number:- ";
    cin>>num;
    long long ctr=0;
    
    for (long long i = 5; (num/i)>=1 ; i*=5) 
    {
            ctr = ctr + floor(num/i);
    }
    cout<<"\nTrailing zeroes are:- "<<ctr<<endl;
    return 0;
}
