#1. Escriba un programa que almacene la cadena de caracteres contraseña en una 
# variable, para luego preguntarle al usuario por la contraseña. 
#Luego, imprima en la consola si la contraseña que el usuario ingreso coincide con 
# la guardada en variable.


print()
print('Comparador de contraseñas')
print()
print('Ingrese una contaseña y compruebe si es correcta')

C = "Abril1980"

print()
x = input('Ingrese una contraseña: ')
print()

if x == C :
    print('! Contraseña Valida ¡')

else :
    print('**Contraseña Invalida**')

print()

#2. Realice un programa que le pida al usuario dos números por teclado y muestre por 
# consola su división. Si el divisor es cero el programa debe mostrar un error y solicitar
#nuevamente el numero.

print('DIVISOR')
print()
print('Ingrese 2 números y obtenga la división')
print()
A = int(input('Ingrese un primer número: '))
B = int(input('Ingrese un segundo número: '))
print()

while B <= 0 :
    print("No se puede dividir por 0")
    print()
    B = int(input('Ingrese nuevamente el segundo número: '))
    print()
else:
    print('El resultado de la división es: ',A/B)


#3. Escriba un programa que le pida al usuario por teclado un numero entero y 
# muestre en consola si es par o impar.

print()
print('Identificador de par o impar')
print()
print('Ingresa un número y descubre si este es par o impar')

y = int(input('Por favor ingrese un número: '))

h = y % 2

print()

if h <= 0 : 
    print('El número es par')

else :
    print('El número es impar')


#4. Escriba que mediante un vector  de 5 item, lea cada item y evalué el ingreso a menores de 
# edad, si la persona tiene menos de 19 años el programa le debe mostrar 
#en pantalla que ¡No puede ingresar!, de caso contrario que le diga ¡Bienvenido!
print()
print('Accceso')
print()
edades = [21,23,18,17,20]


for i in edades:

    if i < 19:
        print('¡No puede ingresar!')
        print()

    else:
        print('¡Bienvenido!')
        print()






