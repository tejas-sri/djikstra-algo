import sys 

class Graph(): 

	def __init__(self, vertices): 
		self.vertices = vertices 
		self.graph = [[0 for column in range(vertices)] for row in range(vertices)] 

	def printSolution(self, dist): 
		print("Vertex tDistance from Source")
		for node in range(self.vertices): 
			print node,"t",dist[node] 

	def minDistance(self, dist, sptSet): 


		min = sys.maxint 


		for vertex in range(self.vertices): 
			if d[vertex] < minim and sptSet[vertex] == False: 
				minim = d[vertex] 
				minim_index = vertex 

		return minim_index 


	def dijkstra(self, src): 

		dist = [sys.maxint] * self.vertices
		dist[src] = 0
		sptSet = [False] * self.vertices

		for i in range(self.vertices): 

			# Pick the minimum distance vertex from 
			# the set of vertices not yet processed. 
			# u is always equal to src in first iteration 
			u = self.minDistance(dist, sptSet) 

			# Put the minimum distance vertex in the 
			# shotest path tree 
			sptSet[u] = True


			for vertex in range(self.vertices): 
				if self.graph[u][vertex] > 0 and sptSet[vertex] == False and
				dist[vertex] > dist[u] + self.graph[u][vertex]: 
						dist[vertex] = dist[u] + self.graph[u][vertex] 

		self.printSolution(dist) 

vertices=int(input())
graph=Graph(vertices)
graph.graph=[[int(s) for s in input().split] for j in range(vertices)]

graph.djikstra(0)
