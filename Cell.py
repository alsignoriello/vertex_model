#!/usr/bin/python
import numpy as np
from geometry import get_area, get_perimeter, get_center

""" 

Cell.py - Class Cell to define unique characteristics 
of every cell in the network 

author: Lexi Signoriello
date: 	1/19/16

vertices - 	list of all vertices in the network
[(x0,y0), (x1,y1) .... (xNvertices,yNvertices)]

cell_vertices - list of vertices in current cell
[(x0,y0), (x1,y1) ... (xNsides,yNsides)]

indices - 	indices mapping to vertices 
			for every vertex in current cell 
			* counter-clockwise order 

n_sides - 	number of sides in polygon for given cell

x, y - geometric center

"""


class Cell:

	def __init__(self, id, vertices, indices):
		self.id = id
		self.indices = indices
		self.n_sides = len(indices)
		self.x, self.y = get_center(self.get_cell_vertices(vertices))
		self.area = get_area(self.get_cell_vertices(vertices))
		self.perim = get_perimeter(self.get_cell_vertices(vertices))
		# self.neighbor_list =


	def get_cell_vertices(self,vertices):
		cell_vertices = []
		for index in self.indices:
			x,y = vertices[index]
			cell_vertices.append((x,y))
		return cell_vertices


	def get_neighbor_list():
		pass