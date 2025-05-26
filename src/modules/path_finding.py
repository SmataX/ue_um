from math import sqrt
import random

from modules.common.path import Path
from modules.common.point import Point
from modules.custers import get_all_points_in_clusters

class PathFinding:
    def __init__(self, points: list[Point], start: Point, end: Point):
        self.points = points
        self.start = start
        self.end = end

    def greedy_path(self) -> Path:
        # Your existing greedy implementation
        candidates = [p for p in self.points if p != self.start and p != self.end]

        unvisited = set(candidates)
        path_points = [self.start]
        current = self.start

        alpha = 0.7  # Bias toward end (0 = local, 1 = direct to end)

        while unvisited:
            if all(Point.distance(current, p) > Point.distance(current, self.end) for p in unvisited):
                break

            def score(p):
                d_curr = Point.distance(current, p)
                d_end = Point.distance(p, self.end)
                return (1 - alpha) * d_curr + alpha * d_end

            next_point = min(unvisited, key=score)
            path_points.append(next_point)
            unvisited.remove(next_point)
            current = next_point

        path_points.append(self.end)
        return Path(self.start, self.end, path_points)

    def aco_path(
            self,
            k_points: int,                # number of intermediate points to visit exactly
            num_ants: int = 20,
            num_iterations: int = 100,
            alpha: float = 1.0,
            beta: float = 5.0,
            evaporation_rate: float = 0.5,
            pheromone_deposit: float = 100.0,
        ) -> Path:
            candidates = [p for p in self.points if p != self.start and p != self.end]

            if len(candidates) < k_points:
                raise ValueError(f"Not enough intermediate points ({len(candidates)}) for k={k_points}")

            # Initial greedy path to get starting solution (may not have exactly k points)
            greedy_solution = self.greedy_path()
            greedy_points = greedy_solution.points  # Assuming Path stores points in order

            # Initialize pheromones on all edges
            all_points = [self.start] + candidates + [self.end]
            pheromones = {(a, b): 1.0 for a in all_points for b in all_points if a != b}

            # Boost pheromones on greedy path edges (only first k intermediate points if needed)
            for i in range(min(len(greedy_points) - 1, k_points + 1)):  # +1 because edges between points
                a, b = greedy_points[i], greedy_points[i + 1]
                pheromones[(a, b)] += pheromone_deposit
                pheromones[(b, a)] += pheromone_deposit

            best_path = None
            best_length = float('inf')

            for iteration in range(num_iterations):
                all_paths = []

                for ant in range(num_ants):
                    path = [self.start]
                    current = self.start
                    unvisited = set(candidates)

                    # Select exactly k intermediate points
                    for _ in range(k_points):
                        probabilities = []
                        total_prob = 0.0

                        for point in unvisited:
                            tau = pheromones[(current, point)]
                            dist = Point.distance(current, point)
                            eta = 1.0 / (dist + 1e-6)
                            prob = (tau ** alpha) * (eta ** beta)
                            probabilities.append((point, prob))
                            total_prob += prob

                        if total_prob == 0.0:
                            # No available points with pheromone/distance, pick random
                            next_point = random.choice(list(unvisited))
                        else:
                            r = random.random()
                            cumulative = 0.0
                            for point, prob in probabilities:
                                cumulative += prob / total_prob
                                if r <= cumulative:
                                    next_point = point
                                    break

                        path.append(next_point)
                        unvisited.remove(next_point)
                        current = next_point

                    # Finally add the end point
                    path.append(self.end)

                    # Calculate path length
                    length = sum(Point.distance(path[i], path[i + 1]) for i in range(len(path) - 1))
                    all_paths.append((path, length))

                    if length < best_length:
                        best_length = length
                        best_path = path

                # Evaporate pheromones
                for key in pheromones:
                    pheromones[key] *= (1 - evaporation_rate)

                # Deposit pheromones based on all paths
                for path, length in all_paths:
                    deposit = pheromone_deposit / (length + 1e-6)
                    for i in range(len(path) - 1):
                        a, b = path[i], path[i + 1]
                        pheromones[(a, b)] += deposit
                        pheromones[(b, a)] += deposit  # undirected graph

            return Path(self.start, self.end, best_path)