#include <bits/stdc++.h> 
using namespace std; 
  
int main() 
{ 
    ifstream file1 , file2;
    ofstream file3; 
    string word1 , word2;
    file1.open("t1.txt"); 
    file2.open("t2.txt");
    file3.open("t3.txt");

    while (file1>>word1 && file2>>word2) 
    { 
        file3<<word1<<" "<<word2<<endl; 
    } 
    
    while(getline(file1,word1))
            file3<<word1<<endl;
    
    while(getline(file2,word2))
    {
            file3<<word2<<endl;
    }
            
    cout<<"Writing done\n";
    file1.close();
    file2.close();
    file3.close();
    system("gedit t3.txt");
    return 0; 
} 