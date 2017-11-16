# http://rosalind.info/problems/revc/
fin = open('rosalind_revc.txt', 'r')
fout = open('revc_out.txt', 'w+')

dna = list(fin.readline().strip("\n"))
for i in range(0,len(dna)):
	if dna[i]=='A':
		dna[i] = 'T'
	elif dna[i]=='T':
		dna[i] = 'A'
	elif dna[i]=='C':
		dna[i]='G'
	else:
		dna[i]='C'

dna = "".join(dna)
fout.write(dna[::-1])

fin.close()
fout.close()