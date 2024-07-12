import mysql.connector 

#conectar con la bd en mysql

try:
    conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_python'
    )
except Exception as e:
    print("Ocurrio algo mal , verifica!!! ")
    print(f"Error: {e}")
    print(f"Tipo de excepcion: {type(e).__name__}")

# except InterfaceError:
#     print("Error al conectar con el servidor")

else:
    #verificar si la conexion fue exitosa
    if conexion.is_connected():
        print(f'se creo la conexion succesfully')
    else:
        print(f'no fue posible conectar co')

