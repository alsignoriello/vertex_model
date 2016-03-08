#!/usr/bin/python
import numpy as np
from Network import Network
from transition import *
from parser import write_cell_indices
from plot import plot_network
from geometry import rand_angle

def steepest_descent(network, vertices, cells, edges, delta_t, epsilon):

	# keep track of time steps
	time = []
	t = 0

	# keep track of energy
	energy = []

	# for T1 transition
	min_dist = 0.2

	L = network.L

	# while forces are greater than epsilon
	forces = epsilon**0.5
	count = 0

	# generate random angle vectors
	for cell in cells:
		cell.theta = rand_angle()
		
	while count < 500:
	# while np.sum(forces**2)**(0.5) > epsilon:
		if count % 5 == 0:
			plot_network(vertices, cells, L, "motility5/%d.jpg" % count)

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
		cells, edges = T1_transition(network, vertices, cells, edges, min_dist)
		count += 1

		# exit()
	return vertices