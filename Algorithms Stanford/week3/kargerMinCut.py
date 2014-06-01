import random, copy
fin= open("kargerMinCut.txt")#.read().splitlines()

G={}
for line in fin: # load data, create adj lists
    lst=[]
    row = line.split('\t')
    for i in range(len(row)-2):
        lst.append(int(row[i+1]))
    G[int(row[0]) ]=lst
print(G)

def chooseRandomEdge(G): #return an edge represented by 2 ints
    v1= G.keys() [random.randint(0,len(G)-1)]
    v2= G[v1] [random.randint(0,len(G[v1])-1)]
    return v1, v2


def kargerStep(G):
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

min=karger(copy.deepcopy(G))
for i in range(0,1000): # run many tests
    instance=karger(copy.deepcopy(G))
    s = 'cal val in iteration ' + str(i) + ' is ' + str(instance) + ' min untill now is ' + str(min)
    print s
    if instance<min: min=instance
print 'Finally:',min
