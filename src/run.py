from modules.world import World
from modules.path import Path
from modules.point import Point

from datetime import datetime

if __name__ == "__main__":
    points = [
        Point(0, 0, 0),
        Point(1, 0, 1),
        Point(2, 1, 1),
        Point(3, 1, 2)
    ]

    paths = [
        Path(0, 0, 3, [0, 1, 2, 3]),
        Path(0, 0, 3, [0, 2, 1, 3]),
        Path(0, 0, 3, [5, 2, 1, 2])
    ]

    world = World(str(datetime.now()), 123, points, paths)
    world.save_to_file()