"""  
Crear los metodos setters y getters.- estos metodos son
importantes y necesarios en todas clases para que el
programador interactue con los valores de los atributos a
traves de estos metodos.-..-digamos que es la manera mas
adecuada y recomendada para solicitar un valor (get) y/o
para ingresar o cambiar un valor (set) a un atributo en
particular de la clase a traves de un objeto.

En teoria se deberia de crear un metodo Getters y
Setters por cada atributo que contenga la clase
Los metodos get siempre regresan valor es decir el
valor de la propiedad a traves del return

Por otro lado el metodo set siempre recibe parametros

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
    def setColor(self,velocidad):
        self.velocidad=velocidad

    def getPlazas(self):
        return self.plazas
    def setPlazas(self,plazas):
        self.plazas=plazas

    def getCaballaje(self):
        return self.caballaje
    def setCaballaje(self,caballaje):
        self.caballaje=caballaje


#Fin definir clase

#Crear un objetos o instanciar la clase

coche1=Coches()

#Mostrar los valores inicales del objeto o instancia de la clase
print(f"Marca: {coche1.marca} {coche1.color}, numeros de plazas: {coche1.plazas} \nModelo: {coche1.modelo} con una velocidad de {coche1.velocidad} Km/h y un potencia de {coche1.caballaje} hp")

#Acelerar la velocidad del coche de 300 a 301
coche1.acelerar()
print(f"La nueva velocidad es: {coche1.velocidad}")

#Disminuir la velocidad del coche de 301 a 100

for i in range(1,202):
   coche1.frenar()

print(f"La nueva velocidad del coche es: {coche1.velocidad}")

coche2=Coches()
coche2.marca="nissan"
coche2.caballaje=9000
coche2.color="azul rey"
coche2.modelo="1986"
coche2.velocidad=900

#Mostrar los valores inicales del objeto o instancia de la clase
print(f"Marca: {coche2.marca} {coche2.color}, numeros de plazas: {coche2.plazas} \nModelo: {coche2.modelo} con una velocidad de {coche2.velocidad} Km/h y un potencia de {coche2.caballaje} hp")

#Acelerar la velocidad del coche de 300 a 301
coche2.acelerar()
print(f"La nueva velocidad es: {coche2.velocidad}")

#Disminuir la velocidad del coche de 301 a 100

for i in range(1,202):
   coche2.frenar()

print(f"La nueva velocidad del coche es: {coche2.velocidad}")


