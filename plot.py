import matplotlib.pyplot as plt
import sys
from parser import *

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

# files to read for plotting
cell_file = "cells.txt"
cell_vertex_file = "cell_vertices"
network_file = "network.txt"
network_vertex_file = "network_vertices.txt"
network_edge_file = "network_edges.txt"

# open files
network_vertices = read_network_vertices(network_vertex_file)
x = network_vertices[:,0]
y = network_vertices[:,1]
print x,y

# close files



# initalize plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# plot vertices 
ax.scatter(x,y,c="k")

# plot edges


# show plot
plt.show()

# save plot


# close plot
# plt.close(fig)


