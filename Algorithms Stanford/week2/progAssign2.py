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


def partition(A,left_index,right_index,pivot_index):
	"""
	A: list of integers
	l: left index of subarray of A
	r: right index of subarray of A
	"""
	pivot_value = A[pivot_index]
	p = A[left_index]
	store_index = left_index+1
	for i in range(left_index+1,right_index+1):
		if A[i] < p:
			swap(i,store_index)
			store_index = store_index+1
	swap(left_index,store_index-1) # Move pivot to its final place in partioned Array
	return store_index


if __name__ == "__main__":
	testList = [2,1,4,6,9,5]
	swap(testList,0,5)
	print(testList)