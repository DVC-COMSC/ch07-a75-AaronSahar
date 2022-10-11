
import sys

num1 = list(map(int, input("Enter the numbers ").split()))
num2 = list(map(int, input("Enter the numbers ").split()))
if len(num1) > len(num2):
	print ('False')
	sys.exit(0)
print(set(num1).issubset(set(num2)))