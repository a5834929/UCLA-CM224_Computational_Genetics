# http://rosalind.info/problems/ini/
fin = open('rosalind_ini.txt', 'r')
fout = open('ini_out.txt', 'w+')

words = fin.readline()
dict = {}
for word in words:
	if word in dict:
		dict[word] = dict[word]+1
	else:
		dict[word] = 1

fout.write(str(dict['A'])+" "+str(dict['C'])+" "+str(dict['G'])+" "+str(dict['T']))

fin.close()
fout.close()
