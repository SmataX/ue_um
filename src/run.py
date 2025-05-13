from modules.map import Map
from modules.path import Path
from modules.point import Point

from datetime import datetime
import random
from random import randint

xMax, yMax = 50000, 50000
points_count = 500
# seed = randint(0, 999999999)
seed = 10
random.seed(seed)

if __name__ == "__main__":
    # Generate random points
    points = [Point(randint(0, xMax), randint(0, yMax)) for _ in range(points_count)]
    map = Map(str(datetime.now()), seed, points)

    map.save_to_file()