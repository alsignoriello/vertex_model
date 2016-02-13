#!/usr/bin/python
import numpy as np
from Network import Network

def steepest_descent(network, vertices, cells, edges, delta_t, epsilon):

	# keep track of time steps
	time = []
	t = 0

	# keep track of energy
	energy = []

	# for T1 transition
	min_dist = 0.3

	# while forces are greater than epsilon
	forces = epsilon**0.5
	while np.sum(forces**2)**(0.5) > epsilon:

		# get energy for network
		energy = network.get_energy(vertices, cells, edges)

		# get forces for network
		forces = network.get_forces(vertices, cells, edges)
	
		# move vertices with forces
		vertices = network.move_vertices(forces, vertices)

		ka = network.parameters['ka']
		A0 = 1.
		print t, energy / (24.*ka*(A0**2)), np.sum(forces**2)**(0.5)
		
		# new time step
		t += delta_t

		# # check for T1 transitions
		cells, edges = network.T1(vertices, cells, edges, min_dist)
		exit()
	return t, energy, vertices, cells, edges