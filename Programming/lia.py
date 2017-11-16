# http://rosalind.info/problems/lia
fin = open('rosalind_lia.txt', 'r')
fout = open('lia_out.txt', 'w+')
line = fin.readline().split()
k, N = int(line[0]), int(line[1])

def combination(n, m):
	if m>n/2:
		m = n-m
	c, i, j = 1, n, 1
	while i>=n-m+1:
		c *= i
		c /= j
		i -= 1
		j += 1
	return c

prob = 0
for i in range(N, pow(2,k)+1):
	AaBb = pow(0.25, i)
	nAaBb = pow(0.75, pow(2,k) - i)
	prob += AaBb*nAaBb*combination(pow(2,k), i)

fout.write(str(round(prob, 3)))
fin.close()
fout.close()