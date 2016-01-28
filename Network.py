#!/usr/bin/python
import numpy as np
from energy import *
from force import *

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
		self.L = L
		self.vertices = vertices
		self.cells = cells
		self.parameters = parameters


	# Potential Energy
	# ka(A - A0)^2 + kp(P - P0)^2
	def get_energy(self):
		cells = self.cells 
		vertices = self.vertices
		L = self.L

		ka = self.parameters['ka']
		e1 = E_elasticity(vertices, cells, ka, L)

		kp = self.parameters['kp']
		e2 = E_tension(vertices, cells, kp, L)
		# don't double count edges between cells
		e2 = e2 / 2.

		# print "Current Energy: %f\n" % (e1 + e2)
		return e1 + e2

	# forces on vertices
	# - derivative of energy wrt vertices
	# list of force vectors corresponding to every vertex
	# in the system
	def get_forces(self):
		cells = self.cells
		vertices = self.vertices
		L = self.L

		ka = self.parameters['ka']
		f1 = F_elasticity(cells, ka, vertices, L)

		kp = self.parameters['kp']
		f2 = F_tension(cells, kp, vertices, L)

		return -(f1 + f2)


	# # move vertices wrt forces 
	def move_vertices(self, f):
		delta_t = self.parameters['delta_t']
		vertices = self.vertices
		self.vertices = vertices + delta_t * f
		return 












