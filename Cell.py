#!/usr/bin/python
import numpy as np
from geometry import 


""" 

Cell.py - Class Cell to define unique characteristics 
of every cell in the network 

author: Lexi Signoriello
date: 1/19/16

vertices - 	list of all vertices in the network

indices - 	indices mapping to vertices 
			for every vertex in current cell 
			* counter-clockwise order 

n_sides - 	number of sides in polygon for given cell


"""


class Cell:

	def __init__(self, vertices, indices):
		self.vertices = vertices
		self.n_sides = len(indices)
		self.area = get_area(vertices)
		self.perimeter = get_perimeter()
		# self.neighbor_list = 


	def get_cell_vertices:
		cell_vertices = []
		return cell_vertices

