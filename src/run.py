from modules.map import Map
from modules.path import Path
from modules.point import Point
from modules.path_finding import find_path, greedy_find_path
from modules.draw import PathVisualizer

from datetime import datetime
import random
from random import randint

xMax, yMax = 50000, 50000
points_count = 500
seed = randint(0, 999999999)
# seed = 10
random.seed(seed)

if __name__ == "__main__":
    # Generate random points
    points = [Point(randint(0, xMax), randint(0, yMax)) for _ in range(points_count)]
    map = Map(str(datetime.now()), seed, points)

    start, end = random.sample(points, 2)
    best_path = greedy_find_path(map.points, start, end, 100)
    map.paths.append(best_path)
    map.save_to_file()

    print(f"Shortest path length: {round(best_path.distance() / 100, 2)}m")
    pv = PathVisualizer(map.points, best_path)
    pv.mainloop()
    