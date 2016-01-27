#!/usr/bin/python
import numpy as np
import sys
from Network import Network
from parser import *
from steepest_descent import steepest_descent

"""

build_network.py - initializes the vertex model

Builds Class Network to describe current configuration


author: Lexi Signoriello
date: 	1/20/16


"""


''' set initial parameters ''' 
# store parameters in dictionary
parameters = {}

# Side length of box in x direction
lx = 9 * (2 / (3 * (3**0.5)))**0.5

# Side length of box in y directions
ly = 4 * (2 / (3**0.5))**0.5

L = np.array([lx,ly])
parameters['L'] = L

# # ka - elastic area coefficient
ka = 1.
parameters['ka'] = ka

# # A0 - preferred area for cell
# This will be a list later
A0 = 1.
parameters['A0'] = A0

# kp - coefficient for line tension and 
# 		maintaining surface area
kp = 1. 
parameters['kp'] = kp


#  P0 - preferred perimeter for cell
# This will be a list later
P0 = 5.
parameters['P0'] = P0

# # gamma - line tension between cells
# # linear coefficient
# gamma = 1.
# parameters['gamma'] = gamma

# delta_t - time step 
delta_t = 0.05
parameters['delta_t'] = delta_t

# read in list of all vertices in network
network_vertex_file = "network_vertices.txt"
network_vertices = read_network_vertices(network_vertex_file)

# read in cells
cell_index_file = "cell_indices.txt"
cells = build_cells(network_vertex_file, cell_index_file, L)
print "There are %d cells\n" % (len(cells))

print parameters

network = Network(L, network_vertices, cells, parameters)

energy = network.get_energy()
print energy

forces =  network.get_forces()
print forces

# steepest descent
epsilon = 10**-6

time, energy = steepest_descent(network, cells, delta_t, epsilon)


# plot network




