import os
import funciones

def menu_peliculas():
    print("\t...::BIENVENIDO!::...\n")
    peliculas = [
        "Mortal Kombat",
        "Barbie",
        "Rudo y Cursi",
        "Mad Max",
        "Halo 4",
    ]

    while True:
        print("\nMenu de Opciones: ")
        print("1.- Agregar peliculas\n2.- Remover peliculas\n3.- Consultar peliculas\n4.- Buscar pelicula\n5.- Vaciar lista\n6.- Actualizar pelicula\n7.- Salir")
        opcion = input("¿Qué deseas hacer? \n")

        if opcion == "1":
            funciones.agregar_pelicula(peliculas)
        elif opcion == "2":
            funciones.remover_pelicula(peliculas)
        elif opcion == "3":
            funciones.consultar_pelicula(peliculas)
        elif opcion == "4":
            funciones.buscar_pelicula(peliculas)
        elif opcion == "5":
            funciones.vaciar_lista(peliculas)
        elif opcion == "6":
            funciones.actualizar_pelicula(peliculas)
        elif opcion == "7":
            print("Gracias por usar el gestor de películas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

        input("Presiona Enter para continuar...")
        os.system("clear")

menu_peliculas()
