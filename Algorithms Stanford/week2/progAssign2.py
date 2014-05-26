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
	left_index: left index of subarray of A
	right_index: right index of subarray of A
	pivot_index: index of the pivot element
	"""
	if left_index < right_index:	
		pivot_value = A[pivot_index]
		# Move pivot to the first element in array
		swap(A,left_index,pivot_index)
		store_index = left_index+1
		for i in range(left_index+1,right_index+1):
			if A[i] < pivot_value:
				swap(A,i,store_index)
				store_index = store_index+1
		# Move pivot to its final place in partioned Array
		swap(A,left_index,store_index-1)
		return store_index-1

def swap(A,m,n):
	"""
	A: list of integers
	m: index of element to be swapped
	n: index of element to be swapped

	returns: nothing, as a side affect swaps the mth and nth element in A
	"""
	if m != n:
		temp = A[m]
		A[m] = A[n]
		A[n] = temp
	else:
		return

def choosePivot(A,choice):
	"""
	A: list of integers
	choice: string describing the chosen pivot
	returns pivot index per the choice of user 
	"""
	pivot_index_dict = {'first':0, 'last':len(A)}
	return pivot_index_dict[choice]


def quickSort(A,left_index,right_index):
	"""
	A: list of integers
	left_index: left index of subarray of A to be sorted
	right_index: right index of subarray of A to be sorted

	returns: nothing, sorts subarray of A identified by left_index and 
	right_index in increasing order
	"""
	# print('at top of quickSort Array to be sorted is',A[left_index:right_index+1])
	if (right_index - left_index == 0): 
		return
	else:
		# Choose pivot index
		pivot_index = left_index
		# Get lists of bigger and smaller items and final position of pivot
		pivot_new_index = partition(A,left_index,right_index,pivot_index)
		# Recursively sort elements smaller than the pivot 
		# (assume pivot_new_index - 1 does not underflow)
		if pivot_new_index - 1 >= left_index:
			quickSort(A, left_index, pivot_new_index-1)
		# Recursively sort elements at least as big as the pivot 
		# (assume pivotNewIndex + 1 does not overflow)
		if pivot_new_index + 1 <= right_index:
			quickSort(A, pivot_new_index + 1, right_index)

def test1():
	test_list = [3,8,2,5,1,4,7,6]
	print('test list is: ',test_list)
	quickSort(test_list,0,len(test_list)-1)
	print('After sorting is: ',test_list)

def test2():
	number_list = loadNumbers()
	quickSort(number_list,0,9999)
	print number_list	


if __name__ == "__main__":
	test1()
	test2()