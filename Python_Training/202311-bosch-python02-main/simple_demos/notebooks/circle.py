
import math

class Circle:
    pass

def validate(circle):
    if not isinstance(circle, Circle):
        raise TypeError(f"{type(circle)} Not a Cricle")
    if circle.radius<=0:
        raise ValueError(f'Invalid Radius: {circle.radius}')

def create(radius):
    c=Circle()
    c.radius=radius
    validate(c)
    return c

def perimeter(circle):
    validate(circle)
    return 2* math.pi*circle.radius

def area(circle):
    validate(circle)
    return math.pi*circle.radius*circle.radius

def draw(circle):
    validate(circle)
    print(f'Circle({circle.radius})')
    
