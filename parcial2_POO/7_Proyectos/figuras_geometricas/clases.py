class Figura:
    def __init__(self, x, y, visible):
        self.x = x
        self.y = y
        self.visible = visible

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_visible(self):
        return self.visible

    def set_visible(self, visible):
        self.visible = visible

    def esta_visible(self):
        return self.visible

    def mostrar(self):
        pass

    def ocultar(self):
        pass

    def mover(self):
        pass

    def calcular_area(self):
        pass


class Rectangulo(Figura):
    def __init__(self, x, y, visible, largo, ancho):
        super().__init__(x, y, visible)
        self.__largo = largo
        self.__ancho = ancho

    def get_largo(self):
        return self.__largo

    def set_largo(self, value):
        self.__largo = value

    def get_ancho(self):
        return self.__ancho

    def set_ancho(self, value):
        self.__ancho = value

    def ocultar(self):
        if self.visible:
            print("Las características del objeto no están ocultas, se están mostrando")
        else:
            print("Las características están ocultas debido a que no es visible")

    def mostrar(self):
        print(f"El rectángulo tiene un ancho de {self.__ancho} y un largo de {self.__largo}, cuenta con un área de {self.calcular_area()}, la figura esta en las coordenadas({self.x},{self.y})")

    def calcular_area(self):
        return self.__largo * self.__ancho


class Circulo(Figura):
    def __init__(self, x, y, visible, radio):
        super().__init__(x, y, visible,)
        self.__radio = radio

    def get_radio(self):
        return self.__radio

    def set_radio(self, radio):
        self.__radio = radio

    def ocultar(self):
        if self.visible:
            print("Las características del objeto no están ocultas, se están mostrando")
        else:
            print("Las características están ocultas debido a que no es visible")

    def mostrar(self):
        print(f"El círculo tiene un radio de {self.__radio} y cuenta con un área de {self.calcular_area()}, la figura esta en las coordenadas({self.x},{self.y})")

    def calcular_area(self):
        import math
        return math.pi * self.__radio ** 2