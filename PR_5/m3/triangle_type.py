import random

def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
def triangle_type(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2) + random.uniform(-0.1, 0.1)
    b = distance(x2, y2, x3, y3) + random.uniform(-0.1, 0.1)
    c = distance(x3, y3, x1, y1) + random.uniform(-0.1, 0.1)
    if abs(a - b) < 1e-6 and abs(a - c) < 1e-6:
        return "равносторонний"
    elif abs(a - b) < 1e-6 or abs(a - c) < 1e-6 or abs(b - c) < 1e-6:
        return "равнобедренный"
    else:
        return "разносторонний"