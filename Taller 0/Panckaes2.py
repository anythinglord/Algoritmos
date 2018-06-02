import itertools as it

def BFS(grafo,key):
    keys = []
    n = len(grafo)
    end = [1,2,3]
    for i in range(0,n):
        for t in range(0,len(grafo[key])):
            if grafo[key][t][1] == end:
                break
            print "llave: ",key,"in graph: ",grafo[key][t][1]

            keys.append(grafo[key][t][1])
        print
        print "keys: ",keys
        print
        for y in range(0,len(keys)):
            key = tuple(keys[y])
            print "before BFS: ",key
            BFS(grafo,key)

        #key = tuple(grafo[key][t][1])
        #BFS(grafo,key)
    return 0



def grafo(n):
    def combine(n):
        array = []
        for i in range(1,n+1):
            array.append(i)
        return list(it.permutations(array,n))

    def swap(array,t):
        n = len(array)
        arr = list(reversed(array[0:n-t]))
        return arr + list(array[n-t:n])

    G = {}
    D = []
    array = combine(n)
    for t in range(0,len(array)):
        for i in range(0,len(array[t])-1):
            D.append((i,swap(array[t],i)))
        G[array[t]] = D
        D = []
    return G


graph = grafo(3)
print BFS(graph,(1,3,2))
