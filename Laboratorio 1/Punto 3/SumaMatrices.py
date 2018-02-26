import time
import numpy as np
import matplotlib.pyplot as pl

def Sum(A , B,tam):
    top = 0
    t0 = time.clock()
    for i in range(0,tam):
        for j in range(0,tam):
            A[i][j] + B[i][j]
            top = time.clock()
            top = top - t0
    total = time.clock()
    return [total,top]


tiempo = []
number = []
t = 0.0
for i in range(0,100):
    for j in range(0,10):
        A = np.ones((i,i))
        B = 2*np.ones((i,i))
        totalM = Sum(A, B, i)
        s = totalM[1]
        t = t + float(s)
        print t
    tiempo.append(t/10)
    number.append(i)


numero = np.array(number)
tiempo = np.array(tiempo)

x = pl.ylabel("Tiempo")
y = pl.xlabel('Numero')

pl.plot(numero,tiempo)
pl.show()

