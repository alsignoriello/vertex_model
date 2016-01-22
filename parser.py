#!/usr/bin/python
import numpy as np
from Cell import Cell

"""

parser.py - defines functions to read and write relevant data
for the system 

author: Lexi Signoriello
date: 1/22/16



"""

# Read/Write class cells
# Write to tab-delimited text file
# cell file - relevant quantities for cells
# Center_x Center_y Area Perimeter  
# vertex file - list of vertices surrounding every cell
# x0 y0 x1 y1 .... xN yN
# cell and vertex file 1-1 map
def read_cells(cell_file):
	xs = []
	ys = []
	areas = []
	perims =[]
	f = open(cell_file, "r")
	for i,line in enumerate(f):
		linesplit = line.split("\t")
		x = linesplit[0]
		xs.append(x)
		y = linesplit[1]
		ys.append(y)
		area = linesplit[2]
		areas.append(area)
		perim = linesplit[3]
		perims.append(perim)
	f.close()
	return xs, ys, areas, perims

def read_cell_vertices(file):
	f = open(file, "r")
	for i,line in f:
		vertices = line.strip().split("\t")
		vertices = [float(vertex) for vertex in vertices]
	f.close()
	return

def read_cell_indices(file):
	indices = np.loadtxt(file)
	return indices

def build_cells(vertex_file, index_file):
	cells = []
	network_vertices = read_network_vertices(vertex_file)
	cell_indices = read_cell_indices(index_file)
	for i,indices in enumerate(cell_indices):
		cell = Cell(i, network_vertices, indices)
		cells.append(cell)
	return cells

def write_cells(cells, file):
	f = open(file,"w+")
	for cell in cells:
		f.write("%f\t%f\t%f\t%f\n" % (cell.x, cell.y, cell.area, cell.perim))
	f.close()
	return

def write_cell_vertices(cells, vertices, file):
	f = open(file,"w+")
	for cell in cells:
		cell_vertices = cell.get_cell_vertices(vertices)
		for x,y in cell_vertices:
			f.write("%f\t%f\t" % (x,y))
		f.write("\n")
	f.close()
	return


# Read/Write class network
def read_network(file):
	pass


def write_network(file, network):
	pass


def read_network_vertices(file):
	vertices = np.loadtxt(file)
	return vertices

def write_network_vertices(vertices, file):
	np.savetxt(file, vertices)
	return



























# may be repeated information....

# def build_network edges(vertex_file, index_file):
# 	vertices = read_network_vertices(vertex_file)
# 	edge_indices = np.loadtxt(index_file)
# 	edges = []
# 	for i,indices in enumerate(edge_indices):
# 		# edge 1

# 		# edge 2 

# 		# edge 3

# 		# check if edge already exists

# 		# remove if already there

# 	return edges

# def read_network_edges(file):
# 	edges = []
# 	f = open(file, "r")
# 	for line in f:
# 		linesplit = line.split("\t")
# 		x0 = float(linesplit[0])
# 		y0 = float(linesplit[1])
# 		x1 = float(linesplit[2])
# 		y1 = float(linesplit[3])
# 		edges.append([x0,y0,x1,y1])
# 	return edges


# def write_network_edges(edges, file):
# 	f = open(file, "w+")
# 	for edge in edges:
# 		x0,y0,x1,y1 = edge
# 		f.write("%f\t%f\t%f\t%f\n" %
# 					(x0,y0,x1,y1))
# 	return










