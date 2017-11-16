# http://rosalind.info/problems/ini5/
fin = open('rosalind_ini5.txt', 'r')
fout = open('ini5_out.txt', 'w+')

i = 0
for line in fin.readlines():
	if i%2 != 0:
		fout.write(line)
	i += 1

fin.close()
fout.close()