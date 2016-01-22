#!/usr/bin/python
import numpy as np
from energy import *
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
		self.parameters = parameters

	# Potential energy in the current configuration
	# 3 forces:
	#	Elasticity of cell area 
	# 	Actin-Myosin in cytoskeleton (perimeter)
	#	Adhesion molecules
	def get_energy_elasticity(self):
		e = E_elasticity(self.cells, self.parameters['A0'],
						self.parameters['k_a'])
		return e

	def get_energy_contraction(self):
		e = E_contraction(self.cells, self.parameters['k_p'])
		return e

	def get_energy_adhesion(self):
		e = E_adhesion(self.cells, self.parameters['gamma'])
		return e

	def get_force_elasticity(self):
		pass

	def get_force_actin(self):
		pass

	def get_force_adhesion(self):
		pass








