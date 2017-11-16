# http://rosalind.info/problems/ba8e
import numpy as np
fin = open('rosalind_ba8e1.txt', 'r')
fout = open('ba8e_out.txt', 'w+')
n = int(fin.readline())
n_cluster = n
M = np.zeros((n,n))
cluster = {}

for i in range(n):
	line = fin.readline().split()
	line = [float(x) for x in line]
	M[i,:] = line
	cluster[i] = [i+1]

def Davg(C1, C2):
	dist = 0
	for c1 in C1:
		for c2 in C2:
			dist += M[c1-1,c2-1]
	return dist/(len(C1)*len(C2))

while len(cluster)>1:
	s1, s2, dist = 0, 0, np.inf
	c1 = [k for k in cluster]
	for i in c1:
		c2 = [k for k in c1 if k>i]
		for j in c2:
			davg = Davg(cluster[i], cluster[j])
			if davg<dist: 
				s1, s2, dist = i, j, davg
				if len(cluster[i])>len(cluster[j]):
					s1, s2 = j, i

	cluster_n = max(c1)+1
	cluster[cluster_n] = cluster[s1]+cluster[s2]
	del cluster[s1]
	del cluster[s2]
	for m in cluster[cluster_n]:
		fout.write(str(m)+" ")
	fout.write("\n")

fin.close()
fout.close()


