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

def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    a = calculate_ambient(ambient, areflect)
    d = calculate_diffuse(light, dreflect, normal)
    s = calculate_specular(light, sreflect, view, normal)
    return limit_color([x+y+z for x,y,z in zip(a,d,s)])

def calculate_ambient(alight, areflect):
    return limit_color([int(a*b) for a,b in zip(alight,areflect)])

def calculate_diffuse(light, dreflect, normal):
    color = [int(a*b) for a,b in zip(light[1],dreflect)]
    normlight = normalize(light[0])
    norm = normalize(normal)
    dot = dot_product(norm, normlight)
    return limit_color([int(x*dot) for x in color])


def calculate_specular(light, sreflect, view, normal):
    color = [int(a*b) for a,b in zip(light[1],sreflect)]
    normlight = normalize(light[0])
    normview = normalize(view)
    norm = normalize(normal)
    if dot_product(norm, normlight) <= 0:
        return [0,0,0]
    fir = [x*2*dot_product(norm, normlight) for x in norm]
    sec = [x-y for x,y in zip(fir,normlight)]
    last = [int(x*(dot_product(sec,normview)**16)) for x in color]
    return limit_color(last)


def limit_color(color):
    ret =  [x if x <= 255 else 255 for x in color]
    return [x if x >= 0 else 0 for x in ret]


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
