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

def quickSort():
	"""
	"""

	
if __name__ == "__main__":
	print(loadNumbers())