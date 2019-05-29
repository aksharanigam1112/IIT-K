#include<iostream>
#include<math.h>
#include<bits/stdc++.h>
#define size 75
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

        int vehicles,space ;
        double con;
        char light;

        road()
        {
            con=0;
            vehicles=0;
            //light = 'G';
        }

        void total()
        {
            vehicles = truck[2]+bus[2]+car[2]+tempo[2]+erick[2]+bike[2]+cycle[2];
            con = (truck[3]+bus[3]+car[3]+tempo[2]+erick[3]+bike[3]+cycle[3])/size;
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
    road r[4];
    int ch;
    for(int i=0;i<4;i++)
    {
        int p=100;
        cout<<"\n\t\tEnter the details for road "<<(i+1);
        cout<<"\n\tUnit of space occupied:- ";
        cin>>r[i].space;
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
                break;
            case 2:
                cout<<"\nEnter the number of buses:- ";
                cin>>r[i].bus[2];
                r[i].bus[3] = r[i].bus[2] * r[i].bus[0];
                break;
            case 3:
                cout<<"\nEnter the number of cars :- ";
                cin>>r[i].car[2];
                r[i].car[3] = r[i].car[2] * r[i].car[0];
                break;
            case 4:
                cout<<"\nEnter the number of E-rickshaw:- ";
                cin>>r[i].erick[2];
                r[i].erick[3] = r[i].erick[2] * r[i].erick[0];
                break;
            case 5:
                cout<<"\nEnter the number of Tempos:- ";
                cin>>r[i].tempo[2];
                r[i].tempo[3] = r[i].tempo[2] * r[i].tempo[0];
                break;
            case 6:
                cout<<"\nEnter the number of Bikes & scooty:- ";
                cin>>r[i].bike[2];
                r[i].bike[3] = r[i].bike[2] * r[i].bike[0];
                break;
            case 7:
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

    int source , destination,l,rows;
    cout<<"\n\nEnter source & destination :- ";
    cin>>source>>destination;

    cout<<"\nEnter the total no. of psuedo-lanes (not more than 3):- ";
    cin>>l;

    rows = (int)(ceil(r[0].vehicles/l);

    /*Signal s(r);
    s.DispQueue();*/
    return 0;
}