from point import Point
from rtree import Rtree
from box import Box
import matplotlib.pyplot as plt
import csv
import time


def visualizeRtree(tree: "Rtree"):
    # Unpack the coordinates of the box

    # Create the figure and 3D axes
    fig = plt.figure()
    ax = plt.axes(projection="3d")

    boxes = []
    for box in tree.getNodesBox(tree.root):
        boxes.append(box)

    for box in boxes:
        x1, y1, z1, x2, y2, z2 = box.getCoordinates()

        if x1 == x2 and y1 == y2 and z1 == z2:
            # Plot the point
            ax.scatter3D([x1], [y1], [z1], c="blue")
        else:
            # Plot the edges of the box
            ax.plot3D([x1, x2], [y1, y1], [z1, z1], "red")
            ax.plot3D([x1, x1], [y1, y2], [z1, z1], "red")
            ax.plot3D([x1, x1], [y1, y1], [z1, z2], "red")
            ax.plot3D([x2, x2], [y1, y2], [z1, z1], "red")

            ax.plot3D([x2, x2], [y1, y1], [z1, z2], "red")
            ax.plot3D([x1, x1], [y2, y2], [z1, z2], "red")
            ax.plot3D([x1, x2], [y2, y2], [z1, z1], "red")
            ax.plot3D([x2, x2], [y2, y2], [z1, z2], "red")

            ax.plot3D([x1, x2], [y1, y1], [z2, z2], "red")
            ax.plot3D([x1, x1], [y1, y2], [z2, z2], "red")
            ax.plot3D([x1, x1], [y2, y2], [z1, z2], "red")
            ax.plot3D([x2, x2], [y1, y2], [z2, z2], "red")
            ax.plot3D([x1, x2], [y2, y2], [z2, z2], "red")

    # Show the plot
    plt.show()


def bulkInsert(tree: "Rtree"):
    """Inserts all the trajectory data to a 3D R-tree"""

    with open("trajectory-data.csv", "r") as f:
        reader = csv.reader(f)
        # Skip first line
        next(reader)

        start = time.time()
        for row in reader:
            x = float(row[0])
            y = float(row[1])
            t = float(row[2])
            # Insert new point to the tree.
            tree.insert(Point(x=x, y=y, t=t))
        end = time.time()
        print(f"Inserted all data points in {end-start} seconds.")


tree = Rtree()
bulkInsert(tree)
visualizeRtree(tree)
