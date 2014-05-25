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

def swap(A,m,n):
	"""
	A: list of integers
	m: index of element to be swapped
	n: index of element to be swapped

	returns: nothing, as a side affect swaps the mth and nth element in A
	"""
	temp = A[m]
	A[m] = A[n]
	A[n] = temp

def choosePivot(choice):
	"""
	choice: string describing the chosen pivot
	returns pivot index per the choice of user 
	"""
	pivot_ind_dict = {'first':0, 'last':len(A)}



if __name__ == "__main__":
	testList = [2,1,4,6,9,5]
	swap(testList,0,5)
	print(testList)
