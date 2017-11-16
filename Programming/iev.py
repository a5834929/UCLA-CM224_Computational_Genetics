# http://rosalind.info/problems/iev/
fin = open('rosalind_iev.txt', 'r')
fout = open('iev_out.txt', 'w+')
couple = fin.readline().split()
couple = [int(x) for x in couple]
prob = [1, 1, 1, 3/4, 1/2, 0]
offspring = [c*p*2 for c,p in zip(couple, prob)]

fout.write(str(sum(offspring)))
fin.close()
fout.close()
