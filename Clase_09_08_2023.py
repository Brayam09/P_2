
edad = int(input("Ingrese una edad: "))

if(edad >= 18):
    print("Es mayor de edad")

else:
    print("Es menor de edad")

#----------------------------------

edad = int(input("Ingrese una edad: "))

if edad <18 and edad >0 :
    print("Niños")

elif edad >= 18 and edad <= 35 :
    print ("Pos-adolescente")

elif edad >= 35 and edad <= 60 :
    print("Adultos")

else:
    print("Adultos mayores")