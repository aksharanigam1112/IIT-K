#include<iostream>
#include<math.h>
#include<bits/stdc++.h>
#define size 75
#include "movement.cpp"
using namespace std;
class road
{
    public:
        int truck[4] = {4,30,0,0};
        int bus[4] = {3,35,0,0};
        int car[4] = {2,40,0,0};
        int tempo[4]={2,35,0,0};
        int bike[4] = {1,45,0,0};
        int cycle[4] = {1,20,0,0};
        int erick[4] = {2,25,0,0};

        int vehicles,space,rows;
        double con;
        char light , arr[25][3];

        road()
        {
            con=0;
            vehicles=0;
            //light = 'G';
        }

        void Display()
        {
            if(truck[2]!=0)
                cout<<"\nNo. of trucks = "<<truck[2]<<" & space consumed = "<<truck[3]<<endl;
            if(bus[2]!=0)
                cout<<"\nNo. of buses = "<<bus[2]<<" & space consumed = "<<bus[3]<<endl;
            if(car[2]!=0)
                cout<<"\nNo. of cars = "<<car[2]<<" & space consumed = "<<car[3]<<endl;
            if(tempo[2]!=0)
                cout<<"\nNo. of tempo = "<<tempo[2]<<" & space consumed = "<<tempo[3]<<endl;
            if(erick[2]!=0)
                cout<<"\nNo. of trucks = "<<erick[2]<<" & space consumed = "<<erick[3]<<endl;
            if(bike[2]!=0)
                cout<<"\nNo. of bikes & scooties = "<<bike[2]<<" & space consumed = "<<bike[3]<<endl;
            if(cycle[2]!=0)
                    cout<<"\nNo. of cycles = "<<cycle[2]<<" & space consumed = "<<cycle[3]<<endl;  
            
            vehicles = truck[2]+bus[2]+car[2]+tempo[2]+erick[2]+bike[2]+cycle[2];
            cout<<"\nTotal Vehicles = "<<vehicles;
            cout<<"\nCongestion = "<<con;
        }
};

/*class Signal
{
    public:
    int dur;
    vector < pair<int,double,char> >v;
    void Signal(road r[4])
    {
        dur=60;
        for(int i=0;i<4;i++)
        {
            v.insert(i+1 , r[i].con , r[i].light);
        }
    }

    void DispQueue()
    {
        vector<pair<int,double,char> > :: iterator it1= v.begin();
        vector<int,double,char>::iterator it2;
        while(it1!=v.end())
        {
            it2 = it1->begin();
            while(it2!=it1->end())
            {
                cout<<*it2;
                it2++;
            }
            it1++;
        }
    }
    void TrafficLight()
    {
        
    }
};*/

int main()
{
    srand(time(NULL));
    road r[4];
    int ch;
    for(int i=0;i<4;i++)
    {
        int p=100;
        cout<<"\n\t\tEnter the details for road "<<(i+1);
        cout<<"\n\tUnit of space occupied:- ";
        cin>>r[i].space;
        r[i].con = double(r[i].space)/size;
        
        do
        {
            cout<<"\n\tTruck...1";
            cout<<"\n\tBuses...2";
            cout<<"\n\tCars...3";
            cout<<"\n\tE-Rickshaw...4";
            cout<<"\n\tTempo...5";
            cout<<"\n\tBikes & Scooty...6";
            cout<<"\n\tCycles...7";
            cout<<"\nEnter your choice:- ";
            cin>>ch;
            switch (ch)
            {
            case 1:
                cout<<"\nEnter the number of trucks:- ";
                cin>>r[i].truck[2];
                r[i].truck[3] = r[i].truck[2] * r[i].truck[0];
                r[i].space-=r[i].truck[3];
                break;
            case 2:
                cout<<"\nEnter the number of buses:- ";
                cin>>r[i].bus[2];
                r[i].bus[3] = r[i].bus[2] * r[i].bus[0];
                r[i].space-=r[i].bus[3];
                break;
            case 3:
                cout<<"\nEnter the number of cars :- ";
                cin>>r[i].car[2];
                r[i].car[3] = r[i].car[2] * r[i].car[0];
                r[i].space-=r[i].car[3];
                break;
            case 4:
                cout<<"\nEnter the number of E-rickshaw:- ";
                cin>>r[i].erick[2];
                r[i].erick[3] = r[i].erick[2] * r[i].erick[0];
                r[i].space-=r[i].erick[3];
                break;
            case 5:
                cout<<"\nEnter the number of Tempos:- ";
                cin>>r[i].tempo[2];
                r[i].tempo[3] = r[i].tempo[2] * r[i].tempo[0];
                r[i].space-=r[i].tempo[3];
                break;
            case 6:
                cout<<"\nEnter the number of Bikes & scooty:- ";
                cin>>r[i].bike[2];
                r[i].bike[3] = r[i].bike[2] * r[i].bike[0];
                r[i].space-=r[i].bike[3];
                break;
            case 7:
                cout<<"\nEnter the number of Cycles:- ";
                cin>>r[i].cycle[2];
                r[i].cycle[3] = r[i].cycle[2] * r[i].cycle[0];
                r[i].space-=r[i].cycle[3];
                break;
            }
            
        } while (r[i].space>0);
    }

    for(int i=0;i<4;i++)
    {
        cout<<"\n\n\t\tDetails for road "<<(i+1)<<" are:- "<<endl;
        r[i].Display();
    }

    /*int source , destination,l;
    cout<<"\n\nEnter source & destination :- ";
    cin>>source>>destination;*/
    int l;

    cout<<"\nEnter the total no. of psuedo-lanes (not more than 3):- ";
    cin>>l;
    
    cout<<"\nTest 0";
    for(int i=0;i<4;i++)
    {
        cout<<"\nTest 1";
        r[i].rows = (int)(ceil(r[i].vehicles/l));
        define(r[i].arr);
        
        cout<<"\nTest 2";
        if(r[i].truck[2]>0)
            arrange(r[i].truck[2] , 'T', r[i].arr , r[i].rows);
        cout<<"\nTest 3";
        if(r[i].bus[2]>0)
            arrange(r[i].bus[2] , 'B', r[i].arr , r[i].rows);
        cout<<"\nTest 4";
        if(r[i].car[2]>0)
            arrange(r[i].car[2] , 'C', r[i].arr , r[i].rows);
        cout<<"\nTest 5";
        if(r[i].tempo[2]>0)
            arrange(r[i].tempo[2] , 't', r[i].arr , r[i].rows);
        cout<<"\nTest 6";
        if(r[i].erick[2]>0)
            arrange(r[i].erick[2] , 'E', r[i].arr , r[i].rows);
        cout<<"\nTest 7";
        if(r[i].bike[2]>0)
            arrange(r[i].bike[2] , 'b', r[i].arr , r[i].rows);
        cout<<"\nTest 8";
        if(r[i].cycle[2]>0)
         arrange(r[i].cycle[2] , 'c', r[i].arr , r[i].rows);

        cout<<"\n\tArrangement of road "<<(i+1)<<" is :- "<<endl;
        display(r[i].arr , r[i].rows);
    }
    

    /*Signal s(r);
    s.DispQueue();*/
    return 0;
}
