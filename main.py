
import sys

num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

match = False
loop = 1

if len(num1) > len(num2):
	print ('False')
	sys.exit(0)
for i in range (len(num1)):
        if num2[0] == num1[i]:
            match = True
            while i+loop < len(num2):
                if num2[loop] != num1[i+loop]:
                    match = False
                loop += 1
# ******************************
# Make your Code
# ******************************

# print ('True') or ('False')
