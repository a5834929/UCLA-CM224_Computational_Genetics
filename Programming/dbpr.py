# http://rosalind.info/problems/dbpr/
from Bio import ExPASy
from Bio import SwissProt

fin = open('rosalind_dbpr.txt', 'r')
fout = open('dbpr_out.txt', 'w+')
protein = fin.readline()

handle = ExPASy.get_sprot_raw(protein)
record = SwissProt.read(handle)

for cr in record.cross_references:
	if cr[0]=='GO' and cr[2][0]=='P':
		fout.write(cr[2].lstrip('P:')+'\n')

fin.close()
fout.close()
