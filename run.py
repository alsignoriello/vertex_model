#!/usr/bin/python
import numpy as np
import sys
from Network import Network
from parser import *
from steepest_descent import steepest_descent
import matplotlib.pyplot as plt
from plot import plot_network

"""

build_network.py - initializes the vertex model

builds cells
builds network
computes energy + forces in network

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
# parameters['L'] = L

# # ka - elastic area coefficient
ka = 1.
parameters['ka'] = ka

# # # A0 - preferred area for cell
# # This will be a list later
A0 = 1.
# parameters['A0'] = A0

# kp - coefficient for line tension and 
# 		maintaining surface area
kp = 0.1
parameters['kp'] = kp


# #  P0 - preferred perimeter for cell
# # This will be a list later
P0 = 0.2
# parameters['P0'] = P0

# # gamma - actin myosin contractility
gamma = 0.04 * ka * A0
parameters['gamma'] = gamma

# # tau - line tension between cell
# linear coefficient 
tau = 0.12 * ka * (A0**(3/2))
# tau = 0.01
parameters['tau'] = tau

# delta_t - time step 
delta_t = 0.05
parameters['delta_t'] = delta_t

# Read Files
# read in list of all vertices in network
vertex_file = "network_vertices.txt"
vertices = read_network_vertices(vertex_file)

# read cell indices 
cell_index_file = "cell_indices.txt"
cell_indices = read_cell_indices(cell_index_file)

# read edge list
edge_file = "edge_indices.txt" 
edges = read_edges(edge_file)
# print len(edges)

# Build cells
cells = build_cells(cell_indices, A0, P0)
print "There are %d cells" % (len(cells))

network = Network(L, vertices, cells, edges, parameters)

# # steepest descent
epsilon = 10**-6

time, energy, vertices, cells, edges = steepest_descent(network, vertices, cells, edges, delta_t, epsilon)

plot_network(vertices, cells, L)

# show plot
plt.show()

