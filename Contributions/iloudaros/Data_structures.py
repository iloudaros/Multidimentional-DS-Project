class Line:
    def __init__(self, start, end, id=None):
        self.start = start
        self.end = end
        self.id = id

    def __lt__(self, other):
        if self.start[1] == other.start[1]:
            return self.start[0] < other.start[0]
        return self.start[1] < other.start[1]

    def __str__(self):
        return "Line {} from {} to {}".format(self.id, self.start, self.end)

    def slope(self):
        return (self.end[1] - self.start[1]) / (self.end[0] - self.start[0])


def slope(p1, p2):
    return (p2[1] - p1[1]) / (p2[0] - p1[0])



class Event:
    def __init__(self, x, y, lines):
        self.x = x
        self.y = y
        self.lines = lines

    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        return self.y < other.y


class Polygon:

    points = [(float,float)]

    def __init__(self, *points):
        self.points = points

    def lines(self):
        lines=[Line]

        for i in range(len(self.points)-1):
            lines.append(Line(self.points[i], self.points[i+1]))
        return lines


    