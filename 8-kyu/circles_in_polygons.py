import math

def circle_diameter(sides, side_length): 
    return 2 * (side_length / (2 * math.tan(math.pi / sides)))