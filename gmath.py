import math
from display import *

'''
AKa     +       PKd(Nhat*Lhat)      +   PKa [ (2(L-> dot  N->) N hat - Lhat) dot  V hat ] ^ x
'''
AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    pass

def calculate_ambient(alight, areflect):
    pass

def calculate_diffuse(light, dreflect, normal):
    pass

def calculate_specular(light, sreflect, view, normal):
    pass

def limit_color(color):
    pass

#vector functions
def normalize(vector):
    denom = (vector[0]**2 + vector[1]**2 + vector[2]**2) **0.5
    return [each/denom for each in vector]

def dot_product(a, b): 
    return sum(m*n for m,n in zip(a, b))

def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N

'''
print dot_product([1,2,3],[1,5,7]) #32
print normalize([1,2,3]) #0.267...
'''
