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
	def push_front(self, data):
        new_node = self.Node(data, self.front)
        if self.front:
            self.front.prev_node = new_node
        else:
            self.back = new_node
        self.front = new_node

    def recur_print_forward(self, node_n, output=""):
        if node_n is None:
            return
        elif node_n.next_node is None:
            print(output + f"{node_n.data}")
        else:
            self.recur_print_forward(node_n.next_node, output + f"{node_n.data} -> ")

    def reverse_between(self, left, right):
        dummy = List(self.front)

        leftPrev, current = dummy, self.front
        for i in range(left - 1):
            leftPrev, current = current, current.next_node
        # Now cure="left", leftPrev="node before left"
        # 2) reverse from left to right
        prev = None
        for i in range((right - left) + 1):
            tmpNext = current.next_node
            current.next_node = prev
            prev, current = current, tmpNext

        leftPrev.next_node.next_node = current
        leftPrev.next_node = prev
        return dummy.next_node

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

