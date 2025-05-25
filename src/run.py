from modules.map import Map
from modules.path import Path
from modules.point import Point
from modules.path_finding import find_path, greedy_find_path
from modules.draw import PathVisualizer

from datetime import datetime
import random
from random import randint

if __name__ == "__main__":
    map = Map.load_from_file("data/data.txt", 100)

    start, end = random.sample(map.points, 2)
    best_path = greedy_find_path(map.points, start, end, 100)

    print(f"Shortest path length: {round(best_path.distance() / 100, 2)}m")
    pv = PathVisualizer(map.points, best_path)
    pv.mainloop()
    