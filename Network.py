#!/usr/bin/python
import numpy as np
from energy import *
from force import *
from transition import T1

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


	def __init__(self, L, vertices, cells, edges, parameters):
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

		return (f1 + f2 + f3)


	# # move vertices wrt forces 
	def move_vertices(self, f, vertices):
		delta_t = self.parameters['delta_t']
		vertices = vertices + delta_t * f
		return vertices 


	def T1_transitions(self, vertices, cells, edges, min_dist):
		L = self.L

		# iterate over edges 
		for i,edge in enumerate(edges):
			# iterate over edge indices
			for index in edge:
				# get vertices
				v0 = vertices[i]
				v = vertices[index]
				# get vertex 2 wrt periodic boundaries
				v1 = v0 + periodic_diff(v, v0, L)

				dist = euclidean_distance(v0[0], v0[1], v1[0], v1[1])
			
				if dist < min_dist:
					print "T1\n" #dist
					# T1 transition
					# self.cells, self.edges = T1(cells, edges, L, i, index)

		return cells, edges














