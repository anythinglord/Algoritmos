# itertools
import itertools as iter

def insert(array):
    size = len(array)
    values = [0,0,1]
    key = 1
    entry = False
    while (key < size):
        i = key
        j = i - 1
        while (j > -1):
            values[1] = values[1]+1
            if array[i] < array[j]:
                entry = True
                values[2] = values[2] + 1
                aux = array[j]
                array[j] = array[i]
                array[i] = aux
            i = i - 1
            j = i - 1
        key = key + 1
    if entry == True:
        values[0] = (values[0]+6)*key+2
    else:
        values[0] = (values[0]+3)*key+2
    return [array,values]

def generate(array,limit):
    stat = []
    lista = []
    for e in iter.permutations(array,limit):
        lista = list(e)
        print "Permutacion: ",lista
        stat = insert(lista)
        print "instruccions: ",stat[1][0]
        print "comparisons: ",stat[1][1]
        print "Swaps: ",stat[1][2]


n = 6
for i in range(2,n+1):
    array = []
    for j in range(0,i):
        array.append(j)
    generate(array,i)


