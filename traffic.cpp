#include<iostream>
#include<math.h>
#include<bits/stdc++.h>
//#define inf 9999
//#define n 7
#define size 75
using namespace std;
class road
{
    public:
        int truck[4] = {4,30,0,0};
        int bus[4] = {3,35,0,0};
        int ct[4] = {2,40,0,0};
        int bike[4] = {1,45,0,0};
        int cycle[4] = {1,20,0,0};
        int erick[4] = {2,25,0,0};

        int vehicles ;
        double con;
        char light;

        road()
        {
            con=0;
            vehicles=0;
            light = 'G';
        }

        void total()
        {
            vehicles = truck[2]+bus[2]+ct[2]+erick[2]+bike[2]+cycle[2];
            con = (truck[3]+bus[3]+ct[3]+erick[3]+bike[3]+cycle[3])/size;
        }
        void Display()
        {
            if(truck[2]!=0)
                cout<<"\nNo. of trucks = "<<truck[2]<<" & space consumed = "<<truck[3]<<endl;
            if(bus[2]!=0)
                cout<<"\nNo. of buses = "<<bus[2]<<" & space consumed = "<<bus[3]<<endl;
            if(ct[2]!=0)
                cout<<"\nNo. of cars & tempos = "<<ct[2]<<" & space consumed = "<<ct[3]<<endl;
            if(erick[2]!=0)
                cout<<"\nNo. of trucks = "<<erick[2]<<" & space consumed = "<<erick[3]<<endl;
            if(bike[2]!=0)
                cout<<"\nNo. of bikes & scooties = "<<bike[2]<<" & space consumed = "<<bike[3]<<endl;
            if(cycle[2]!=0)
                    cout<<"\nNo. of cycles = "<<cycle[2]<<" & space consumed = "<<cycle[3]<<endl;  
            cout<<"\nTotal Vehicles = "<<vehicles;
            cout<<"\nCongestion = "<<con;
        }

/*double graph[n][n] = {    {inf,4,inf,inf,2,inf,inf},
                        {4,inf,3,inf,inf,inf,inf},
                        {inf,3,inf,5,4,7,inf},
                        {inf,inf,5,inf,inf,inf,3},
                        {2,inf,3,inf,inf,1,inf},
                        {inf,inf,7,inf,1,inf,4},
                        {inf,inf,inf,3,inf,4,inf}
                    };
double traffic[n][n] = {  {inf,0.8,inf,inf,1,inf,inf},
                        {3,inf,1.5,inf,inf,inf,inf},
                        {inf,0.2,inf,2,0.4,4,inf},
                        {inf,inf,2.5,inf,inf,inf,1.7},
                        {1.3,inf,2.5,inf,inf,0,inf},
                        {inf,inf,6,inf,0.3,inf,2},
                        {inf,inf,inf,1.2,inf,2.7,inf}
                    };*/
};

class Signal
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
    /*void TrafficLight()
    {
        
    }*/
};

int main()
{
    road r[4];
    int ch;
    for(int i=0;i<4;i++)
    {
        cout<<"\n\t\tEnter the details for road "<<(i+1);
        do
        {
            cout<<"\n\tTruck...1";
            cout<<"\n\tBuses...2";
            cout<<"\n\tCars & Tempos...3";
            cout<<"\n\tE-Rickshaw...4";
            cout<<"\n\tBikes & Scooty...5";
            cout<<"\n\tCycles...6";
            cout<<"\nEnter your choice:- ";
            cin>>ch;
            switch (ch)
            {
            case 1:
                cout<<"\nEnter the number of trucks:- ";
                cin>>r[i].truck[2];
                r[i].truck[3] = r[i].truck[2] * r[i].truck[0];
                break;
            case 2:
                cout<<"\nEnter the number of buses:- ";
                cin>>r[i].bus[2];
                r[i].bus[3] = r[i].bus[2] * r[i].bus[0];
                break;
            case 3:
                cout<<"\nEnter the number of cars & tempos:- ";
                cin>>r[i].ct[2];
                r[i].ct[3] = r[i].ct[2] * r[i].ct[0];
                break;
            case 4:
                cout<<"\nEnter the number of E-rickshaw:- ";
                cin>>r[i].erick[2];
                r[i].erick[3] = r[i].erick[2] * r[i].erick[0];
                break;
            case 5:
                cout<<"\nEnter the number of Bikes & scooty:- ";
                cin>>r[i].bike[2];
                r[i].bike[3] = r[i].bike[2] * r[i].bike[0];
                break;
            case 6:
                cout<<"\nEnter the number of Cycles:- ";
                cin>>r[i].cycle[2];
                r[i].cycle[3] = r[i].cycle[2] * r[i].cycle[0];
                break;
            }
            cout<<"\nDo you want to enter more? Yes...1 No...0 ";
            cin>>ch;
        } while (ch==1);
    }

    for(int i=0;i<4;i++)
    {
        cout<<"\n\n\t\tDetails for road "<<(i+1)<<" are:- "<<endl;
        r[i].Display();
    }

    Signal s(r);
    s.DispQueue();


    return 0;
}
