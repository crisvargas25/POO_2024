# 6.- Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10

for i in range(1,11):
    print(f"......TABLA DEL {i} .......")
    for m in range(1,11):
        resultado=m*i
        print(f" {i} x {m} = {resultado}")
    print()