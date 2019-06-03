#!/usr/bin/env python3

from collections import defaultdict
from sys import argv, exit, stdout, stdin, stderr, setrecursionlimit

setrecursionlimit(50000)
global oAdjacency, sAdjacency, Nodes, d_sc, l_w, sNum, inSack, inD, outD, comp
size = 20015

def readIn(ProvenImplications):
    try:
        for _ in range(0, int(ProvenImplications)):
            uv = stdin.readline().split()
            u, v = int(uv[0]), int(uv[1])
            #print("(" + str(u) + ", " + str(v) + ")")
            oAdjacency[u].append(v)
    except (ValueError, IndexError):
        pass
    return oAdjacency

def createDictionary(size):
    newDict= defaultdict(list)
    for vertex in range(size):
        newDict[vertex] = [ ]
    return newDict

def findSCC(current, oAdjacency):
    global temp, Nodes, sccID, sNum
    d_sc[current] = temp
    l_w[current] = temp
    temp += 1
    comp.append(current)
    inStack[current] = True
    for i in range(0, len(oAdjacency[(current)])):
        next_ = oAdjacency[(current)][i]

        if (d_sc[next_] == -1):
            findSCC(next_, oAdjacency)
            l_w[current] = min(l_w[current], l_w[next_])   
           
        elif inStack[next_] == True: 
            l_w[current] = min(l_w[current], d_sc[next_])
    
    if l_w[current] == d_sc[current]:
        now = -1
        while comp[(len(comp)-1):] != [current]:
            now = comp.pop()
            Nodes[sccID].append(now)
            inStack[now] = False
            sNum[now] = sccID
        now = comp.pop()
        Nodes[sccID].append(now)
        inStack[now] = False
        sNum[now] = sccID
        sccID += 1
        

comp = [ ]
testcases = int(stdin.readline())

#def main():
    
while testcases != 0:
    testcases -= 1
    d_sc, l_w, sNum = [-1]*size, [-1]*size, [-1]*size
    inStack = [False]*size
    inD, outD = [0]*size, [0]*size
    sccID, temp, zIn, zOut = 0, 0, 0, 0
    Nodes = createDictionary(size)
    oAdjacency = createDictionary(size)
    sAdjacency = createDictionary(size)
    try:
        givenStatements, ProvenImplications = stdin.readline().split() 
    except ValueError:
        pass
    oAdjacency = readIn(ProvenImplications)

    for i in range(1, (int(givenStatements)+1)):
        if d_sc[i] == -1:
            findSCC(i, oAdjacency)
    #print("sccID: " + str(sccID))
    #print("Nodes: " + str(Nodes))
    
    for k in range(sccID):
        for i in Nodes[k]:
            for j in oAdjacency[i]:
                if sNum[i] != sNum[j]:
                    sAdjacency[sNum[i]].append(sNum[j])
                    inD[sNum[j]] += 1
                    outD[sNum[i]] += 1
    for k in range(sccID):
        if inD[k] == 0:
            zIn += 1
        if outD[k] == 0:
            zOut += 1
    if sccID == 1:
        zIn, zOut = 0, 0
    print(str((max(zIn, zOut))))
