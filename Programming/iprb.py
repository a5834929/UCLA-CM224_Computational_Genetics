# http://rosalind.info/problems/iprb/
fin = open('rosalind_iprb.txt', 'r')
fout = open('iprb_out.txt', 'w+')
population = fin.readline().split()

prob = []
population = [int(n) for n in population]
s = sum(population)

for i in range(len(population)-1):
	fst = population[i]
	for j in range(i,len(population)):
		scd = population[j]
		if i==j:
			prob.append((fst/s)*((scd-1)/(s-1)))
		else:
			prob.append(2*(fst/s)*(scd/(s-1)))

prob[3] = prob[3]*(3/4)
prob[4] = prob[4]*(1/2)
fout.write(str(sum(prob)))

fin.close()
fout.close()
