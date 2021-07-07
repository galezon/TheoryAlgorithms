import copy

def read_graph(f):
    """
    Read a graph from a text file.

    :param f: the file to read
    :return: the edge-list, the starting and final vertex of path
    """

    header = f.readline().split()
    n, m, from_where, to_where = [int(s) for s in header]

    graph = dict((i, []) for i in range(n))
    for j in range(m):
        edge = f.readline().split()
        u, v = [int(s) for s in edge]
        graph[u].append(v)

    return graph, from_where, to_where

def vertice_in_graph(graph,vertice):
    g = []
    for i in graph:
        for j in graph[i]:
            g.append(j)
    if vertice not in g:
        return False

def one_layer(dict,keylist):
    #intended to work with a dictionary, keylist is the current path so far, returns the possible next edge to go through
    res = []
    temp_list = copy.deepcopy(keylist)
    if len(dict[keylist[-1]]) != 0:
        for i in dict[ keylist[-1] ]:
            if i in keylist: #If i is in the keylist, then there is a cycle, so we skip it
                continue
            temp_list.append(i)
            res.append( copy.deepcopy(temp_list) ) 
            temp_list.remove(i)
    else:
        return keylist
    return res

def search(graph,fr,to):
    
    if fr == to:
        return [fr]
    fr = [fr]
    a = one_layer(graph,fr)
    while True:
        res = []
        for i in a:
            if i[-1] != to: #now i = [0,1,2]
                temp = copy.deepcopy( one_layer(graph,i) )
                if temp == i: #to catch if there are no forward edges from Vertex= i[-1]
                    res.append(i)
                    continue
                for j in temp:
                    if j[-1] == to:
                        return j
                    res.append(j)
            else:
                return i
        if a == res:  #the idea is that if there are no further edges from ALL the paths we have, then just exit
            return(False) 
        a = copy.deepcopy(res)
        

def search_path(graph, from_where, to_where):
    """
    Search a shortest path between the two vertices.

    :param graph: the edge-list of the graph
    :param from_where: starting vertex of the path
    :param to_where: final vertex of the path
    :return: a list of vertices of the shortest path if it exists, 
             and False otherwise
    """

    if vertice_in_graph(graph,to_where) == False:
        return('v')
    return (search(graph, from_where, to_where) )

if __name__ == '__main__':

    import sys

    with open(sys.argv[1], 'r') as f:
        graph, from_where, to_where = read_graph(f)
    path = search_path(graph, from_where, to_where)
    if path == 0:
        print('no path')
    elif path == 'v':
        print('vertice not in graph')
    else:
        print('path: ' + ' -> '.join(str(i) for i in path))
 