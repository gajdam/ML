import random
import math
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

def straight_line_with_2_points(generated_start_end_points):
    x = generated_start_end_points[0]
    y = generated_start_end_points[1]
    if x[0] == x[1]:
        raise ValueError("Division by zero is not allowed.")

    slope = (y[0] - y[1]) / (x[0] - x[1])
    y_intercept = y[0] - (slope * x[0])
    result = slope, y_intercept
    return result



def distance_bw_straight_and_point(straight_line, point):
    #y= a*x + b
    #gen_form = -straight_line[0]* x + y + -straight_line[1]
    distance= (abs(-straight_line[0]*point[0]+point[1]-straight_line[1]))/math.sqrt(pow(-straight_line,2)+1)
    return distance

#def calculate_euclidean_distance:


generated_points = generate_points(10)


print(f"Generated points: {generated_points}")

x=generate_start_end_points(generated_points)
print(straight_line_with_2_points(x))
print(x[0][0])
print(x[0][1])
print(x[0])
print(x[1])
print(x)


print(generate_random_k(generated_points))
