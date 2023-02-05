import random
import matplotlib.pyplot as plt
from collections import namedtuple
from functools import cmp_to_key

Point = namedtuple("Point", ["x", "y"])

def cross_product(p1, p2, p3):
    """Calculates the cross product of the vectors p1p2 and p1p3.

    Returns a positive value if p3 is to the left of p1p2,
    a negative value if p3 is to the right of p1p2, and 0 if p1, p2, and p3 are collinear.
    """
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)

def convex_hull(points):
    """Calculates the convex hull of a set of points.

    Returns a list of points in the convex hull, in counter-clockwise order.
    """
    # Sort the points (first by x-coordinate, then by y-coordinate)
    points = sorted(points)

    # Build the lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build the upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Join the lower and upper hulls, and add the first point of the hull to the end
    hull = lower[:-1] + upper[:-1]
    hull.append(hull[0])

    return hull

def visualize(points, hull):
    """Visualizes the points and the convex hull using matplotlib."""
    # Extract the x- and y-coordinates of the points and the hull
    xs = [p.x for p in points]
    ys = [p.y for p in points]
    hx = [p.x for p in hull]
    hy = [p.y for p in hull]

    # Plot the points and the hull
    plt.plot(xs, ys, "bo")  
    plt.plot(hx, hy, "r-")  
    plt.show()

# Test 
num_points = 20
points = [Point(x=random.uniform(0, 10), y=random.uniform(0, 10)) for _ in range(num_points)]
hull = convex_hull(points)
visualize(points, hull)
