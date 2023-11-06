#include <iostream>
#include <cmath>

using namespace std;


int N;
int count = 0;
int x[20];

bool place(int row, int col){
    for(int i= 1; i<=row; i++){
        if(x[i] == col || abs(x[i] - col) == abs( i - row))
            return false;
        
       
    }
  return true;
   
}


void printSolution(){
    cout<<"\n\nSolution\n\n"<<endl;
    for(int i= 1; i<=N; i++)
      cout<<"\t"<<i;
     for(int i= 1; i<=N; i++){
        cout<<"\n"<<i;
     
     for(int j = 1; j<=N; j++){
        if(x[i]==j)
          cout<<"\t Q";
          
        else
          cout<<"\t -"; 
     }
    
     }
      cout<<endl;
}
void NQueen(int row) {
    for (int col = 1; col <= N; col++) {
        if (place(row, col)) {
            x[row] = col;
            if (row == N)
                printSolution();
            else
                NQueen(row + 1);
        }
    }
}

int main(){
    cout << "\n ****** N-Queen Solution *****\n";
    
    cout << "\n Enter the Queen: ";
    cin >> N;
    NQueen(1);
    return 0;
}



