# Función sin parámetros y sin retorno
def solicitar_datos_paciente():
    global nombre, edad, estatura, tipo_sangre
    nombre = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    estatura = float(input("Ingrese la estatura del paciente (en metros): "))
    tipo_sangre = input("Ingrese el tipo de sangre del paciente: ")

# Función sin parámetros pero con retorno
def obtener_datos_paciente():
    nombre = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    estatura = float(input("Ingrese la estatura del paciente (en metros): "))
    tipo_sangre = input("Ingrese el tipo de sangre del paciente: ")
    return nombre, edad, estatura, tipo_sangre

# Función con parámetros y sin retorno
def mostrar_datos_paciente(nombre, edad, estatura, tipo_sangre):
    print(f"Nombre del paciente: {nombre}")
    print(f"Edad del paciente: {edad} años")
    print(f"Estatura del paciente: {estatura} metros")
    print(f"Tipo de sangre del paciente: {tipo_sangre}")

# Función con parámetros y con retorno
def procesar_datos_paciente(nombre, edad, estatura, tipo_sangre):
    datos_paciente = {
        "Nombre": nombre,
        "Edad": edad,
        "Estatura": estatura,
        "Tipo de Sangre": tipo_sangre
    }
    return datos_paciente

solicitar_datos_paciente()  # Llama a la función sin parámetros y sin retorno

# Llama a la función sin parámetros pero con retorno y muestra los datos
nombre, edad, estatura, tipo_sangre = obtener_datos_paciente()
print("\nDatos obtenidos de la función sin parámetros pero con retorno:")
mostrar_datos_paciente(nombre, edad, estatura, tipo_sangre)

# Procesa y obtiene un diccionario con la función con parámetros y con retorno
datos_paciente = procesar_datos_paciente(nombre, edad, estatura, tipo_sangre)
print("\nDatos procesados con la función con parámetros y con retorno:")
print(datos_paciente)
