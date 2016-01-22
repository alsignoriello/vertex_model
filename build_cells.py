#!/usr/bin/python
import numpy as np
import sys
from Cell import Cell


"""

build_cells.py - initializes an object cell for every
cell in the network

author: Lexi Signoriello
date: 	1/21/16


"""

# File with coordinates for all vertices in network
# x \t y
vertex_file = "vertices.txt"

# File with indices for all vertices surrounding cells
# i_1, i_2, .... i_Nsides 
cell_file = "cell_indices.txt"

network_vertices = np.loadtxt(vertex_file)
n_vertices = len(network_vertices)
print "There are %d vertices" % n_vertices
for vertex in network_vertices:
	print "(x,y) = (%f,%f)" % (vertex[0], vertex[1])


cell_indices = np.loadtxt(cell_file)
n_cells = len(cell_file)
print "There are %d cells" % n_cells

# change to 0 base
cell_indices = cell_indices - 1

# list to hold all cells
cells = []
for i,indices in enumerate(cell_indices):
	cell = Cell(i, network_vertices, indices)
	print cell.area, cell.perim
	cells.append(cell)
	print cell.get_cell_vertices(network_vertices)


