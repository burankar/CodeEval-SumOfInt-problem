'''
Author: Brian Urankar
'''

my_file = open('input-SumOfInt.txt', 'r')
numbers = []

for line in my_file:
	if line.strip():
		n = int(line)
		numbers.append(n)
		
answer = sum(numbers)
my_file.close()

print answer

