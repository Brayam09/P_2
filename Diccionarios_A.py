
#DICCIONARIOS ANIDADOS
Colegio = {
  "Clase_1" : {
    "Estudiante_1" : "Carlos",
    "Estudiante_2" : "Juan",
    "Estudiante_3" : "Maria"
  },
  "Clase_2" : {
    "Estudiante_1" : "Camila",
    "Estudiante_2" : "Jhon",
    "Estudiante_3" : "Luisa"
  },
  "Clase_3" : {
    "Estudiante_1" : "Cesar",
    "Estudiante_2" : "Julian",
    "Estudiante_3" : "Raul"
  }
}


print(Colegio["Clase_3"]["Estudiante_3"])

"""Clase_1 = {
"Estudiante_1" : "Carlos", 
"Estudiante_2" : "Juan",
"Estudiante_3" : "Maria"
}

Clase_2 = {
"Estudiante_1" : "Camila",
"Estudiante_2" : "Jhon",
"Estudiante_3" : "Luisa"
}

Clase_3 = {
"Estudiante_1" : "Cesar",
"Estudiante_2" : "Julian",
"Estudiante_3" : "Raul"
}

Colegio = {
"Clase 1" : Clase_1,
"Clase 2" : Clase_2,
"Clase 3" : Clase_3
}


"""