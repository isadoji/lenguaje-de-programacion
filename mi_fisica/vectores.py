"""Módulo con la clase Vector y funciones auxiliares."""
import math

class Vector:
    """Vector 2D/3D con operaciones básicas."""
    def __init__(self, x, y, z=0):
        self.x, self.y, self.z = x, y, z
    def __add__(self, o): return Vector(self.x+o.x, self.y+o.y, self.z+o.z)
    def __abs__(self):    return math.sqrt(self.x**2+self.y**2+self.z**2)
    def __str__(self):    return f"({self.x}, {self.y}, {self.z})"

def angulo_entre(v1, v2):
    """Ángulo en grados entre dos vectores."""
    cos_a = (v1.x*v2.x+v1.y*v2.y+v1.z*v2.z) / (abs(v1)*abs(v2))
    return math.degrees(math.acos(max(-1, min(1, cos_a))))
