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


	def __init__(self, L, parameters):
		self.L = L
		self.parameters = parameters


	def get_energy(self, vertices, cells, edges):
		L = self.L

		ka = self.parameters['ka']
		e1 = E_elasticity(vertices, cells, ka, L)
		
		tau = self.parameters['tau']
		e2 = E_adhesion(vertices, edges, tau, L)
		# take into account double counting edges
		e2 = e2 / 4.
		
		gamma = self.parameters['gamma']
		e3 = E_actin_myosin(vertices, cells, gamma, L)

		return e1 + e2 + e3

	def get_forces(self, vertices, cells, edges):
		L = self.L

		ka = self.parameters['ka']
		f1 = F_elasticity(vertices, cells, ka, L)

		tau = self.parameters['tau']
		f2 = F_adhesion(vertices, edges, tau, L)
		
		gamma = self.parameters['gamma']	
		f3 = F_actin_myosin(vertices, cells, gamma, L)

		km = self.parameters['km']
		f4 = F_motility(vertices, cells, km)

		return (f1 + f2 + f3 + f4)


	# # move vertices wrt forces 
	def move_vertices(self, f, vertices):
		delta_t = self.parameters['delta_t']
		vertices = vertices + delta_t * f

		L = self.L
		# wrap around periodic boundaries
		for i,(x,y) in enumerate(vertices):
			if x < 0:
				# wrap around to right
				vertices[i,0] = x + L[0]

			if x > L[0]:
				# wrap around to left
				vertices[i,0] = x - L[0]

			if y < 0:
				# wrap around to top
				vertices[i,1] = y + L[1]

			if y > L[1]:
				# wrap around to bottom
				vertices[i,1] = y - L[1]

		return vertices 












