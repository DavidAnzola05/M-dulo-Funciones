def suma_DAAC(a_DAAC, b_DAAC):
    return a_DAAC + b_DAAC

def resta_DAAC(a_DAAC, b_DAAC):
    return a_DAAC - b_DAAC

def multiplicacion_DAAC(a_DAAC, b_DAAC):
    return a_DAAC * b_DAAC

def division_DAAC(a_DAAC, b_DAAC):
    if b_DAAC == 0:
        return "Error: División por cero"
    return a_DAAC / b_DAAC

def calculadora_DAAC():
    print("Seleccione una operación")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    opcion_DAAC = input("Ingrese el número de la operación (1/2/3/4): ")
    num1_DAAC = float(input("Ingrese el primer número: "))
    num2_DAAC = float(input("Ingrese el segundo número: "))
    
    if opcion_DAAC == '1':
        resultado_DAAC = suma_DAAC(num1_DAAC, num2_DAAC)
    elif opcion_DAAC == '2':
        resultado_DAAC = resta_DAAC(num1_DAAC, num2_DAAC)
    elif opcion_DAAC == '3':
        resultado_DAAC = multiplicacion_DAAC(num1_DAAC, num2_DAAC)
    elif opcion_DAAC == '4':
        resultado_DAAC = division_DAAC(num1_DAAC, num2_DAAC)
    else:
        resultado_DAAC = "Opción inválida"
    
    print(f"Resultado: {resultado_DAAC}")

calculadora_DAAC()
