# Summation of the First n integers (Timing)
import time

def sumOfN(n):
	start = time.time()

	theSum = 0
	for i in range(1, n+1):
		theSum = theSum + i

	end = time.time()

	return theSum, end-start

x = sumOfN(30)
print(x)
