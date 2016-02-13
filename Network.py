#!/usr/bin/python
import numpy as np
from energy import *
from force import *
from transition import *

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


	def T1(self, vertices, cells, edges, min_dist):
		L = self.L

		for edge in edges:
			i1 = edge[0]
			i2 = edge[1]

			v1 = vertices[i1]
			vertex2 = vertices[i2]
			v2 = v1 + periodic_diff(vertex2, v1, L)

			dist = euclidean_distance(v1[0], v1[1], v2[0], v2[1])

			if dist < min_dist:
				print "T1"
				cell_ids = get_4_cells(cells, i1, i2)
				if -1 in cell_ids:
					# print cell_ids
					pass
				else:
					# find minimum configuration

					# original configuration
					cells_0, edges_0 = T1_0(cells, edges, i1, i2, cell_ids)
					E0 = self.get_energy(vertices, cells_0, edges_0)
					print E0

					# left T1 transition 
					cells_l, edges_l = T1_left(cells, edges, i1, i2, cell_ids)
					E_left = self.get_energy(vertices, cells_l, edges_l)
					print E_left

					# for cell in cells_l:
					# 	print cell.indices

					# for cell in cells:
					# 	print cell.indices
					# exit()

					# # right T1 transition
					cells_r, edges_r = T1_right(cells, edges, i1, i2, cell_ids)
					# E_right = self.get_energy(vertices, cells_r, edges_r)

					# get minimum
					# min_energy = np.minimum((E0, E_left, E_right))


					# if current configuration is minimum

					# else: replace cells and edges


		return cells, edges














