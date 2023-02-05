#!/usr/bin/env python3

import matplotlib.pyplot as plt
from random import random
from Geo_Data import *

plt.figure()
plt.plot(xlk,ylk)
plt.plot(xc1,yc1)
plt.plot(xc2,yc2)
plt.show()

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
	
	
	
	
#def pol_interesect_naive(polygon1, polygon2):
#	
#	n_lines1 = len(polygon1)-1
#	n_lines2 = len(polygon2)-1
#	
#	
#	for i in range(0, 2, n_lines1) :
#		for j in (0, 2, n_lines2) :
#			