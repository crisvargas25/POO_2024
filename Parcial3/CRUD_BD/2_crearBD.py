import mysql.connector

try:
    conexion=mysql.connector.connect(host='localhost', user='root', password='')

except:
    print("Ocurrio un error con el sistema, por favor verifique")

else:
    #crear un objeto de tipo cursor que permita ejecutar instrucciones SQL

    micursor=conexion.cursor()

    sql="CREATE DATABASE bd_python"
    #ejevutar la consulta
    micursor.execute(sql)

    if micursor:
        print("bien hecho")

    #mostrar las bases de datos que exiten en el servidor

    micursor.execute("SHOW DATABASES")

    for x in micursor:
        print(x)
