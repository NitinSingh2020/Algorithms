import math
PATH_TO_FILE = 'ProgAssign1.txt'

def loadNumbers():
	lines = open(PATH_TO_FILE, 'r', 0).read().splitlines()
	numberList = []
	for a in lines:
		numberList.append(int(a))
	return numberList


testList = [2,5,6,1,3,9,7]

def mergeSort(inputList):
	"""
	inputList: list of integers to be sorted in increasing order
	returns a new list sorted in increasing order
	meregeSort is O[nlog(n)]
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



def merge(left, right):
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

print(mergeSort(testList))
print(mergeSort(loadNumbers()))