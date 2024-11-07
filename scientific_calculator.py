import math
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def divide(x,y):
    return x/y

def multiply(x,y):
    return x*y

def sin(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a numeric value.")
    return math.sin(math.radians(x))

def cos(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a numeric value.")
    return math.cos(math.radians(x))

def tan(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a numeric value.")
    return math.tan(math.radians(x))

def sqrt(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a numeric value.")
    if x < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(x)

def log(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a numeric value.")
    if x <= 0:
        raise ValueError("Cannot calculate the logarithm of zero or a negative number.")
    return math.log(x)

def exp(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a numeric value.")
    return math.exp(x)



       
            


