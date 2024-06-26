from clases import *

def main():
    rectangulo = Rectangulo(5.0, 3.0)
    circulo = Circulo(4.0)
    triangulo = Triangulo(6.0,4.0)

    print(f"Área del rectángulo: {rectangulo.calcular_area()}")
    print(f"Área del círculo: {circulo.calcular_area()}")
    print(f"Área del triángulo: {triangulo.calcular_area()}")

main()
