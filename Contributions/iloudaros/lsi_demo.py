from line_segment_intersection import *
import  tkinter
from tkinter import messagebox




intersection_points_1 = pol_interesect_naive(lake.points, country1.points)
intersection_points_2 = pol_interesect_naive(lake.points, country2.points)

if intersection_points_1 == intersection_points_2 : 
    print("The lake is a natural border, intersecting the two countries at coordinatess", intersection_points_2)
    tkinter.messagebox.showinfo("There is an intersection point!",  ("The lake is a natural border, intersecting the two countries at coordinatess: \n Point 1: %s \nPoint 2: %s " %(intersection_points_2[0],intersection_points_2[1])) )

plt.figure()
plt.plot(xlk,ylk)
plt.plot(xc1,yc1)
plt.plot(xc2,yc2)
for x in intersection_points_1:
    plt.plot(*x, 'ok', markersize=10)
plt.show()