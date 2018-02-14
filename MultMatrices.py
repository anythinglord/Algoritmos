import time
import random


def Mult(A , B):
    top = 0
    t0 = time.clock()
    mul = 0
    for i in range(0,tam):
        for j in range(0,tam):
            mul = A[i][i]*B[i][j] + A[i][j]*B[j][i]
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

totalM = Mult(A, A)
print "Multiplicacion: "
print "Tiempo de cada Multiplicacion: " + str(totalM[1])
print "Tiempo total de la Multiplicacion: " + str(totalM[0])
