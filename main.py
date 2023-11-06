import random
import heapq

def generate_points(num_points):
    points = []
    for i in range(num_points):
        x = random.randint(0, 5000)
        y = random.randint(0, 5000)
        points.append((x / 100, y / 100))
    return points

def generate_start_end_points(points, k):
    start_end_points = []
    selected_points = random.sample(range(len(points)), k + 2)
    start = selected_points[0]
    end = selected_points[-1]
    while end == start:
        end = random.choice(selected_points)
    start_end_points.append((points[start], points[end]))
    return start_end_points

def generate_random_k(max_value):
    return random.randint(0, max_value - 1)

def calculate_euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def dijkstra(graph, start, end):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    predecessors = {}
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_vertex == end:
            path = []
            while current_vertex in predecessors:
                path.insert(0, current_vertex)
                current_vertex = predecessors[current_vertex]
            path.insert(0, start)
            return path

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return None

# Generate points
generated_points = generate_points(20)

# Set the desired k value here
k_value = 5

# Generate start and end points
generated_start_end = generate_start_end_points(generated_points, k_value)

# Generate random k
generated_k = generate_random_k(5)

# Create the graph
graph = {}
for i in range(len(generated_points)):
    graph[i] = {}

for i in range(len(generated_points)):
    for j in range(i + 1, len(generated_points)):
        distance = calculate_euclidean_distance(generated_points[i], generated_points[j])
        graph[i][j] = distance
        graph[j][i] = distance

start_point, end_point = generated_start_end[0]

# Find the shortest path through k random points between the start and end
shortest_path = dijkstra(graph, generated_points.index(start_point), generated_points.index(end_point))

if shortest_path:
    print(f"Generated points: {generated_points}")
    print(f"Start and End points: {generated_start_end}")
    print(f"Generated k: {generated_k}")
    print(f"Shortest path from start to end: {shortest_path}")

    # Print the points traversed in the shortest path
    points_traversed = [generated_points[i] for i in shortest_path]
    print(f"Points traversed in the shortest path: {points_traversed}")

    total_distance = sum(graph[shortest_path[i]][shortest_path[i + 1]] for i in range(len(shortest_path) - 1))
    print(f"Total distance: {total_distance}")
else:
    print("No path found.")
