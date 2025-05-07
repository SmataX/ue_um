from modules.point import Point

class Path:
    def __init__(self, id: int, start: int, end: int, points: list[int]):
        self.id = id
        self.start = start
        self.end = end
        self.points = points

    def to_dict(self):
        return {
            "id": self.id, 
            "start": self.start, 
            "end": self.end,
            "points": [p for p in self.points]
        }