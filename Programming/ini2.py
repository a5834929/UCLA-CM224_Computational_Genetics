# http://rosalind.info/problems/ini2/
f = open('rosalind_ini2.txt', 'r')
line = f.read()
numbers = line.split()
a = int(numbers[0])
b = int(numbers[1])
print(a*a+b*b)

f.close()