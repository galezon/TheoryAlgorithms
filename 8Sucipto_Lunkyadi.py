import sys
import pulp
import copy

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

def check(filename, temp_size):
    graph, vertices, size = read_graph( open(filename,'r'))
    non_adj = test2(graph,vertices, temp_size)
    return non_adj

def read_graph2( file ):
    with open(file, 'r') as f:
        a = f.read()
    b = a.split('\n')
    c = b[0].split(' ')
    vertices = c[0]
    res = [tuple( i.split(' ') )  for i in b ]
    res.pop(0)
    res.pop(-1)
    return res, vertices

def maxind(file):
    edges, vertices = read_graph2( file )
    variables = [ pulp.LpVariable( str(i), lowBound=0, cat=pulp.LpInteger) for i in range( int(vertices) )]
    problem = pulp.LpProblem( 'maxind', pulp.LpMaximize)
    problem += pulp.lpSum(variables)
    for i in edges:
        problem += variables[ int(i[0]) ] + variables[ int(i[1]) ] <= 1
    problem.solve()
    return pulp.value(problem.objective)

def main():
    maks = int( maxind( sys.argv[1] ) )
    a = check( sys.argv[1] , maks )
    print( 'MaxInd =', str( maks ), ', Proof ->', a[0], sep=' ') 
if __name__ == '__main__' :
    main()