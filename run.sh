#!/usr/bin/bash

vertex_file=$1
edge_file=$2
poly_file=$3

python relax.py $vertex_file $edge_file $poly_file 

# later, will add division simulations..
# python divide.py $vertex_file $edge_file $poly_file 

