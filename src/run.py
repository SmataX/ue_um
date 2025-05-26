from modules.common.map import Map
from modules.common.path import Path
from modules.common.point import Point
from modules.custers import run, get_clusters_from_ids, get_all_points_in_clusters
from modules.visualizer import visualize
from modules.path_finding import greedy_path

if __name__ == "__main__":
    map = Map.load_from_file("data/data.txt", 100)
    start = map.points[0]
    end = map.points[100]

    map_size = 10000
    cluster_size = 500

    clusters, selected_clusters = run(map.points, start, end, cluster_size=cluster_size, map_size=map_size)

    points = get_all_points_in_clusters(
        get_clusters_from_ids(clusters, selected_clusters)
    )
    # path = greedy_path(start, end, points, 158, alpha=0.7)
    # print(f"Path length: {path.distance()}")
    path = None

    visualize(points, clusters, selected_clusters, cluster_size=cluster_size, map_size=map_size, path=path)
    