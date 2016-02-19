#!/usr/bin/python
import numpy as np
import sys
from Network import Network
from parser import *
from steepest_descent import steepest_descent
import matplotlib.pyplot as plt
from plot import plot_network, plot_edges

"""

run.py - runs vertex model simulation
		initalizes vertex model
		minimizes energy using steepest descent
		plots the relaxed network

author: Lexi Signoriello
date: 	1/20/16



Notes:
The network should have vertices that each have exactly
3 edges each

Duplicate edges in reverse order in edge list

Periodic Boundary Conditions


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
gamma = 0.001
# gamma = 0.04 * ka * A0 # hexagonal network
# gamma = 0.1 * ka * A0 # soft network
parameters['gamma'] = gamma

# # tau - line tension between cell
# linear coefficient 
tau = 0.12 * ka * (A0**(3/2)) # hexagonal network
# tau = -0.85 * ka * A0**(3/2) # soft network
# tau = 0.01
parameters['tau'] = tau

# delta_t - time step 
delta_t = 0.05
parameters['delta_t'] = delta_t

# Read Files
# read in list of all vertices in network
vertex_file = "network_vertices.txt"
vertices = read_vertices(vertex_file)

# read cell indices 
# cell_index_file = "cell_indices.txt"
cell_index_file = "cells_T1.txt"
cell_indices = read_cell_indices(cell_index_file)

# Build cells
cells = build_cells(cell_indices, A0, P0)
print "There are %d cells" % (len(cells))

# read edge list
# edge_file = "edges.txt"
edge_file = "edges_T1.txt"
edges = read_edges(edge_file)


# plot_network(vertices, cells, L, "hex_network_T0.jpg")

network = Network(L, parameters)

# # steepest descent
epsilon = 10**-6

vertices = steepest_descent(network, vertices, cells, edges, delta_t, epsilon)

plot_network(vertices, cells, L, "hex_network_2.jpg")



