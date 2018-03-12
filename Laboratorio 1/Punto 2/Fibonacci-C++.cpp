
#include <iostream>
#include <limits.h>

using namespace std;

   long int loFib(int x){
    long int b = 0,a = 1,s = 0;
    for (int i = 0; i < x ; ++i) {
        s = a + b;
        a = b;
        b = s;
    }
    return s;
}


int main() {

    int a;
    int b;
    int c;
    long l = 0;

    short sh_max = SHRT_MAX;
    int int_max = INT_MAX;
    long long_max = LONG_MAX;
    //long long llong_max = LLONG_MAX;

    for(int i = 0; i< 100 ;i++){

        l = loFib(i);
        if((l > sh_max) & (a == 0)){
            std::cout << "OverFlow in short : \t" << i << std::endl;
            a = 1;
        }
        if((l > int_max) & (b == 0)){
            std::cout << "OverFlow in int : \t" << i << std::endl;
            b = 1;
        }
        if((l > long_max) & (c == 0)){
            std::cout << "OverFlow in long : \t" << i << std::endl;
            c = 1;
        }
    }
    return 0;
}

