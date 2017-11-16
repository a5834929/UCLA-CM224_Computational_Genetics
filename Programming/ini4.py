# http://rosalind.info/problems/ini4/
f = open('rosalind_ini4.txt', 'r')
line = f.readline()
numbers = line.split()
a = int(numbers[0])
b = int(numbers[1])
s = 0
for i in range(a,b+1):
	if i%2 != 0:
		s += i
print(s)

f.close()