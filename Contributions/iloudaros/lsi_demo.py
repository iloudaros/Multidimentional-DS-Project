from line_segment_intersection import *



intersection_points_1 = pol_interesect_naive(lake, country1)
intersection_points_2 = pol_interesect_naive(lake,country2)
if intersection_points_1 == intersection_points_2 : print("The lake is a natural border, intersecting the two countries at coordinatess", intersection_points_2)


plt.figure()
plt.plot(xlk,ylk)
plt.plot(xc1,yc1)
plt.plot(xc2,yc2)
for x in intersection_points_1:
    plt.plot(*x, 'ok', markersize=10)
plt.show()