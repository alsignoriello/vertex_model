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

def read_cells():
	cells = []
	f = open("cells.txt", "r")
	for line in f:
		linesplit = line.split("\t")
		x = linesplit[0]
		y = linesplit[1]
		area = linesplit[2]
		perim = linesplit[3]
	f.close()
	return x, y, area, perim

def read_cell_vertices():
	f = open("cell_vertices.txt", "r")
	for i,line in f:
		vertices = line.strip().split("\t")
		vertices = [float(vertex) for vertex in vertices]
	f.close()
	return

def write_cells(cells):
	f = open("cells.txt","w+")
	for cell in cells:
		f.write("%f\t%f\t%f\t%f\n" % (cell.x, cell.y, cell.area, cell.perim))
	f.close()
	return

def write_cell_vertices(cells):
	f = open("cell_vertices.txt","w+")
	for cell in cells:
		cell_vertices = cell.get_cell_vertices(vertices)
		for vertex in cell_vertices:
			f.write("%f\t" % vertex)
		f.write("\n")
	f.close()
	return


# Read/Write class network
def read_network():
	pass


def write_network():
	pass



def read_network_vertices():
	pass

def write_network_vertices():
	pass

def read_network_edges():
	pass


def write_network_edges():
	

