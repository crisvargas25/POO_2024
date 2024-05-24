calculos=0

while True:
    peso=float(input("ingrese peso: "))
    altura=float(input("ingrese altura en metros: "))

    imc= peso / (altura*altura)

    if imc < 18.5:
         composición="Peso inferior al normal"
    elif imc >= 18.5 and imc<=24.9:
         composición="normal"
    elif imc >= 25.5 and imc<=29.9:
         composición="peso superior"
    else:
         composición="Obesidad"

    print(f"Su IMC es: {imc}")
    print(f"Clasificación: {composición}")
    
    calculos=+1

    continuar=input("\n Deseas otra captura (SI/NO)?").upper()
    if continuar == "SI":
        continue
    else:
        break

print(f"Total de cálculos de IMC realizados: {calculos}")

    

         
         