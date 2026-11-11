
"""numero1 = int(input("Indique el número 1 : "))
numero2 = int(input("Indique el número 2 : "))
Resultado = numero1+numero2
print("el resultado de la suma es ",Resultado)"""




numero1 = int(input("Indique el número 1 : "))
numero2 = int(input("Indique el número 2 : "))

opcion = int(input(
    "\n CALCULADORA \n"
    "Seleccione la operación que desea realizar:\n\n"
    "1. Suma\n"
    "2. Resta\n"
    "3. Multiplicación\n"
    "4. División\n\n"
    "Ingrese una opción: "
))
if opción ==1:
    Resultado = numero1+numero2
    print("el resultado de la suma es ",Resultado)
elif opción ==2:
    Resultado = numero1-numero2
    print("el resultado de la Resta es ",Resultado)
elif opción ==3:
    Resultado = numero1*numero2
    print("el resultado de la Multiplicación es ",Resultado) 
elif opción ==4:
    Resultado = numero1/numero2
    print("el resultado de la división es ",Resultado)       