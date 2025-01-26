graph = {'A': set(['B', 'C']),
         'B': set(['A', 'C', 'D', 'E']),
         'C': set(['A', 'B' ,'F', 'G']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E']),
         'G': set(['C', 'H']),
         'H': set(['G'])} 

def ciclo(graph, start):
	visited, queue = set(), [start]
	while queue:
		vertex = queue.pop(0)
		if vertex not in visited:
			visited.add(vertex)
			queue.extend(graph[vertex] - visited)
			print("visited", visited)
			print("queue", queue)
		else:
			print ("cycle", vertex) 
			return visited
	return visited

def bfs(graph, start):
	visited, queue = set(), [start]
	while queue:
		vertex = queue.pop(0)
		if vertex not in visited:
			visited.add(vertex)
			queue.extend(graph[vertex] - visited)
			print("visited", visited)
			print("queue", queue)
	return visited


ciclo(graph, 'A')
print("--------")
bfs(graph, 'A')
