import random
from itertools import permutations
from modules.point import Point
from modules.path import Path

def find_path(points: list[Point], start: Point, end: Point, k: int):
    remaining_points = [p for p in points if p != start and p != end]
    waypoints = random.sample(remaining_points, k)

    min_distance = float('inf')
    best_path = []

    for perm in permutations(waypoints):
        full_path = [start] + list(perm) + [end]
        dist = sum(Point.distance(full_path[i], full_path[i+1]) for i in range(len(full_path)-1))
        if dist < min_distance:
            min_distance = dist
            best_path = full_path

    return Path(start, end, best_path)


def greedy_find_path(points: list[Point], start: Point, end: Point, k: int):
    if k < 2:
        raise ValueError("k must be at least 2 to include start and end")

    available = [p for p in points if p != start and p != end]

    if len(available) < k - 2:
        raise ValueError(f"Not enough intermediate points to build path of length {k}")

    path = [start]
    used = set()

    current = start

    for _ in range(k - 2):
        next_point = min(
            (p for p in available if p not in used),
            key=lambda p: Point.distance(current, p)
        )
        path.append(next_point)
        used.add(next_point)
        current = next_point

    path.append(end)
    return Path(start, end, path)


