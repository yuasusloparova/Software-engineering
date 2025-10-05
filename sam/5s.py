import math

def heron_triangle_area(a, b, c):
    
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Треугольник с такими сторонами не существует")
    
  
    p = (a + b + c) / 2
    
  
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    
    return area
