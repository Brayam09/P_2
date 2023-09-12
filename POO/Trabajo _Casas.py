import random

class Estudiante:
    def __init__(self, nombre, apellido, edad, email, casa):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email
        self.casa = casa

    def asignar_casa(self):
        self.casa = random.choice(['Slytherin', 'Gryffindor'])

def nuevo_estudiantes():
    Slytherin = []
    Gryffindor = []
    cantidad = int(input("Ingrese la cantidad de estudiantes: "))

    for i in range(cantidad):
        nombre = input(f"Nombre del estudiante {i + 1}: ")
        apellido = input(f"Apellido del estudiante {i + 1}: ")
        edad = int(input(f"Edad del estudiante {i + 1}: "))
        email = input(f"Email del estudiante {i + 1}: ")

        estudiante = Estudiante(nombre, apellido, edad, email, None)
        estudiante.asignar_casa()

        if estudiante.casa == 'Slytherin':
            Slytherin.append(estudiante)
        elif estudiante.casa == 'Gryffindor':
            Gryffindor.append(estudiante)

    return Slytherin, Gryffindor

# Ejemplo de uso
slytherin_estudiantes, gryffindor_estudiantes = nuevo_estudiantes()

# Imprimir estudiantes y sus casas
print("Estudiantes de Slytherin:")
for estudiante in slytherin_estudiantes:
    print(f"Nombre: {estudiante.nombre}, Apellido: {estudiante.apellido}, Edad: {estudiante.edad}, Email: {estudiante.email}, Casa: {estudiante.casa}")

print("\nEstudiantes de Gryffindor:")
for estudiante in gryffindor_estudiantes:
    print(f"Nombre: {estudiante.nombre}, Apellido: {estudiante.apellido}, Edad: {estudiante.edad}, Email: {estudiante.email}, Casa: {estudiante.casa}")
