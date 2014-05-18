import math
PATH_TO_FILE = 'ProgAssign1.txt'

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


def merge(left, right):
	"""
	left: sorted list of integers 
	right: sorted list of integers
	returns: sorted merge list of left and right
	"""
	result = []
	while len(left) > 0 or len(right) > 0:
		if len(left) > 0 and len(right) > 0:
			if left[0] <= right[0]:
				result.append(left[0])
				left = left[1:]
			else:
				result.append(right[0])
				right = right[1:]
		elif len(left) > 0:
			result = result + left
			left = []
		elif len(right) > 0:
			result = result + right
			right = []
	return result


def mergeSort(input_list):
	"""
	input_list: list of integers to be sorted in increasing order
	returns: a new list sorted in increasing order
	Time Complexity: O[nlog(n)]
	"""
	if len(input_list) <= 1:
		return input_list

	left_list = []
	right_list = []
	middle_num = int(math.ceil(len(input_list) / 2.0))

	for num in range(middle_num):
		left_list.append(input_list[num])
	for num in range(middle_num, len(input_list)):
		right_list.append(input_list[num])

	left_list = mergeSort(left_list)
	right_list = mergeSort(right_list)
	result = merge(left_list, right_list)
	return result


def CountInv(input_list, n):
	"""
	input_list: list of integers
	n: length/size of inputList
	returns: number of invesions in inputList

	Brute Force Method with Time Complexity: O(n^2)
	"""
	count = 0
	for i in range(n-1):
		for j in range(i+1, n):
			if (input_list[i] > input_list[j]):
				count += 1
	return count





testList1 = [2,5,6,1,3,9,7]
testList2 = [1,3,5,2,4,6]




if __name__ == "__main__":
	print(mergeSort(testList1))
	print(mergeSort(testList2))
	print(mergeSort(loadNumbers()))
	# print(SortAndMerge(testList1))
	# print(SortAndMerge(testList2))
	# print("Brute force on testList1", CountInv(testList1, 7))
	# print("Brute force on testList2", CountInv(testList2, 6))
	# print(CountInv(loadNumbers(), 100000))
	# print(countSplitInv([2,5,6,1], [3,9,7]))
	# print(countSplitInv([1,3,5], [2,4,6]))
	# print("Fast way on testList1", Count(testList1, 7))
	# print("Fast way on testList2", Count(testList2, 6))
