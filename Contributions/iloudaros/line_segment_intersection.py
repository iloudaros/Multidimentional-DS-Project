import matplotlib.pyplot as plt
from random import random
from Geo_Data import *


# Η συνάρτηση ελέγχει αν υπάρχει τομή μεταξύ των ευθυγράμμων τμημάτων (p1, p2) και (p3, p4)
def intersect(p1, p2, p3, p4):
	
	x1,y1 = p1
	x2,y2 = p2
	x3,y3 = p3
	x4,y4 = p4
	
	denom = (y4-y3)*(x2-x1) - (x4-x3)*(y2-y1)
	
	if denom == 0: # Τότε τα τμήματα είναι παράλληλα
		return None
	ua = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / denom
	
	if ua < 0 or ua > 1: # out of range
		return None
	ub = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / denom
	
	if ub < 0 or ub > 1: # out of range
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
	
		inter = intersect(*points) 
	
		if inter is not None:
			plt.plot(*inter, 'ok', markersize=10)
		
		plt.show()
	
	
	
	
def pol_interesect_naive(polygon1, polygon2):
	
	n_lines1 = len(polygon1)-1
	n_lines2 = len(polygon2)-1
	points = []
	
	for i in range(n_lines1) :
		for j in range(n_lines2) :
			temp = intersect(polygon1[i],polygon1[i+1],polygon2[j], polygon2[j+1])
			if temp is not None:
				points.append(temp)	
	
	return points

