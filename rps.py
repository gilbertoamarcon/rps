#!/usr/bin/env python3
import sys
import numpy.random as rnd

# Printing position list
def print_pos(str,pos_list):
	print str
	for p in pos_list:
		print "(%6.3f,%6.3f)"%(p[0],p[1])
	print ""

# Printing distance matrix
def print_dist(str,mat):
	print str
	for i in range(1,len(mat)):
		for j in range(0,i):
			sys.stdout.write("%8.3f"%mat[i][j])
		print ""
	print ""

# Compute vector distance
def dist(vec_a, vec_b):
	return (((vec_a[0] - vec_b[0])**2) + ((vec_a[1] - vec_b[1])**2))**0.5

# Estimate relative robot positions from relative distance measurements
def estimate_relative_pos(measured_dists,gess_range=1.0,step_size=0.001,iterations=1e3,verbose=0):

	# Getting number of robots
	N = len(measured_dists)

	# Square distances matrices
	sqr_measured_dists	= [[0 for i in range(N)] for i in range(N)]
	sqr_est_dists		= [[0 for i in range(N)] for i in range(N)]

	# Measured distances squared
	for i in range(N):
		for j in range(0,i):
			sqr_measured_dists[i][j] = measured_dists[i][j]**2

	# Random initial position estimate
	est_pos = rnd.normal(scale=gess_range, size=(N,2))

	# Gradient descent loop
	for it in range(iterations):
		for i in range(N):
			for j in range(0,i):
				sqr_est_dists[i][j] = dist(est_pos[i], est_pos[j])**2
				e = sqr_measured_dists[i][j]-sqr_est_dists[i][j]
				est_pos[i][0] += step_size*e*(est_pos[i][0]-est_pos[j][0])
				est_pos[i][1] += step_size*e*(est_pos[i][1]-est_pos[j][1])
				est_pos[j][0] += step_size*e*(est_pos[j][0]-est_pos[i][0])
				est_pos[j][1] += step_size*e*(est_pos[j][1]-est_pos[i][1])

	if verbose:
		print_dist("Measured distances squared:",sqr_measured_dists)
		print_dist("Estimate distances squared:",sqr_est_dists)

	return est_pos

# Generate distance measured_dists from ground truth
def gen_measurements(gt_pos,noise=0.0):

	# Getting number of robots
	N = len(gt_pos)

	# Distances matrices
	measured_dists = [[0 for i in range(N)] for i in range(N)]

	# Measured distances
	for i in range(N):
		for j in range(0,i):
			measured_dists[i][j] = dist(gt_pos[i], gt_pos[j])

	# Adding Gaussian noise
	if noise > 0.0:
		measured_dists += rnd.normal(scale=noise, size=(N,N))

	return measured_dists
