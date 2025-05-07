from modules.point import Point

class Path:
    def __init__(self, start: Point, end: Point, points: list[Point]):
        self.start = start
        self.end = end
        self.points = points

    def distance(self) -> float:
        dist = 0
        for i in range(len(self.points) - 1):
            dist += Point.distance(self.points[i], self.points[i + 1])
        return dist


    def to_dict(self):
        return {
            "start": self.start.to_dict(), 
            "end": self.end.to_dict(),
            "points": [p.to_dict() for p in self.points]
        }