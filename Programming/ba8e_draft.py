import scipy.cluster.hierarchy as hcluster
import numpy as np
from numpy import zeros
from numpy import shape
from numpy import expand_dims
from itertools import product

# distance between clusters
def distance(c1, c2, dMat):
    sigmaDist = 0
    for a in c1:
        for b in c2:
            temp_dist =  dMat[a][b]
            sigmaDist += temp_dist
    return sigmaDist/ len(c1) / len(c2)


numNodes = open('rosalind_ba8e.txt', 'r')
numNodes = int(numNodes.readline())

distanceMat = np.loadtxt('rosalind_ba8e.txt', skiprows = 1)
distanceMatOriginal = distanceMat
distanceMatUpper = np.triu(distanceMat)

# ====================
# nodes = {};
nodes = [];
for i in range(0, numNodes):
    nodes.append({i})
#     nodes[i] = [i]
    
while len(nodes)>1:
    set1 = set()
    set2 = set()
#     minumum distance set
    minD = np.min(distanceMatUpper[np.nonzero(distanceMatUpper)])
    # print(minD)
    minDnodes = np.where(distanceMatUpper == minD)
    set1 = set1.union(nodes[int(minDnodes[0])], nodes[int(minDnodes[1])])
    # print (set1)
    
    nodes.append(set1)
    
    print (nodes)
    temp_mat = np.zeros((distanceMatUpper.shape[0]+1,distanceMatUpper.shape[0]+1))
    temp_mat[:-1,:-1] = distanceMatUpper
    distanceMatUpper = temp_mat
    for j in range(0 , len(nodes)-1):
        # print (j)
        if j not in nodes[distanceMatUpper.shape[0]-1]:
            set2 = set2.union(nodes[j])
            distanceMatUpper[j][distanceMatUpper.shape[0]-1] =  distance(set1, set2, distanceMatOriginal)

#     distanceMatUpper[int(minDnodes[0])][int(minDnodes[1])] = 0
    distanceMatUpper[:,int(minDnodes[0])] = 0
    distanceMatUpper[:,int(minDnodes[1])] = 0
#     distanceMatUpper[distanceMatUpper.shape[0]-1][distanceMatUpper.shape[0]-1] = 0
#     print (distanceMatUpper)
    
    tem_mat = distanceMatUpper
    for m in range(distanceMatUpper.shape[0]):
        for n in range(m, distanceMatUpper.shape[0]):
            tem_mat[n][m] = tem_mat[m][n]
            distanceMat  = tem_mat
    
    distanceMatUpper = np.triu(distanceMat)

# print (nodes)



