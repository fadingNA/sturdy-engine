"""
Implemented Doubly Linklist, with 
important function such as search count and make_set

"""
class List:
	class Node:
		def __init__(self, d, n = None, p = None):
			self.d = d
			self.n = n
			self.p = p

	def __init__(self):
		self.head = None
		self.tail = None

	def printt(self):
		cur = self.head
		while cur:
			print(cur.d)
			cur = cur.n

	def make_set(self,data):
		nn = self.Node(data,self.head)
		if self.head:
			self.head.p = nn
		else:
			self.tail = nn
		self.head = nn

	def count_node(self):
		cur = self.head
		count = 0
		while cur:
			count += 1
			cur = cur.n
		print(count)
		return count

	def search(self,data):
		cur = self.head
		while cur:
			if cur.d == data:
				return True
			else:
				cur = cur.n
		return False

	def pop_front(self):
		if self.head:
			remove = self.head
			self.head = self.head.n
			if self.head is None:
				self.tail = None
			else:
				self.head.p = None
			del remove


non = List()

non.make_set('423')
non.pop_front()
non.make_set('532')
non.make_set('532')
non.make_set('532')
non.make_set('532')
non.pop_front()

print(non.search('50'))

non.count_node()


non.printt()
print("<before pop_front>")
non.pop_front()
print("after pop")
non.printt()

