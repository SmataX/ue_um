import tkinter as tk
from tkinter import Canvas
import random

from modules.path import Path
from modules.point import Point

# ----- Visualization -----
class PathVisualizer(tk.Tk):
    def __init__(self, all_points: list[Point], path: Path, width=800, height=800):
        super().__init__()
        self.title("Path Visualizer")
        self.canvas = Canvas(self, width=width, height=height, bg='white')
        self.canvas.pack()
        self.points = all_points
        self.path = path
        self.width = width
        self.height = height
        self.padding = 20
        self._draw()

    def _draw(self):
        # Normalize coordinates to fit canvas
        all_x = [p.x for p in self.points]
        all_y = [p.y for p in self.points]
        min_x, max_x = min(all_x), max(all_x)
        min_y, max_y = min(all_y), max(all_y)

        def normalize(p: Point):
            x = self.padding + (p.x - min_x) / (max_x - min_x) * (self.width - 2*self.padding)
            y = self.padding + (p.y - min_y) / (max_y - min_y) * (self.height - 2*self.padding)
            return x, y

        # Draw all points as gray circles
        for point in self.points:
            x, y = normalize(point)
            self.canvas.create_oval(x-3, y-3, x+3, y+3, fill='gray', outline='')

        # Draw path
        full_path = [self.path.start] + self.path.points + [self.path.end]
        for i in range(len(full_path)-1):
            x1, y1 = normalize(full_path[i])
            x2, y2 = normalize(full_path[i+1])
            self.canvas.create_line(x1, y1, x2, y2, fill='blue', width=2)

        # Highlight start and end
        x, y = normalize(self.path.start)
        self.canvas.create_oval(x-6, y-6, x+6, y+6, fill='green', outline='black', width=2)

        x, y = normalize(self.path.end)
        self.canvas.create_oval(x-6, y-6, x+6, y+6, fill='red', outline='black', width=2)