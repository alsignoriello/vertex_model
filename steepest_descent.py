#!/usr/bin/python
import numpy as np
from Network import Network
from parser import build_cells

def steepest_descent(network, delta_t, epsilon):

	# keep track of time steps
	time = []
	t = 0

	# keep track of energy
	energy = []

	# while forces are greater than epsilon
	f = epsilon**0.5
	while np.sum(f**2)**(0.5) > epsilon:

		# get energy for network
		e = network.get_energy()
	
		# get forces for network
		f = network.get_forces()
	
		# move vertices with forces
		vertices = network.move_vertices(f)

		print t, e, np.sum(f**2)**(0.5)
		t += delta_t

	return t, energy