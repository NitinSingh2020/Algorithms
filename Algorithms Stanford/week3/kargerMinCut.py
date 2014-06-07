"""
Author     : Nitin Singh
Dependency : kargerMinCut.txt
Execution  : python kargerMinCut.py
"""

import random, copy

def loadAdjList():
    """
    returns: graph a dictionary keys are the vertices and values are the adjacent
             nodes
    """
    fin = open("kargerMinCut.txt")
    graph = {}
    for line in fin: # load data, create adj lists
        lst = []
        row = line.split('\t')
        for i in range(len(row)-2):
            lst.append(int(row[i+1]))
        graph[int(row[0])] = lst
    return graph

def chooseRandomEdge(graph): #return an edge represented by 2 ints
    """
    graph   : adj list of the graph, graph is a python dictionary
    returns : a randomly chosen edge identified by its end points v1 and v2
    """
    v1 = graph.keys()[random.randint(0, len(graph)-1)]
    v2 = graph[v1][random.randint(0, len(graph[v1])-1)]
    return v1, v2


def kargerStep(graph):
    """
    graph   : adj list of the graph, graph is a python dictionary
    returns : nothing, modifies graph per one Karger step
    """
    v1, v2 = chooseRandomEdge(graph)
    #1. attach v2's list to v1
    graph[v1].extend(graph[v2])
    #2. replace all appearance of v2 as v1
    for x in graph[v2]:
        lst = graph[x]
        for i in range(0, len(lst)):
            if lst[i] == v2: lst[i] = v1
    #3.remove self-loop
    while v1 in graph[v1]:
        graph[v1].remove(v1)
    #4. remove v2's list
    del graph[v2]

def karger(graph):
    """
    Main function
    """
    while len(graph) > 2: kargerStep(graph)
    return len(graph[graph.keys()[0]])

if __name__ == "__main__":
    min = karger(copy.deepcopy(loadAdjList()))
    for i in range(0, 10): # run many tests
        instance = karger(copy.deepcopy(loadAdjList()))
        # s = 'Min cuts in iteration #' + str(i) + ' are ' + str(instance) + \
        #     ' Min value untill now is ' + str(min)
        # print s
        if instance < min: min = instance
    print '# of min cuts are: ', min
