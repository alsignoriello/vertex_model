#!/usr/bin/python
import numpy as np
from Polygon import Polygon

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


def read_poly_indices(file):
	# indices = np.loadtxt(file, dtype=int)
	indices = []
	f = open(file)
	for line in f:
		poly_indices = []
		linesplit = line.strip().split("\t")
		for i in linesplit:
			poly_indices.append(int(i))
		indices.append(poly_indices)
	f.close()
	return indices


def build_polygons(cell_indices, A0):
	polys = []
	for i,indices in enumerate(cell_indices):
		poly = Polygon(i, indices, A0)
		polys.append(poly)
	return polys


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


















# def write_cell_indices(cells, file):
# 	f = open(file, "w+")
# 	for cell in cells:
# 		for i in cell.indices:
# 			f.write("%d\t" % i)
# 		f.write("\n")
# 	f.close()
# 	return 


# def write_cells(cells, file):
# 	f = open(file,"w+")
# 	for cell in cells:
# 		f.write("%f\t%f\t%f\t%f\n" % (cell.x, cell.y, 
# 									cell.area, cell.perim))
# 	f.close()
# 	return
