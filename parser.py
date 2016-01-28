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

def read_cell_indices(file):
	indices = np.loadtxt(file, dtype=int)
	return indices

def build_cells(cell_indices, A0, P0):
	cells = []
	for i,indices in enumerate(cell_indices):
		cell = Cell(i, indices, A0, P0)
		cells.append(cell)
	return cells

def write_cells(cells, file):
	f = open(file,"w+")
	for cell in cells:
		f.write("%f\t%f\t%f\t%f\n" % (cell.x, cell.y, 
									cell.area, cell.perim))
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


