import os
import re
import copy
import sys

def prep_graph(file):
    with open(file,'r') as f:
        graph = f.read().split("\n")
    info = (int(graph[0][0]),int(graph[0][2]))
    edges = {}
    counter = 1
    count = 0 #to check how many edges have we added (per edge added, althought we make A->B,B->A, only counted once)
    graph.pop( len(graph) - 1 )
    while counter <= len(graph) - 1 :
        if int(graph[counter][0]) in edges:
            edges[ int(graph[counter][0]) ].append( int(graph[counter][2] ))
        else:
            edges[ int(graph[counter][0]) ] = [int(graph[counter][2])]
        if int(graph[counter][2]) in edges:
            edges[ int(graph[counter][2]) ].append( int(graph[counter][0] ))
        else:
            edges[ int(graph[counter][2]) ] = [int(graph[counter][0])]
        counter += 1
        count += 1 #to check if number of vertices added matches the given number
    if count != info[1]:
        print('Supposed number of edges and actual number of edges dont match')
    return info,edges

def prep_witness(file):
    with open(file,'r') as f:
        path = f.read().strip()
    path1 = list(path)
    res = []
    for i in path1:
        if i != ' ':
            res.append(int(i))
    return res

def vertice_verify(witness,number):
    wit = copy.deepcopy(witness)
    count = 0
    while count <= number - 1:
        try:
            wit.remove(count)
        except ValueError:
            return False
        count += 1
    if len(wit) == 0:
        return True
    else:
        return False

def hamilton(graph,witness):
    if vertice_verify(witness, graph[0][0]) == False:
        return False
    edges = graph[1]
    v1,v2 = 0,1
    while v2 <= len(witness) - 1:
        if witness[v2] in edges[ witness[v1] ]:
            v1 += 1
            v2 += 1
        else:
            return False
    if witness[0] in edges[ witness[v2 - 1]]:
        return True
    else:
        return False

def main():
    graph = prep_graph(sys.argv[1])
    witness = prep_witness(sys.argv[2])
    if hamilton(graph,witness) == True:
        print("witness")
    else:
        print('not a witness')

if __name__ == '__main__':
    main()