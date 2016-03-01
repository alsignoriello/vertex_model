#!/usr/bin/python
import numpy as np
from Cell import Cell

"""

parser.py - defines functions to read and write relevant data


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

def read_cell_indices(file):
	# indices = np.loadtxt(file, dtype=int)
	indices = []
	f = open(file)
	for line in f:
		cell_indices = []
		linesplit = line.strip().split("\t")
		for i in linesplit:
			cell_indices.append(int(i))
		indices.append(cell_indices)
	f.close()
	return indices

def write_cell_indices(cells, file):
	f = open(file, "w+")
	for cell in cells:
		for i in cell.indices:
			f.write("%d\t" % i)
		f.write("\n")
	f.close()
	return 

def build_cells(cell_indices, A0, P0, theta):
	cells = []
	for i,indices in enumerate(cell_indices):
		cell = Cell(i, indices, A0, P0, theta)
		cells.append(cell)
	return cells

def write_cells(cells, file):
	f = open(file,"w+")
	for cell in cells:
		f.write("%f\t%f\t%f\t%f\n" % (cell.x, cell.y, 
									cell.area, cell.perim))
	f.close()
	return

def read_vertices(file):
	vertices = np.loadtxt(file)
	return vertices

def write_vertices(vertices, file):
	np.savetxt(file, vertices)
	return

# i1 i2
# indices for edge from v1 to v2
def read_edges(file):
	edges = np.loadtxt(file).astype(int)
	return edges













# old edge parser 
# edges0 = np.loadtxt(file).astype(int)
# edges = np.zeros((len(edges0)*3, 2)).astype(int)
# counter = 0
# for i,edge in enumerate(edges0):
# 	for j in edge:
# 		# print i, j
# 		edges[counter, 0] = i
# 		edges[counter, 1] = j
# 		counter += 1
# np.savetxt("edges.txt", edges, fmt="%d")
# exit()
