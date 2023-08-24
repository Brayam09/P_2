#1. Escriba un programa que almacene (Input) en una 
#Lista las materias que has cursado con sus respectivas notas
# Luego muestre la lista por consola mediante un ciclo.

print("MATERIAS VISTAS")
print()
print()

Materias = []

a = input("Por favor ingrese una materia y seguido a este su respectiva nota: ")
print()

Materias.append(a)

m = input("Escriba '+' para añadir mas materias o enter para ver la lista de materias: ")
print()

while m == "+":
    a = input("Por favor ingrese una materia: ")
    print()
    Materias.append(a)
    m = input("Escriba '+' para añadir mas materias o enter para ver la lista de materias: ")
    print()
   
else :
    print()
    print("Las materias vistas son: ")
    print()
    for x in Materias:
        print(x)


#2. Escriba un programa que almacene personas (input), luego que le muestre 
# por pantalla el mensaje de ‘Su nombre es ‘nombre’
print()
print("Lista de Nombres")
print()

Persona = []
p = input("Por favor ingrese un Nombre: ")
print()
Persona.append(p)

y = input("Si desea añadir mas escriba yes, de lo contrario presione enter: ")
print()

while y == "yes":
    p = input("Por favor ingrese un Nombre: ")
    print()
    Persona.append(p)
    y = input("Si desea añadir mas escriba yes, de lo contrario presione enter: ")
    print()

else :
    for x in Persona:
        print("Su nombre es: ",x)
        print()

#3. Escribir un programa que guarde en una variable un diccionario con los
#siguientes valores {'Euro':'€', 'Dollar':'$', 'Yen':'¥'} 
#Luego pregunte al usuario por una divisa y el valor en pesos a convertir. Luego muestre en consola el 
#símbolo con el valor que corresponde a la divisa o un mensaje de advertencia si esa divisa no se 
#encuentra en el diccionario.
print()
print("CONVERSOR DE DIVISAS")
print()

Divisas= {
    'Euro':'€',
    'Dollar':'$',
    'Yen':'¥'
    } 


print()
print(Divisas.items())

d = float(input("Ingrese el valor en pesos a convertir: "))

s = input("Seleccione una divisa")

Euro = float(4500),
Dolar = float(3500),
Yen = float(3000)

if s == "Euro":
    print("El valor en Euros es: ",d*Euro,"€")
    print()

elif s == "Dolar":
    print("El valor en Dolar es: ",d*Euro,"$")
    print()

elif s == "Yen":
    print("El valor en Yenes es: ",d*Euro,"¥")
    print()

else :
    print("No se encuentra la divisa")


#4. En una tupla coloque o ingrese (input) los siguientes valores: números enteros, 
#decimales, String, colecciones. Luego muestre en consola que tipo de datos o variable 
#son los valores digitados.

tupla = ()

t = list(tupla)
x = input("Ingrese los elementos de la tupla")
t.append(x)
tupla = tuple(t)


for x in tupla:
    z = type(x)
    print(z)




