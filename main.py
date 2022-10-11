
import sys

num1 = list(map(int, input("Enter the numbers ").split()))
num2 = list(map(int, input("Enter the numbers ").split()))
match = False
loop = 1
if len(num1) > len(num2):
	print ('False')
	sys.exit(0)
if len(num1) <= len(num2) and set(num2) <= set(num1):
		match=True
print(match)