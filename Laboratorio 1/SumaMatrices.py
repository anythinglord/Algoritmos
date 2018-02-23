import time
import random

def Sum(A , B):
    top = 0
    t0 = time.clock()
    for i in range(0,tam):
        for j in range(0,tam):
            sum = A[i][j] + B[i][j]
            top = time.clock()
            top = top - t0
    total = time.clock()
    return [total,top]


tam = input("Tamanio de la matriz: ")

A = []
for i in range(0,tam):
    A.append([])
    for j in range(0,tam):
        num = random.randrange(20)
        A[i].append(num)

totalS = Sum(A , A)
print "Suma: "
print "Tiempo de cada suma: " + str(totalS[1])
print "Tiempo total de la suma: " + str(totalS[0])
print " "

