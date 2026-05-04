 
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    
    def saludar_v2(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    
    def despedirse_v2(self):
        return f"Adiós, me llamo {self.nombre} y tengo {self.edad} años."

'''
def saludar_v2(nombre):
    return f"Hola, mi nombre es {nombre}."
    
def despedirse_v2(nombre,edad=0):
        return f"Adiós, me llamo {nombre} y tengo {edad} años."

'''
