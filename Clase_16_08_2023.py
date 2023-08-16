#LISTAS


varlista = ['Hector',True,5.5,9]
"""
print(varlista[0])
print(varlista[1])
print(varlista[2])
print(varlista[3])

for z in varlista:
    print(z)

w = len(varlista)

print(w)

q = 0

while q < w :
    print(varlista[q])
    q +=1

q = 0

while q < len(varlista):
    print(varlista[q])
    q +=1

"""
"""
#Eliminar elementos

del varlista[0]

q = 0

while q < len(varlista):
    print(varlista[q])
    q +=1
"""
"""
eliminar = input("Ingrese elemento a elminar: ")
contador = 0

for z in varlista:
    if eliminar == z :
        del varlista[contador]

    else :
        contador +=1
    
print(varlista)


#Agregar elementos

print()

varlista.insert(2,"Clase")


for z in varlista:
    print(z)

print()

varlista.append("6")


for z in varlista:
    print(z)


print()

varlista.append(input("Ingrese un nombre: "))


for z in varlista:
    print(z)
"""



