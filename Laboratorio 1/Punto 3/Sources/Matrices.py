import time
def One(n):
    M = []
    for i in range(0,n):
        M.append([])
        for j in range(0,n):
            M[i].append(1)

    return M
def Zero(n):
    M = []
    for i in range(0,n):
        M.append([])
        for j in range(0,n):
            M[i].append(0)
    return M

def Suma(lista):
    n = len(lista)
    suma = 0.0
    for i in range(0,n):
        suma = suma + lista[i]
    return suma / 10

def Dot(A,B):
    tstar = time.clock()
    n = len(A)
    a = 0
    for i in range(0,n):
        for j in range(0,n):
            a = a + A[i][j]+B[j][i]
    tend = time.clock()
    return tend - tstar

for i in range(0,501):
    A = One(i)
    B = Zero(i)
    times = []
    for j in range(0,10):
        tiempo = Dot(A,B)
        times.append(tiempo)
    print 'Tiempo Promedio para una matriz de tamanio:',i," ",Suma(times),' seconds'
