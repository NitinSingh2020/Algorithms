import math
PATH_TO_FILE = 'ProgAssign1.txt'

def loadNumbers():
	"""
	reads txt file
	returns: array/list of int in file
	"""
	lines = open(PATH_TO_FILE, 'r', 0).read().splitlines()
	numberList = []
	for a in lines:
		numberList.append(int(a))
	return numberList


def merge(left, right):
	"""
	left: list of int
	right: list of int
	returns: sorted merge list 
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
			result.append(left[0])
			left = left[1:]
		elif len(right) > 0:
			result.append(right[0])
			right = right[1:]
	return result


def mergeSort(inputList):
	"""
	inputList: list of integers to be sorted in increasing order
	returns: a new list sorted in increasing order
	Time Complexity: O[nlog(n)]
	"""
	if len(inputList) <= 1:
		return inputList

	leftList = []
	rightList = []
	middleNum = int(math.ceil(len(inputList) / 2.0))

	for num in range(middleNum):
		leftList.append(inputList[num])
	for num in range(middleNum, len(inputList)):
		rightList.append(inputList[num])

	leftList = mergeSort(leftList)
	rightList = mergeSort(rightList)
	result = merge(leftList, rightList)
	return result


def CountInv(inputList, n):
	"""
	inputList: list of integers
	n: length/size of inputList
	returns: number of invesions in inputList

	Brute Force Method with Time Complexity: O(n^2)
	"""
	count = 0
	for i in range(n-1):
		if (i%1000 == 0):
			print("Done with step: ", i)
		for j in range(i+1, n):
			if (inputList[i] > inputList[j]):
				count += 1
	return count


testList1 = [2,5,6,1,3,9,7]
testList2 = [1,3,5,2,4,6]




if __name__ == "__main__":
	print(mergeSort(testList1))
	# print(mergeSort(loadNumbers()))
	# print(SortAndMerge(testList1))
	# print(SortAndMerge(testList2))
	print(CountInv(testList1, 7))
	print(CountInv(testList2, 6))
	print(CountInv(loadNumbers(), 100000))