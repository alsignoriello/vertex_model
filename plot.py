import matplotlib.pyplot as plt
import sys
from parser import *
from geometry import periodic_diff

"""

plot.py - plots the network for vertex model


author: Lexi Signoriello
date: 1/19/16

[vertices] [edges]

options:
	vertices

	line color

	color by number of neighbors
	color by area


"""


def plot_network(vertices, cells, L):
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)
	for vertex in vertices:
		x = vertex[0]
		y = vertex[1]
		ax.scatter(x, y, c="c")

	for cell in cells:
		indices = cell.indices
		for i,index in enumerate(indices):
			x1,y1 = vertices[index]
			if i == len(indices) - 1:
				x2,y2 = vertices[indices[0]]
			else:
				x2,y2 = vertices[indices[i+1]]

			v1 = np.array((x1,y1))
			v2 = np.array((x2,y2))
			v2 = v1 + periodic_diff(v2, v1, L)
			x2,y2 = v2
			ax.plot([x1,x2],[y1,y2],c="k")

	ax.axis([0,L[0],0,L[1]])
	plt.show()
	return



# # files to read for plotting
# cell_file = "cells.txt"
# cell_vertex_file = "cell_vertices"
# network_file = "network.txt"
# network_vertex_file = "network_vertices.txt"
# network_edge_file = "network_edges.txt"

# # open files
# network_vertices = read_network_vertices(network_vertex_file)
# x = network_vertices[:,0]
# y = network_vertices[:,1]
# print x,y

# # close files



# # initalize plot
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)

# # plot vertices 
# ax.scatter(x,y,c="k")

# # plot edges


# # show plot
# plt.show()

# # save plot


# # close plot
# # plt.close(fig)


