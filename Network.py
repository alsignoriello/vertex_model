#!/usr/bin/python
import numpy as np

"""

Network.py - Class Network to define characteristics of the
network connected by vertices

author: Lexi Signoriello 
date: 1/20/16


vertices - list of all vertices in network
			(x0, y0), (x1, y1) ... (xN, yN)

n_vertices - number of vertices in network

L = [lx, ly]
lx - side length in x direction of surrounding box
ly - side length in y direction of surrounding box

cells - list of Cells 
n_cells - number of cells in network

energy - potential energy in the system

forces - forces in system contribute to movement

parameters - dictionary containing relevant parameter values


"""


class Network:


	def __init__(self, L, vertices, cells, parameters):
		self.lx = L[0]
		self.ly = L[1]
		self.vertices = vertices
		self.cells = cells
		self.n_cells = len(cells)
		self.n_vertices = len(vertices)
		self.energy = get_energy(self)


	# Potential energy in the current configuration
	# 3 forces:
	#	Elasticity of cells
	# 	Actin-Myosin in cytoskeleton
	#	Adhesion molecules
	def get_energy():
		# Elasticity iterates over all cells
		pass

	def build_edge_list():
		pass








