#!/usr/bin/env python3

lake = ((2.5, 3), (3, 4), (4, 3), (4, 2), (2.5, 3))
country1 =((1, 1), (1.8, 1.95), (3, 1), (3, 2.91), (2.1, 5), (0.8, 5), (1, 3),(1, 1))
country2 =((3, 1), (7, 1), (6.5, 3.74),(5, 4),(2.1, 5),(3, 2.91), (3, 1))

xlk, ylk = zip(*lake)
xc1, yc1 = zip(*country1)
xc2, yc2 = zip(*country2)

#plt.figure()
#plt.plot(xlk,ylk)
#plt.plot(xc1,yc1)
#plt.plot(xc2,yc2)
#plt.show()