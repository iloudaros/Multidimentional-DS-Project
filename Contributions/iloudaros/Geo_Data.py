from Data_structures import *

lake = Polygon((2.5, 3), (3, 4), (4, 3), (4, 2), (2.5, 3))
country1 =Polygon((1, 1), (1.8, 1.95), (3, 1), (3, 2.91), (2.1, 5), (0.8, 5), (1, 3),(1, 1))
country2 =Polygon((3, 1), (7, 1), (6.5, 3.74),(5, 4),(2.1, 5),(3, 2.91), (3, 1))

xlk, ylk = zip(*lake.points)
xc1, yc1 = zip(*country1.points)
xc2, yc2 = zip(*country2.points)