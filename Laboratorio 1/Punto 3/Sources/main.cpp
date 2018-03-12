#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

int A[200][200];
int B[200][200];
double Tiempos[200];


void Dot(int n){
    clock_t t0,tf;
    t0 = clock();
    double suma = 0;
    int h = 0;
    for (int i =0;i<10;i++){
        for (int a =0;a<10;a++){
            for (int b =0;b<10;b++){
                h = h + (A[a][b]*B[b][a]);
            }
        }
        tf = clock();
        suma = suma + (tf - t0);
    }
    Tiempos[n-1] = suma / 10;
}

int main()
{
    for(int i=1;i<200;i++){
        for(int j= 1;j<200;j++){
            A[i][j] = 0;
            B[i][j] = 1;
        }
    }
    for(int t=1;t<200;t++){
        Dot(t);
    }
    cout<<"[";
    for(int i=0;i<200;i++){
        cout<<Tiempos[i]<<",";
    }
    cout<<"]"<<endl;

    cout<<"[";
    for(int i=0;i<200;i++){
        cout<<i<<",";
    }
    cout<<"]"<<endl;
    return 0;
}
