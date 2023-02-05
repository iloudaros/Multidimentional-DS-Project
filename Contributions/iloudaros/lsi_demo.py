#!/usr/bin/env python3

from line_segment_intersection import *


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