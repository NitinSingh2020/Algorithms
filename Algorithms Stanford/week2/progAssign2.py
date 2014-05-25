import math
PATH_TO_FILE = 'QuickSort.txt'

def loadNumbers():
	"""
	reads txt file
	returns: array/list of integers in file
	"""
	lines = open(PATH_TO_FILE, 'r', 0).read().splitlines()
	number_list = []
	for a in lines:
		number_list.append(int(a))
	return number_list

# def quickSort():
# 	"""
# 	"""

def partition(A,l,r):
	"""
	A: list of integers
	l: left index of subarray of A
	r: right index of subarray of A
	"""
	p = A[l]
	i = l+1
	for j in range(l+1,r+1):
		if A[j] < p:
			swap(A[j], A[i])
			i = i+1
	swap(A[l], A[i-1])

if __name__ == "__main__":
	print(loadNumbers())