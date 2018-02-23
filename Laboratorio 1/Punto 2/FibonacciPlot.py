import numpy as np
import matplotlib.pyplot as pl
import time

numero1 = []
tiempo1 = []
n=100

def fib(n):
    if n==0 :
        return 0
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a+b
    return b

for j in range(1,100):
    t01 = time.clock()
    k1 = fib(j)
    numero1.append(k1)
    tf1 = time.clock()
    tiempo1.append(tf1-t01)

print("n=",n,"fib(",n,")=",k1,"time",tf1 - t01, "seconds process time")



numero2 = []
tiempo2 = []

def fibR(n):
    if n==0 :
        return 0
    if n==1 :
        return 1
    return fibR(n-1)+fibR(n-2)

for t in range(1,100):
    t02 = time.clock()
    k2 = fib(t)
    numero2.append(k2)
    tf2 = time.clock()
    tiempo2.append(tf2-t02)

print("n=",n,"fib(",n,")=",k2,"time",tf2 - t02, "seconds tiempo de proceso")

Nnumero1 = np.array(numero1)
Ntiempo1 = np.array(tiempo1)


Nnumero2 = np.array(numero2)
Ntiempo2 = np.array(tiempo2)


x = pl.ylabel("Tiempo")
y = pl.xlabel('Numero')
pl.plot(Nnumero1,Ntiempo1,Nnumero2,Ntiempo2)
pl.show()


