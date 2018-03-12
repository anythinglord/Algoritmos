array = [0,1,2,3,4,5]

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

def swap(array,i,j):
    t = array[i]
    array[i] = array[j]
    array[j] = t
def copia(array):
    v = []
    for i in range(0,len(array)):
        v.append(array[i])
    return v

def perm(array,i,n):
    array2 = []
    if i == n:
        print "permutacion: ",array
        array2 = copia(array)
        stat = insert(array2)
        print "sorted: ",stat[0]
        print "instruccions: ",stat[1][0]
        print "comparisons: ",stat[1][1]
        print "Swaps: ",stat[1][2]

    else:
        for j in range(i,n):
            swap(array,i,j)
            perm(array,i+1,n)
            swap(array,i,j)


perm(array,0,6)
