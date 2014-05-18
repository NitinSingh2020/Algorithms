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
	returns: a new sorted list by merging left and right
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

	middle_num = int(math.ceil(len(input_list) / 2.0))

	# Split list into two halves
	left_list = input_list[0:middle_num]
	right_list = input_list[middle_num:]

	# Recursive call
	left_list = mergeSort(left_list)
	right_list = mergeSort(right_list)

	# Merge the two sorted lists
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


def sortAndCount(input_list, list_size):
	"""
	input_list: list of integers
	list_size: length/size of inputList
	returns: the number of inversions in inputList and sorts input_list

	! imp : does not return new list, sorts the input list
	Time Complexity: O[n*log(n)]
	"""
	temp_list = [0]*list_size
	return _sortAndCount(input_list, temp_list, 0, list_size - 1)


def _sortAndCount(input_list, temp_list, left, right):
    """
    helper recursive function to sort the input array and return the number of
    inversions

    input_list: list of integers
    temp_list: temp list
    left: integer, identifies starting index of part of the list to be sorted
    right: integer, identifies ending index of part of the list to be sorted
    returns: the number of inversions in inputList and sorts input_list

    ! imp : does not return new list, sorts the input list
    """
    inv_count = 0
    if (right > left):
        # Divide the array into two parts and call _mergeSortAndCountInv()
        # for each of the parts
        mid = (right + left)/2
        # Inversion count will be sum of inversions in left-part, right-part
        #  and number of inversions in merging

        inv_count  = _sortAndCount(input_list, temp_list, left, mid)
        inv_count += _sortAndCount(input_list, temp_list, mid+1, right)

        # Merge the two parts
        inv_count += countSplitInv(input_list, temp_list, left, mid+1, right)
    return inv_count


def countSplitInv(input_list, temp_list, left, mid, right):
    inv_count = 0;

    i = left; # i is index for left subarray*/
    j = mid;  # j is index for right subarray*/
    k = left; # k is index for resultant merged subarray*/

    while ((i <= mid - 1) and (j <= right)):
        if (input_list[i] <= input_list[j]):
        	temp_list[k] = input_list[i]
        	k+=1
        	i+=1
        else:
        	temp_list[k] = input_list[j]
        	k+=1
        	j+=1
        	inv_count = inv_count + (mid - i)

    # Copy the remaining elements of left subarray
    # (if there are any) to temp*/
    while (i <= mid - 1):
    	temp_list[k] = input_list[i]
    	k+=1
    	i+=1

    # Copy the remaining elements of right subarray
    # (if there are any) to temp*/
    while (j <= right):
    	temp_list[k] = input_list[j]
    	k+=1
    	j+=1

    # Copy back the merged elements to original array*/
    for i in range(left, right+1):
    	input_list[i] = temp_list[i];

    return inv_count


testList1 = [2,5,6,1,3,9,7]
testList2 = [1,3,5,2,4,6]


if __name__ == "__main__":
	print(mergeSort(testList1)) # Runs fine
	print(mergeSort(testList2)) # Runs fine
	# print(mergeSort(loadNumbers()))

	print("Brute force on testList1", CountInv(testList1, 7))
	print("Brute force on testList2", CountInv(testList2, 6))
	# print('Brute force on text file', CountInv(loadNumbers(), 100000))

	print("Fast way on testList1", sortAndCount(testList1, 7)) # Infinite loop
	print("Fast way on testList2", sortAndCount(testList2, 6))
	print('Fast way on text file', sortAndCount((loadNumbers()), 100000))