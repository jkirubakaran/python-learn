import time


def fib(num):
	
	if num < 3:
		return 1

	a = b = 1

	for i in range(2,num):
		a, b = b, a+b
	return b

def fibRecursive(num):
	if num < 3:
		return 1

	return fibRecursive(num - 1) + fibRecursive(num - 2)


#print(fib(40))
print(fibRecursive(40))
