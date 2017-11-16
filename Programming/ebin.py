# http://rosalind.info/problems/ebin
import numpy as np

fin = open('rosalind_ebin.txt', 'r')
fout = open('ebin_out.txt', 'w+')
n = int(fin.readline())
line = fin.readline().split()
P = [float(x) for x in line]

for p in P:
	b = p*n
	fout.write(str(b)+" ")

fin.close()
fout.close()