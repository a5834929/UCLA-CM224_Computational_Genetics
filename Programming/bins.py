# http://rosalind.info/problems/bins
fin = open('rosalind_bins.txt', 'r')
fout = open('bins_out.txt', 'w+')
n = int(fin.readline())
m = int(fin.readline())
line = fin.readline().split()
arr = [int(x) for x in line]
line = fin.readline().split()
query = [int(x) for x in line]
idx = [-1]*m

for i in range(len(query)):
	left = 0
	right = n
	if arr[left] == query[i]:
		idx[i] = 1
	else:
		while left+1<right:
			mid = int((left+right)/2)
			if arr[mid]<query[i]:
				left = mid
			elif arr[mid]>query[i]:
				right = mid
			else:
				idx[i] = mid+1 
				break

for i in idx:
	fout.write(str(i)+" ")

fin.close()
fout.close()