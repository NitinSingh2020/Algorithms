# Author     : Nitin Singh
# Dependency : kargerMinCut.txt
# Execution  : python kargerMinCut.py

import random, copy

def loadAdjList():
    """
    returns: G a dictionary keys are the vertices and values are the adjacent
             nodes
    """
    fin= open("kargerMinCut.txt")
    G={}
    for line in fin: # load data, create adj lists
        lst=[]
        row = line.split('\t')
        for i in range(len(row)-2):
            lst.append(int(row[i+1]))
        G[int(row[0]) ]=lst
    return G

def chooseRandomEdge(G): #return an edge represented by 2 ints
    """
    G       : adj list of the graph, G is a python dictionary
    returns : a randomly chosen edge identified by its end points v1 and v2
    """
    v1= G.keys() [random.randint(0,len(G)-1)]
    v2= G[v1] [random.randint(0,len(G[v1])-1)]
    return v1, v2


def kargerStep(G):
    """
    G       : adj list of the graph, G is a python dictionary
    returns : nothing, modifies G per one Karger step
    """
    v1,v2= chooseRandomEdge(G)
    #1. attach v2's list to v1
    G[v1].extend(G[v2])
    #2. replace all appearance of v2 as v1
    for x in G[v2]:
        lst=G[x]
        for i in range(0,len(lst)):
            if lst[i]==v2: lst[i]=v1        
    #3.remove self-loop
    while v1 in G[v1]:
        G[v1].remove(v1)
    #4. remove v2's list
    del G[v2]

def karger(G): 
    while len(G)>2: kargerStep(G)
    return len(G[G.keys()[0]])

if __name__ == "__main__":
    min=karger(copy.deepcopy(loadAdjList()))
    for i in range(0,1000): # run many tests
        instance = karger(copy.deepcopy(loadAdjList()))
        # s = 'Min cuts in iteration #' + str(i) + ' are ' + str(instance) + \
        #     ' Min value untill now is ' + str(min)
        # print s
        if instance<min: min=instance 
    print '# of min cuts are: ',min