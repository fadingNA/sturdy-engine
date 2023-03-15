# Graphs from links - Create a Program that will create a graph or network from a series of links.
class Graph:
	def __init__(self):
		self.graph = dict()

	def add_edge(self, node1, node2, cost):
		if node1 not in self.graph:
			self.graph[node1] = []
		if node2 not in self.graph:
			self.graph[node2] = []

		self.graph[node1].append((node2, int(cost)))

		#in case of undirected graph
		# self.graph[node2.append]((node1, int(cost)))

	def kruskalsMST(self,G=(V,E)):
		T= []
		

	def print_graph(self):
		for source, desination in self.graph.items():
			print(f"{source} ---> {desination}")



graph = [[0,1,5,9,0],[1,2,5,0,0],[2,1,0,0,0],[1, 0, 0, 0, 13],
        [0, 0, 0, 0, 0]]

g_dictionary = {
	'A' : ['B', 'C'],
	'B' : ['D', 'E'],
	'C' : ['D'],
	'D' : ['E', 'A'],
	'E' : []
}


# if graph[i[j]] == 0:
# then there is no path between node i and j.
#but if graph[i][j] gives us a value other than 0, we can say there is a path between node i and j

"""
Example if graph[0][1], the output is 1. That means there is a path between node 0 and node 1
and the path cost is 5. This represents edge(A,B) in our graph.
"""

for key, val in g_dictionary.items():
	print(f"{key} --> {val}")


"""
The dictionary g_dictionary represents the graph decribed above.
Now let's see how to construct this structure of the graph from user input
We can create a function addEdge(). This functionm will take two parameter
the two nodes having a path between them. So, addEdge('A','B') will mean
node A and node B are neighbours.

"""

g_with_function = dict()

def addEdge(node1, node2):
	# create an empty list for a key node
	if node1 not in g_with_function:
		g_with_function[node1] = []
	if node2 not in g_with_function:
		g_with_function[node2] = []

	# append the neighbor node to its corresponding key node
	g_with_function[node1].append(node2)

"""
But there is a problem. We have to call the addEdge() Function every time we
went to creat an edge of the graph. It would be nice if we could input
the whole graph and the adjacency list be created at once.
"""

def main():
	g = Graph()

	with open("input.txt") as f:
		lines = f.readlines()

	nodes, edges = lines[0].split()

	# first line is number of nodes and edges,
	# pair of nodes starts from second line
	for i in range(1, len(lines)):
		node1, node2, cost = lines[i].split()
		g.add_edge(node1, node2, int(cost))
	g.print_graph()

if __name__=="__main__":
	main()