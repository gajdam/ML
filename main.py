import random

def generate_points(num_points):
    points = []
    for i in range(num_points):
        x = random.randint(0, 5000)
        y = random.randint(0, 5000)
        points.append((x , y ))
    return points

def generate_start_end_points(points):
    start=random.randint(0,len(points)-1)
    end=random.randint(0,len(points)-1)
    while start==end:
        end=random.randint(0,len(points)-1)
    return  points[start],points[end]

def generate_random_k(points):
    return random.randint(1, len(points) - 3) # "-3", because 2 points are start and stop


generated_points = generate_points(10)
print(f"Generated points: {generated_points}")

print(generate_start_end_points(generated_points))
print(generate_random_k(generated_points))
