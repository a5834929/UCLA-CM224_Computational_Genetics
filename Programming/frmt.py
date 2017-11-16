# http://rosalind.info/problems/frmt/
from Bio import Entrez
from Bio import SeqIO

fin = open('rosalind_frmt.txt', 'r')
fout = open('frmt_out.txt', 'w+')
ids = fin.readline().split()

Entrez.email = "your_name@your_mail_server.com"
handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))
min_seq = min(records, key=lambda rec: len(rec.seq))
fout.write(min_seq.format("fasta"))

fin.close()
fout.close()
