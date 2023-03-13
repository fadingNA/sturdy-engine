# Classic ALgorithms

"""
Start with a number n > 1.
Find the number of steps it takes to reach one using
the following process. if n is even // 2
if n is odd multiply it by 3 and add 1
"""
def conjecture(nums):
	if len(nums) > 1:
		for i in range(0, len(nums) - 1):
			if nums[i] % 2 == 0:
				nums[i] //= 2
			if nums[i] % 1 == 0:
				nums[i] *= 3 + 1
				print(nums[i])

	return nums


conjecture([10,20,30,40,50])

# Sorting

"""
Implement two types of sorting algorithms Merge sort and bubble sorts.
"""

def bubble_sort(nums):
	for i in range(0, len(nums) - 1):
		for j in range(0 , len(nums) - 1 - i):
			if nums[j] > nums[j + 1]:
				nums[j] , nums[j + 1] = nums[j + 1], nums[j]
				print(nums[j] , end="->")
				print(nums[j + 1])
	print(nums)

test_bubble = [2,3,71,2,3,4,567,89,534]

bubble_sort(test_bubble)


def merge_sort(nums):
	if len(nums) > 1:
		mid = len(nums) // 2
		l = nums[:mid]
		r = nums[mid:]

		merge_sort(l)
		merge_sort(r)

		i = j = k = 0

		while i < len(l) and j < len(r):
			if l[i] <= r[j]:
				nums[k] = l[i]
				i += 1
			else:
				nums[k] = r[j]
				j += 1
			k += 1

		# checking if any element was left
		while i < len(l):
			nums[k] = l[i]
			i += 1
			k += 1

		while j < len(r):
			nums[k] = r[j]
			j += 1
			k += 1

def printList(arr):
	for i in range(0 , len(arr)):
		print(arr[i] , end = " ")
	print()

printList(test_bubble)

if __name__ == '__main__':
	arr =[12,11,13,5,6,7]
	print("Given arr is", end="\n")
	printList(arr)
	merge_sort(arr)
	print("Sroted array is: ", end="\n")
	printList(arr)
