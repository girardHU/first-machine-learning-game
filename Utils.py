import math

def vector_length(x, y):
    return math.sqrt(x*x + y*y)

def normalize_vector(x, y):
    norm = vector_length(x, y)
    return x/norm, y/norm