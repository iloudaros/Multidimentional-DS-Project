import matplotlib.pyplot as plt
import bisect
from random import random


from .Geo_Data import *
from .Data_structures import *


# Η συνάρτηση ελέγχει αν υπάρχει τομή μεταξύ των ευθυγράμμων τμημάτων (p1, p2) και (p3, p4)
def intersect(line1, line2):
	
	x1,y1 = line1.start
	x2,y2 = line1.end
	x3,y3 = line2.start
	x4,y4 = line2.end
	
	denom = (y4-y3)*(x2-x1) - (x4-x3)*(y2-y1)
	
	if denom == 0: # Τότε τα τμήματα είναι παράλληλα
		return None
	ua = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / denom
	
	if ua < 0 or ua > 1: # Το σημείο τομής των ευθυών είναι πέρα από τα ευθύγραμμα τμήματα
		return None
	ub = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / denom
	
	if ub < 0 or ub > 1: # Το σημείο τομής των ευθυών είναι πέρα από τα ευθύγραμμα τμήματα
		return None
	x = x1 + ua * (x2-x1)
	y = y1 + ua * (y2-y1)
	return (x,y)

def intersect_demo():
	for i in range(4):
		points = [(random(), random()) for i in range(4)]
	
		(x1,y1),(x2,y2),(x3,y3),(x4,y4) = points
		plt.figure(figsize=(4,4))
		plt.plot((x1,x2), (y1,y2), '.r--')
		plt.plot((x3,x4), (y3,y4), '.b--')
	
		inter = intersect(Line((x1,y1), (x2,y2)), Line((x3,y3),(x4,y4))) 
	
		if inter is not None:
			plt.plot(*inter, 'ok', markersize=10)
		
		plt.show()
	
	
	
	
def pol_interesect_naive(polygon1, polygon2):
	
	n_lines1 = len(polygon1)-1
	n_lines2 = len(polygon2)-1
	points = []
	
	for i in range(n_lines1) :
		for j in range(n_lines2) :
			temp = intersect(Line(polygon1[i],polygon1[i+1]),Line(polygon2[j], polygon2[j+1]))
			if temp is not None:
				points.append(temp)	
	
	return points



def pol_intersect_sweep_line(polygon1, polygon2):
	# Define a list of all the edges in both polygons
	edges = []
	for i in range(len(polygon1) - 1):
		edges.append((polygon1[i], polygon1[i+1]))
	for i in range(len(polygon2) - 1):
		edges.append((polygon2[i], polygon2[i+1]))

	# Sort the edges by their x-coordinate
	edges.sort(key=lambda edge: edge[0][0])

	# Define a list of active edges
	active_edges = []

	# Define a list of intersection points
	intersection_points = []

	# Define the sweep line
	sweep_line = float('-inf')

	# Loop through the edges
	for edge in edges:
		# If the edge's left endpoint is to the right of the sweep line, remove it from the active edges
		while active_edges and active_edges[0][1][0] < sweep_line:
			active_edges.pop(0)

		# If the edge's left endpoint is to the left of the sweep line, add it to the active edges
		if edge[0][0] < sweep_line:
			active_edges.append(edge)

		# Loop through the active edges and check for intersections
		for active_edge in active_edges:
			intersection = intersect(Line(edge[0], edge[1]), Line(active_edge[0], active_edge[1]))
			if intersection is not None:
				intersection_points.append(intersection)

		# Update the sweep line
		sweep_line = edge[0][0]

	# Return the intersection points
	return intersection_points