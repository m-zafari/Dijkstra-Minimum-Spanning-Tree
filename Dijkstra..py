import matplotlib.pyplot as plt
import networkx as nx

'''
** Mohammad Zafari **
///dijkstra algorithm
'''

class Graph():
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]
		self.TreeEdge = []

	def printSolution(self, d):
		print("Vertex \t Distance from Source")
		for node in range(self.V):
			print(node, "\t\t", d[node])
	def minDistance(self, d, S):
		min = 1e7 #binahayat
		for v in range(self.V):
			if d[v] < min and S[v] == False:
				min = d[v]
				min_vertex = v
		return min_vertex
	def dijkstra(self, src):
		d = [1e7] * self.V
		d[src] = 0
		S = [False] * self.V
		u = src
		for cout in range(self.V):
			b = u
			u = self.minDistance(d, S)
			a = u
			if cout != 0:
				if self.graph[b][a] > 0:
					self.TreeEdge.append((b, a))   # moshakas kardan yal haye tree G
				else:
					minweight = 1e7 #binahayat
					for v in range(self.V):
						if 0 < self.graph[v][a] and d[v] < minweight and S[v] == True :
							b = v
							minweight = self.graph[b][a]
					self.TreeEdge.append((b, a))
			S[u] = True
			for v in range(self.V):
				if (self.graph[u][v] > 0 and    # shart vojod yal(hamsayeghi) 
				S[v] == False and               # v hayi ke dar S nistand(dar V-S hastand)
				d[v] > d[u] + self.graph[u][v]):
					d[v] = d[u] + self.graph[u][v]

		self.printSolution(d)
		self.plot_weighted_graph()

	def plot_weighted_graph(self):
		#add nodes
		G = nx.Graph()
		node_list = list(range(self.V))
		for node in node_list:
			G.add_node(node)
		for i in range(self.V):
			for j in range(self.V):
				if(self.graph[i][j] > 0):
					G.add_edge(i, j, weight = self.graph[i][j])
		black_edges = []			
		for i in node_list:
			for j in node_list:
				if 0 < self.graph[i][j] and	(i, j) not in self.TreeEdge and (j, i) not in self.TreeEdge :
					black_edges.append((i, j))

		edge_labels = dict([((u, v), d['weight'])
                 for u,v,d in G.edges(data = True)])
		pos = nx.spring_layout(G)
		nx.draw_networkx_nodes(G, pos)
		nx.draw_networkx_labels(G, pos)
		nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
		nx.draw_networkx_edges(G, pos, edgelist=self.TreeEdge, edge_color='r') #arrows=True
		nx.draw_networkx_edges(G, pos, edgelist=black_edges) #arrows=True
		plt.show()


if __name__ == "__main__":

	g = Graph(5)
	g.graph = [[0 , 5 , 0 , 9 , 1 ],
           [5 , 0 , 2 , 0 , 0 ],
           [0 , 2 , 0 , 6 , 0 ],
           [9 , 0 , 6 , 0 , 2 ],
           [1 , 0 , 0 , 2 , 0 ]]
	g.dijkstra(0)





