#!/usr/bin/python
import numpy as np
import sys
from Cell import Cell
from parser import *

"""

build_cells.py - initializes an object cell for every
cell in the network

author: Lexi Signoriello
date: 	1/21/16


"""

# File with coordinates for all vertices in network
# x \t y
vertex_file = "network_vertices.txt"

# network_vertices = np.loadtxt(vertex_file)
# n_vertices = len(network_vertices)
# print "There are %d vertices" % n_vertices
# # for vertex in network_vertices:
# # 	print "(x,y) = (%f,%f)" % (vertex[0], vertex[1])

# File with indices for all vertices surrounding cells
# i_1, i_2, .... i_Nsides 
index_file = "cell_indices.txt"

# cell_indices = np.loadtxt(cell_file)
# n_cells = len(cell_file)
# print "There are %d cells" % n_cells

# # list to hold all cells
# cells = []
# for i,indices in enumerate(cell_indices):
# 	cell = Cell(i, network_vertices, indices)
# 	cells.append(cell)
# 	# print cell.area, cell.perim
# 	# print cell.get_cell_vertices(network_vertices)

# build cells
cells = build_cells(vertex_file, index_file)

# write cell file
write_cells(cells, "cells.txt")

# write cell vertices 
# write_cell_vertices(cells, network_vertices, "cell_vertices.txt")


