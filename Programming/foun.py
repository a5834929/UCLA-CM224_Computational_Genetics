#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.
Problem Title: The Founder Effect and Genetic Drift
Rosalind ID: FOUN
Rosalind #: 095
URL: http://rosalind.info/problems/foun/
'''

from math import log10
from numpy import zeros
from scipy.misc import comb

with open('rosalind_foun.txt') as input_data:
    A = [int(num) for num in input_data.read().strip().split()]
    m, N = A.pop(1), A.pop(0)

M = zeros((m, len(A)))
for index, rec_allele in enumerate(A):
    # Calculate the probability of the number of each rec allele in the first# generation.
    p_rec = rec_allele/(2.0*N)
    p = [comb(2*N, i)*(p_rec**i)*(1.0-p_rec)**(2*N-i) for i in range(0, 2*N+1)]
    M[0][index] = log10(p[0])

    # Use the previous generation to calculate the next.
    for gen in range(1, m-1):
        temp_p = []
        for j in range(0, 2*N+1):
            temp_term = [comb(2*N, j)*((x/(2.0*N))**j)*(1.0 - (x/(2.0*N)))**(2*N-j) for x in range(0, 2*N+1)]
            temp_p.append(sum([temp_term[i]*p[i] for i in range(len(temp_term))]))
        p = temp_p
        M[gen][index] = log10(p[0])

    # Only need the 0th term from the last generation.  We could use the previous loop to determine this.
    # However, the previous loop calculates all additional terms.  This ends up being more code, but less compuatations.
    temp_term = [(1.0 - (x/(2.0*N)))**(2*N) for x in range(0, 2*N+1)]
    M[m-1][index] = log10(sum([temp_term[i]*p[i] for i in range(len(temp_term))]))

# Print and save the output.
# print '\n'.join([' '.join(map(str, M[i])) for i in range(len(M))])
with open('foun_out.txt', 'w+') as output_file:
    for i in range(len(M)):
        for j in range(len(M[i])):
            output_file.write(str(M[i][j])+" ")
        output_file.write('\n')





