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



def sweep_line_intersect(polygon1, polygon2):

  # Get lines from polygons
  lines1 = polygon1.lines()
  lines2 = polygon2.lines()

  # Create events from all line endpoints
  events = []
  for line in lines1 + lines2:
    events.append(Event(line.start[0], line.start[1], True, [line]))
    events.append(Event(line.end[0], line.end[1], False, [line]))

  # Sort events by x coordinate
  events.sort()

  # Active line segments
  active_lines = []

  # Intersection points
  intersections = []

  # Sweep line algorithm
  for event in events:

    if event.is_left_endpoint():
      # Insert segment in active lines
      active_lines.append(event.line)

    else:
      # Remove segment from active lines
      active_lines.remove(event.line)

    # Check intersections between active segments
    for l1 in active_lines:
      for l2 in active_lines:
        if l1 is not l2:
          temp = intersect(l1, l2)
          if temp:
            intersections.append(intersect)

  return intersections





