# http://rosalind.info/problems/sexl
fin = open('rosalind_sexl.txt', 'r')
fout = open('sexl_out.txt', 'w+')
male = fin.readline().split()
male_float = [float(m) for m in male]
female = [(1-m)*m*2 for m in male_float]

for i in female:
	fout.write(str(i)+" ")

fin.close()
fout.close()