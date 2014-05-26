import math
PATH_TO_FILE = 'QuickSort.txt'
# PATH_TO_FILE = '1000.txt'
comparisonCount = 0 # Important : Global Variable

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

def choosePivotIndex(A,left_index,right_index,choice):
	"""
	A: list of integers
	choice: string describing the chosen pivot
	returns pivot index per the choice of user 
	"""
	if choice == 'median':	
		a = A[left_index]
		b = A[right_index]
		if (right_index - left_index) % 2 != 0:
			c_index = left_index + (right_index - left_index -1)/2
			c = A[c_index]
		else:
			c_index = left_index + (right_index - left_index)/2
			c = A[c_index]

		if (a-b)*(a-c) <= 0:
			pivot_index = left_index
		elif (b-a)*(b-c) <= 0:
			pivot_index = right_index
		elif (c-b)*(c-a) <= 0:
			pivot_index = c_index
	elif choice == 'first':
		pivot_index = left_index
	elif choice == 'last':
		pivot_index = right_index

	return pivot_index


def quickSort(A,left_index,right_index):
	"""
	A: list of integers, no repitition of numbers assumed
	left_index: left index of subarray of A to be sorted
	right_index: right index of subarray of A to be sorted

	returns: nothing, sorts subarray of A identified by left_index and 
	right_index in increasing order
	"""
	global comparisonCount # GLOBAL
	comparisonCount = comparisonCount + right_index-left_index
	if (right_index - left_index == 0): 
		return
	else:
		# Choose pivot index
		pivot_index = choosePivotIndex(A,left_index,right_index,'first')		
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

def countComparisons():
	print comparisonCount

def test1():
	test_list = [3,8,2,5,1,4,7,6]
	print('test list is: ',test_list)
	quickSort(test_list,0,len(test_list)-1)
	print('After sorting is: ',test_list)

def test2():
	number_list = loadNumbers()
	quickSort(number_list,0,9999)
	print number_list

# Answers are:
# size    first     last      median
# 10       25        29        21
# 100     615       587        518
# 1000   10297     10184       8921


if __name__ == "__main__":
	#test1()
	test2()
	countComparisons()