import json

from modules.point import Point
from modules.path import Path

class Map:
    def __init__(self, name: str, seed: int, points: list[Point], paths: list[Path]):
        self.name = name
        self.seed = seed
        self.points = points
        self.paths = paths

    def to_dict(self):
        return {
            "map": self.name,
            "seed": self.seed,
            "points": [p.to_dict() for p in self.points],
            "paths": [p.to_dict() for p in self.paths],
        }
    
    def save_to_file(self):
        with open(f"data/{self.name}.json", "w") as f:
            json.dump(self.to_dict(), f, indent=2) 