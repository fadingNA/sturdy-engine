from PIL import Image, ImageDraw
images = []

a = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0 ,0, 0, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0 ,0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0 ,0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
zoom = 20
borders = 6
start = 1,1
end = 5,19

def make_step(step):
	for i in range(len(m)):
		for j in range(len(m[i])):
			if m[i][j] == k:
				if i > 0 and m[i-1][j] == 0 and a[i-1][j] == 0:
					m[i-1][j] = k + 1
				if j > 0 and m[i][j-1] == 0 and a[i][j-1] == 0:
					m[i][j-1] = k + 1
				if i < len(m)-1 and m[i+1][j] == 0 and a[i+1][j] == 0:
					m[i+1][j] = k + 1
				if i < len(m[i]) -1 and m[i][j-1] == 0 and a[i][j-1] == 0:
					m[i][j+1] = k + 1

def print_m(m):
	for i in range(len(m)):
		for j in range(len(m[i])):
			print( str(m[i][j]).ljust(2),end = ' ')
		print()

def draw_matrix(a,m,the_path = []):
	im = Image.new('RGB', (zoom * len(a[0]), zoom * len(a)), (255, 255,255))
	draw = ImageDraw.Draw(im)
	for i in range(len(a)):
		for j in range(len(a[i])):
			color = (255, 255, 255)
			r = 0
			if a[i][j] == 1:
				color = (0,0,0)
			if i == start[0] and j == start[1]:
				color = (0, 255, 0)
				r = borders
			if i == end[0] and j == end[1]:
				color = (0,255,0)
				r = borders
			draw.rectangle((j*zoom+r, i*zoom+r, j*zoom+zoom-r-1, i*zoom+zoom-r-1), fill=color)




"""
For travesing a graph we can taek two approaches.
We can go level by level or we can go to the depth as far
as possible

DFS takes teh cond approach. It starts with a root node and 
explores the graphs in-depth as far as possible.
After reaching a dead-end the algorithm starts
back-tracking and eventually completes the search.
"""

def dfs(graph, source, visited, dfs_traversal):
	if source not in visited:
		dfs_traversal.append(source)
		visited.add(source)

		for node in graph[source]:
			dfs(graph, node, visited, dfs_traversal)
	return dfs_traversal
"""
BFS AND DFS are two of the most basic algorithms to learn when
studying graphs, In this article, we learned how the DFS algorithm
recursively traverse a graph. We also saw the Python Implementation
of the algorithm
"""

def main():
	visited = set()
	dfs_traversal = list()

	graph = {
	'A' : ['B', 'C'],
	'B' : ['D', 'E'],
	'C' : ['F', 'G'],
	'D' : [],
	'E' : [],
	'F' : [],
	'G' : []
	}

	print(f"DFS: {dfs(graph, 'A', visited, dfs_

def recur_parlin(ss,left,right)
    if left >= right:
        return True
    else:
        if ss[left] != ss[right]:
            return False
        else:
            return recur_parlin(ss,left + 1, right -1)
            
def isPalindrome(s):
    return recur_parlin(s,0,len(s)-1)
    
ggts = 'non'
print(isPalindrome(ggts))

if __name__=="__main__":
	main()