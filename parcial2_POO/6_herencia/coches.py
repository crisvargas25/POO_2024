"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.

MÈTODO COSNTRUCTOR.- Este metodo especial se coloca dentro de la clase y s eutiliza para dar un valora los atributosdel objeto al momento de crear 
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

class Coches:

  #Atributos o propiedades (variables)
  #Caracteristicas del coche
  #valores iniciales es posible declarar al principio de una clase
  def __init__(self,color,marca,modelo,velocidad,caballaje,plazas):
    self.color=color
    self.marca=marca
    self.modelo=modelo
    self.velocidad=velocidad
    self.caballaje=caballaje
    self.plazas=plazas

###en python el ecapsulamiento tmbn se llama visibilidad y por lo general define como seran los atributos y metodos es decir publicos o privados


##atributopublico
  publico_atributo="soy un att publico"

##atributoprivado
  __privado_atributo="soy un att privado"

# nota,para utilizar un atributo privado se tendria que hacer dentro d eun metodo que fuera publico

  def getPrivAtt(self):
      return self.__privado_atributo

#metodo privado
  def __getMetodoPrivado(self):
    print("soy un metodo privado")


  #Metodos o acciones o funciones que hace el objeto 

  def acelerar(self):
      self.velocidad+=1

  def frenar(self):
      self.velocidad-=1


    #Crear los metodos setters y getters .- estos metodos son importantes y necesarios en todos clases para que el programador interactue con los valores de los atributos a traves de estos metodos ... digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto. 
    # En teoria se deberia de crear un metodo Getters y Setters por cada atributo que contenga la clase
    #   Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return
    #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

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

  def getCaballaje(self):
    return self.caballaje

  def setCaballaje(self,caballaje):
    self.caballaje=caballaje  

  def getPlazas(self):
    return self.plazas

  def setPlazas(self,plazas):
    self.plazas=plazas

  def getInfo(self):
      print(f"Marca: {self.getMarca()} {self.getColor()}, numeros de plazas: {self.getPlazas()} \nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h y un potencia de {self.getCaballaje()} hp")     


class Camiones(Coches):
  def __init__(self, color, marca, velocidad, caballaje, plazas,  eje, capacidadCarga):
    super().__init__(color, marca, velocidad, caballaje, plazas, eje, capacidadCarga)
    self.__eje=eje
    self.__capacidadCarga=capacidadCarga
    __tipo_carga=""
    def cargar(self,tipo_carga):
      self.tipo_carga=tipo_carga
      return self.tipo_carga
    
    def getEje(self):
      return self.__eje
    def setEje(self):
      self.__eje=eje
  
    def getCapacidadCarga(self):
      return self.__capacidadCarga
    def setCapacidadCarga(self):
      self.__capacidadCarga=capacidadCarga

    def getInfo(self):
      print(f"Marca: {self.getMarca()} {self.getColor()}, numeros de plazas: {self.getPlazas()} \nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h y un potencia de {self.getCaballaje()} hp , con {self.getEje()} ejes y una capacidad de carga de {self.getCapacidadCarga}")     


class Camionetas(Coches):
  def __init__(self, color, marca, velocidad, caballaje, plazas,  traccion, cerrada):
    super().__init__(color, marca, velocidad, caballaje, plazas, traccion, cerrada)
    self.traccion=traccion
    self.cerrada=cerrada
    __num_pasajeros=""
    def transportar(self,num_pasajeros):
      self.num_pasajeros=num_pasajeros
      return self.num_pasajeros
    
    def getTraccion(self):
      return self.traccion
    def setTraccion(self):
      self.traccion=traccion
  
    def getCerrada(self):
      return self.cerrada
    def setCerrada(self):
      self.cerrada=cerrada

    def getInfo(self):
      print(f"Marca: {self.getMarca()} {self.getColor()}, numeros de plazas: {self.getPlazas()} \nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h y un potencia de {self.getCaballaje()} hp , con una traccion {self.getTraccion()} y es  {self.getCerrada}")     

#Fin definir clase

