#!/usr/bin/python
import numpy as np
from geometry import *

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

L - length of box
	* used to compute periodic boundary conditions

"""


class Cell:

	def __init__(self, id, vertices, indices, L):
		self.id = id
		self.L = L
		self.vertices = vertices
		self.indices = indices
		self.n_sides = len(indices)
		# self.x, self.y = get_center(self.get_cell_vertices())
		# self.area = get_area(self.get_cell_vertices())
		# self.perim = get_perimeter(self.get_cell_vertices())
		# self.neighbor_list =


	# return list of vertices
	# with periodic boundaries 
	def get_cell_vertices(self):
		indices = self.indices
		vertices = self.vertices
		cell_vertices = []
		L = self.L

		# align everything to first vertex
		x0,y0 = vertices[indices[0]]
		v0 = np.array((x0,y0))

		for i in indices:
			x,y = vertices[i]
			v = np.array((x,y))
			v_next = v0 + periodic_diff(v, v0, L)
			x,y = v_next
			cell_vertices.append((x,y))
		return cell_vertices


	def update_vertices(self, vertices):
		self.vertices = vertices
		return

	def get_area(self):
		a = area(self.get_cell_vertices())
		return a 

	def get_perim(self):
		p = perimeter(self.get_cell_vertices())
		return p

	def get_center(self):
		x,y = center(self.get_cell_vertices())
		return x,y


	def get_neighbor_list(self):
		pass