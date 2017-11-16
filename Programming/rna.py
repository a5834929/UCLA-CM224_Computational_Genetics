# http://rosalind.info/problems/rna/
fin = open('rosalind_rna.txt', 'r')
fout = open('rna_out.txt', 'w+')

dna = fin.readline()
rna = dna.replace('T', 'U')

fout.write(rna)

fin.close()
fout.close()
