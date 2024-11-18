#importar las funciones del archivo operaciones.py
from operaciones import suma, resta, multiplicacion, division

repetir = "s"
while repetir != "n":
    print("-----------------------")
    print("      Calculadora      ")
    print("-----------------------")
    print("      1-Sumar          ")
    print("      2-Restar         ")
    print("      3-Multiplicar    ")
    print("      4-Dividir        ")
    print("-----------------------")
   
    while True:
        op = input("Operación a realizar? (1-4): ")
    
        if op.isdigit():#verificar si la opcion introducida es un número
            op = int(op)
            if op in [1, 2, 3, 4]:#verificar que está entre 1 y 4
                break#si el valor es válido, salir de este ciclo
            else:
                print("El valor debe estar entre 1 y 4.")
        else:
            print("El valor debe ser un número válido entre 1 y 4.")
   
    #solicitar los números
    n1 = int(input("Introduce el primer número: "))
    n2 = int(input("Introduce el segundo número: "))

   
    #realizar la operación correspondiente e mostrar el resultado
    if op == 1:
        resultado = suma(n1, n2)
        print(f"Resultado: {resultado}")
    elif op == 2:
        resultado = resta(n1, n2)
        print(f"Resultado: {resultado}")
    elif op == 3:
        resultado = multiplicacion(n1, n2)
        print(f"Resultado: {resultado}")
    elif op == 4:
        resultado = division(n1, n2)
        print(f"Resultado: {resultado}")
       
    #preguntar si quiere realizar otra operación
    repetir = input("¿Quiere realizar otra operación? (s/n): ").lower()
    if(repetir!="s" and repetir!="n"):
        print("No ha introducido ni s ni n")
