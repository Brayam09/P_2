
class Personas:

    def __init__(self,  nombre, altura, peso, email):
        self.nombre = nombre
        self.altura = altura
        self.peso = peso
        self.email = email

    def imprimir(self):
        print(f'El nombre {self.nombre} altura {self.altura} peso {self.peso} email {self.email}')

objPersona = Personas('Brayam','172', 63, 'blosqdae@gmail.com')

objPersona.imprimir()





