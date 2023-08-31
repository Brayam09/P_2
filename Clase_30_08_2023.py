
def nombre():
    return { 'Maria': 'Lopez',
            'Juan': 'Sanchez'}

for i in nombre():
    print(f"Nombre: {i} Apellido: ",nombre()[i]) 

def resta():
    a = 30
    b = 40
    c = 15
    return(b-c)

print('La resta da como resultado: ', resta)

def alumnos():
    return['Juan', "Maria", "Raul"]

for val in alumnos():
    print("Nombre: ",val)

def suma(num1,num2,num3):
    resultado = num1+num2+num3
    return resultado

print(suma(10,20,30))


def suma(*args):
    resultado = 0
    for i in args:
        resultado += i
    return resultado

x = int(input("Cuantos numeros: ")) 
y = x 

while y == x :
    print("La suma es: ", suma(int(input('Numeros: '))))


