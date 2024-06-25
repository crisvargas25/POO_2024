"""

"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    marca="Ferrari"
    color="rojo"
    modelo="2010"
    velocidad=300
    caballaje=500
    plazas=2

    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
        self.velocidad+=1
    def frenar(self):
        self.velocidad-=1   

    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color=color
    
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca

    def getModelo(self):
        return self.modelo
    def setModelo(self,modelo):
        self.modelo=modelo

    def getVelocidad(self):
        return self.velocidad
    def setVelocidad(self,velocidad):
        self.velocidad=velocidad

    def getPlazas(self):
        return self.plazas
    def setPlazas(self,plazas):
        self.plazas=plazas

    def getCaballaje(self):
        return self.caballaje
    def setCaballaje(self,caballaje):
        self.caballaje=caballaje

coche1=Coches()
coche1.setColor("Amarillo")
coche1.setModelo("2020")
coche1.setMarca("Porsche")
coche1.setVelocidad(250)
coche1.setCaballaje(450)
coche1.setPlazas(2)



# Para crear multiples objetos es necesario hacer varias instancias de la clase

print('objeto 3')
coche3=Coches()
coche3.setColor('amarillo')
coche3.setCaballaje(220)
coche3.setMarca('Mitsubishi')
coche3.setModelo('Lancer')
coche3.setPlazas('5')
coche3.setVelocidad('amarillo')

def get_info(coche):

    print(f"Color del coche: {coche.color}\nCaballaje del carro:{coche.caballaje} \nMarca del carro: {coche.marca} \nModelo del carro: {coche.modelo} \nPlazas disponibles: {coche.plazas} \nVelocidad: {coche.velocidad}")

get_info(coche1)
