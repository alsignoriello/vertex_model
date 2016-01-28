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

	def __init__(self, id, indices, A0, P0):
		self.id = id
		self.indices = indices
		self.A0 = A0
		self.P0 = P0


	# return list of vertices
	# with periodic boundaries 
	def get_cell_vertices(self, vertices, L):
		indices = self.indices
		nsides = len(indices)

		# array of x,y vertices in counter-clockwise order
		# moving vertices to maintain periodic boundaries
		cell_vertices = []

		# align everything to first vertex
		x0,y0 = vertices[indices[0]]
		v0 = np.array((x0,y0))

		for i in indices:
			# print vertices 
			x,y = vertices[i]
			v = np.array((x,y))
			v_next = v0 + periodic_diff(v, v0, L)
			x,y = v_next
			cell_vertices.append((x,y))
		return cell_vertices

	def get_area(self, vertices, L):
		cell_vertices = self.get_cell_vertices(vertices, L)
		a = area(cell_vertices)
		# print a
		return a 

	def get_perim(self, vertices, L):
		cell_vertices = self.get_cell_vertices(vertices, L)
		p = perimeter(cell_vertices)
		return p

	def get_center(self, vertices, L):
		x,y = center(self.get_cell_vertices(vertices, L))
		return x,y

	# occurs during a T1 transition
	def update_indices(self):
		pass


	def get_neighbor_list(self):
		pass