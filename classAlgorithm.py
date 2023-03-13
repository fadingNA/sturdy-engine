import math

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

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def compare_x(a,b):
	p1 = a
	p2 = b
	return (p1.x - p2.x)

def compare_y(a,b):
	p1 = a 
	p2 = b 
	return (p1.y - p2.y)

def dist(p1, p2):
	return math.sqrt(((p1.x - p2.x) * (p1.x - p2.x)) + ((p1.y - p2.y) * (p1.y - p2.y)))

def bruteForce(P, n):
	min_dist = float("inf")
	for i in range(n):
		for j in range(i + 1, n):
			if dist(P[i], P[j])< min_dist:
				min_dist = dist(P[i],P[j])
	return min_dist

def min(x,y):
	return x if x < y else y

def stripClosest(strip, size, d):
	min_dist = d
	strip = sorted(strip, key=lambda point: point.y)

	for i in range(size):
		for j in range(i + 1, size):
			if strip[j].y - strip[i].y >= min_dist:
				break
			if dist(strip[i], strip[j]) < min_dist:
				min_dist = dist(strip[i], strip[j])
	return min_dist


def clossetUtill(P,n):
	if n <= 3:
		return bruteForce(P,n)

	mid = n // 2
	midPoint = P[mid]
	dl = clossetUtill(P,mid)
	dr = clossetUtill(P[mid:], n - mid)
	d = min(dl,dr)
	strip = []
	for i in range(n):
		if abs(P[i].x - midPoint.x) < d:
			strip.append(P[i])
	return min(d, stripClosest(strip, len(strip), d))

def closest(P, n):
    P = sorted(P, key=lambda point: point.x)
    return closestUtil(P, n)


# Prime smaller than or equal to
# n using Sieve of Eratosthese

def SieveOfEra(n):
	"""
	1. Create a boolen array
	2. primt[0..n] and intitalize
	3. all entries it as true.
	4. A value in prime[i] will
	   finally be false if i is not a prime, else True
	"""
	prime = [True for i in range(n + 1)]
	p = 2
	while( p * p <= n):
		# if prime[p] is not
		# changed, then it is a prime
		if prime[p]:
			for i in range( p * p , n + 1, p):
				prime[i] = False
		p += 1

	# print all prime numbers
	for p in range(2, n + 1):
		if prime[p]:
			print(p)
printList(test_bubble)

if __name__ == '__main__':
	arr =[12,11,13,5,6,7]
	print("Given arr is", end="\n")
	printList(arr)
	merge_sort(arr)
	print("Sroted array is: ", end="\n")
	printList(arr)
	n = 20
	print("Following are the prime numbers smaller")
	print("then or equal to <" , n , ">")
	SieveOfEra(n)
	P = [Point(x=2, y=3), Point(x=12, y=30),
         Point(x=40, y=50), Point(x=5, y=1), Point(x=12, y=10), Point(x=3, y=4)]
   # n = len(P)
    #print("The smallest distance is", closest(P, n))
