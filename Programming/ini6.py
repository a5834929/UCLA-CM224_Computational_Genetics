# http://rosalind.info/problems/ini6/
fin = open('rosalind_ini6.txt', 'r')
fout = open('ini6_out.txt', 'w+')

words = fin.readline().split()
dict = {}
for word in words:
	if word in dict:
		dict[word] = dict[word]+1
	else:
		dict[word] = 1

for key, value in dict.items():
	fout.write(key+" "+str(value)+"\n")

fin.close()
fout.close()