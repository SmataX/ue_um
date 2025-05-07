from modules.world import World
from modules.path import Path
from modules.point import Point

from datetime import datetime

if __name__ == "__main__":
    points = [
        Point(0, 0),
        Point(0, 1),
        Point(1, 1),
        Point(1, 2)
    ]

    paths = [
        Path(Point(0, 0), Point(1, 2), [Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 2)]),
        Path(Point(0, 0), Point(1, 2), [Point(0, 0), Point(1, 1), Point(0, 1), Point(1, 2)]),
    ]

    world = World(str(datetime.now()), 123, points, paths)
    world.save_to_file()