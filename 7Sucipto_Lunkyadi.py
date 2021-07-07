import copy
import sys

def read_graph(f):
    head = f.readline().split()
    n, m, k = [int(s) for s in head]

    graph = dict((i, []) for i in range(n))
    for j in range(m):
        edge = f.readline().split()
        u, v = [int(s) for s in edge]
        graph[u].append(v)
        graph[v].append(u)
    return graph, n, k

def test2(graph, vert, size):
    res = []
    current, working = [ [i] for i in range(vert) ], []
    for count in range( size - 1 ):
        for i in current:
            j = comp2(i, graph, vert)
            for k in j:
                working.append(k)
        current, working = copy.deepcopy(working), []
    return current

def comp2(obj, graph, vert):
    edges = set()
    res = []
    for i in obj:
        edges = edges | set( graph[i] )
    for j in range(obj[-1] + 1, vert):
        if j not in edges and len( set( graph[j] ) & set(obj) ) == 0:
            temp = copy.deepcopy(obj)
            temp.append(j)
            res.append(temp)
    return res

def check(filename):
    graph, vertices, size = read_graph( open(filename,'r'))
    non_adj = test2(graph,vertices,size)
    return non_adj

def main():
    a = check( sys.argv[1] )
    if len(a) == 0:
        print("No independent k-set")
    else:
        print( "A witness is -> " + str(a[0]) )

if __name__ == '__main__':
    main()