# Dijkstra-Minimum-Spanning-Tree
This program plot the MST and gives the minimum distance form each staring point to other vertices.
the input is given ti the program by a 2d arry as graph matrix\
# Example
**input**\
	g = Graph(5)\
	g.graph = [[0 , 5 , 0 , 9 , 1 ],\
           [5 , 0 , 2 , 0 , 0 ],\
           [0 , 2 , 0 , 6 , 0 ],\
           [9 , 0 , 6 , 0 , 2 ],\
           [1 , 0 , 0 , 2 , 0 ]]\
	g.dijkstra(0)\
 
 **output**\
Vertex 	 Distance from Source\
0 		 0\
1 		 5\
2 		 7\
3 		 3\
4 		 1\

![Figure_1](https://github.com/user-attachments/assets/5d9eb506-9909-44a3-afcd-46c0e37628f9)
