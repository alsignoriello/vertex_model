#!/usr/bin/python
import numpy as np
from Network import Network

def steepest_descent(network, delta_t, epsilon):

	# keep track of time steps
	time = []
	t = 0

	# keep track of energy
	energy = []

	# while forces are greater than epsilon
	forces = epsilon**0.5
	while np.sum(forces**2)**(0.5) > epsilon:

		# get energy for network
		energy = network.get_energy()

		# get forces for network
		forces = network.get_forces()
	
		# move vertices with forces
		vertices = network.move_vertices(forces)

		ka = network.parameters['ka']
		A0 = 1.
		# print t, energy / (24.*ka*(A0**2)), np.sum(forces**2)**(0.5)
		
		# new time step
		t += delta_t

		# check for T1 transitions
		min_dist = 0.2
		network.T1_transitions(min_dist)

	return t, energy