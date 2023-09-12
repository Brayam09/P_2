"""1. Escriba una función que muestre por consola un saludo personalizado. 
Por ejemplo ‘¡Hola mundo!’
"""
def saludop():
    return "Hola querido y amado mundo"
    
print(saludop())

print()

"""
2. Escriba una función que reciba un nombre por parámetro y que luego muestre en pantalla 
¡Hola <nombre>!"""
def saludo2():
    x = input("Digite un nombre por favor: ")
    print("¡Hola " + x + "!")

saludo2()
print()


"""
3. Cree una función que le pida al usuario su nombre y su edad, 
luego muestre en pantalla los resultados

"""
def NyE():
    n = input("Escriba su nombre por favor: ")
    e = int(input("Escriba su edad por favor: "))

    print(f"Nombre: {n}, Edad: {e}")

print()
NyE()
print()

"""
4. Definir una función que reciba n cantidad de números por parámetros 
y que luego los sume, reste, mutiplique y divida."""


def operaciones(*args):
    resultadosuma = 0
    for i in args:
        resultadosuma += i
    resultadoresta = 0
    for i in args:
        resultadoresta -=i
    resultadomulti = 0
    for i in args:
        resultadomulti *= i
    resultadodiv = 0
    for i in args:
        resultadodiv /= i
    
        
    print("La suma es: ",resultadosuma )
    print("La resta es: ",resultadoresta)
    print("El resultado de la multiplicación es: ",resultadomulti)
    print("El resultado de la división es: ",resultadodiv)


operaciones(10, 20, 45, 78, 10)
    