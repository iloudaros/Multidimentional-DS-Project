"""
This file contains the declaration of the Point class.
A point hold the x,y,t values of a trajectory for a specific t.
"""
from .box import Box


class Point:
    def __init__(self, x: float, y: float, t: float) -> "Point":
        self.x = x
        self.y = y
        self.t = t
        self.mbb = Box(x, y, t, x, y, t)

    def __str__(self) -> str:
        return f"x:{self.x} y:{self.y} t:{self.t}"
