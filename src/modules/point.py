from math import sqrt, pow

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @staticmethod
    def distance(p1: 'Point', p2: 'Point') -> float:
        # Returns a distance between two points
        return sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2))
    
    def to_dict(self):
        # Returns point class in dict format
        return {
            "x": self.x, 
            "y": self.y
        }