
#include <iostream>
using namespace std;

    short sFib(int x){
        short b = 0,a = 1,s = 0;
        for (int i = 0; i < x ; ++i) {
            s = a + b;
            a = b;
            b = s;
        }
        return s;
    }

    long lFib(int x){
        long b = 0,a = 1,s = 0;
        for (int i = 0; i < x ; ++i) {
            s = a + b;
            a = b;
            b = s;
        }
        return s;
    }

    long long loFib(int x){
        long long b = 0,a = 1,s = 0;
        for (int i = 0; i < x ; ++i) {
            s = a + b;
            a = b;
            b = s;
        }
        return s;
    }

    int iFib(int x){
        int b = 0,a = 1,s = 0;
        for (int i = 0; i < x ; ++i) {
            s = a + b;
            a = b;
            b = s;
        }
        return s;
    }
    int main() {
        int x;
        std::cout << "Ingrese Numero: " << std::endl;
        std::cin >> x;
        std::cout << "[int]Fibonacci:\t" << iFib(x) << std::endl;
        std::cout << "[short]Fibonacci:\t" << sFib(x) << std::endl;
        std::cout << "[long]Fibonacci:\t" << lFib(x) << std::endl;
        std::cout << "[long long]Fibonacci:\t" << loFib(x) << std::endl;

       return 0;
    }
