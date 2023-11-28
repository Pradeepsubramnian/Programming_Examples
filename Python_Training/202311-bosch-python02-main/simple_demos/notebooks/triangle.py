
import math

class Triangle:
    pass

def validate(t):
    if not isinstance(t, Triangle):
        raise TypeError("t must be a Triangle")
    
    if t.s1>0 and t.s2>0 and t.s3>0 and \
            t.s1+t.s2>t.s3 and \
            t.s2+t.s3>t.s3 and \
            t.s1+t.s3>t.s2:
        return
    raise ValueError("Invalid Sides")

def perimeter(t):
    validate(t) # if it raises we won't reach next line
    # if we reach here that means sides are valid.
    return t.s1+t.s2+t.s3


def create(s1,s2,s3):
    t=Triangle()
    t.s1=s1
    t.s2=s2
    t.s3=s3
    return t

def area(t):
    validate(t)
    s=perimeter(t)/2
    return math.sqrt(s*(s-t.s1)*(s-t.s2)*(s-t.s3))

def draw(t):
    validate(t)
    print(f'Triangle<{t.s1},{t.s2},{t.s3}>')
