# http://rosalind.info/problems/ini3/
f = open('rosalind_ini3.txt', 'r')
line = f.readline()
numbers = f.readline().split()

a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
d = int(numbers[3])

print(line[a:b+1]+" "+line[c:d+1])

f.close()