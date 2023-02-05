"""
This file contains the implementation of the Box class.
2D R-trees use rectangles but in the case of an 3D R-tree boxes are used.
"""
from math import fabs


class Box:
    def __init__(
        self,
        x1: float,
        y1: float,
        z1: float,
        x2: float,
        y2: float,
        z2: float,
    ) -> "Box":
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2

    def __str__(self) -> str:
        return f"x:({self.x1, self.x2} x:({self.y1, self.y2} z:({self.z1, self.z2}"

    def getVolume(self) -> float:
        return fabs((self.x2 - self.x1) * (self.y2 - self.y1) * (self.z2 - self.z1))

    def getCoordinates(self):
        return self.x1, self.y1, self.z1, self.x2, self.y2, self.z2

    def overlaps(self, box: "Box") -> bool:
        a, b = self, box
        x1 = max(min(a.x1, a.x2), min(b.x1, b.x2))
        y1 = max(min(a.y1, a.y2), min(b.y1, b.y2))
        x2 = min(max(a.x1, a.x2), max(b.x1, b.x2))
        y2 = min(max(a.y1, a.y2), max(b.y1, b.y2))
        z1 = max(min(a.z1, a.z2), min(b.z1, b.z2))
        z2 = min(max(a.z1, a.z2), max(b.z1, b.z2))
        return x1 <= x2 and y1 <= y2 and z1 <= z2
