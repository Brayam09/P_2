
#edad = int(input("Ingrese una edad: "))

#if(edad >= 18):
  #  print("Es mayor de edad")

#else:
 #   print("Es menor de edad")

#----------------------------------

#edad = int(input("Ingrese una edad: "))

#if edad <18 and edad >0 :
   # print("Niños")

#elif edad >= 18 and edad <= 35 :
   # print ("Pos-adolescente")

#elif edad >= 35 and edad <= 60 :
  #  print("Adultos")

#else:
   # print("Adultos mayores")

#----------------------------------------

print("----- CALCULADORA ------")

print()
print()


print("Por favor seleccione la operación a realizar y posteriormente ingrese los 2 numeros a operar.")

print()
print("Para Suma escribir + ")
print("Para Resta escribir - ")
print("Para Multiplicación escribir * ")
print("Para división escribir / ")
print()
o = input("Selecione una operación a realizar:  ")
print()
x = int(input("Ingrese un primer número: "))
y = int(input("Ingrese un segundo número: "))
print()

if o == "+":
    print("El resultado de la suma es: ", x + y)
  
elif o == "-":
    print("El resultado de la resta es: ", x - y)

elif o == "*":
    print("El resultado de la multiplicación es: ", x * y)

elif o == "/" and y <= 0:
    print("No se puede dividir por 0")

elif o == "/":
    print("El resultado de la división es: ", x / y)

else:
    print("No seleccionó nada")


