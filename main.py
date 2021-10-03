def menu():
    print("\nCALCULADORA EN PYTHON POR CONSOLA")
    print("1. Iniciar \n2. Salir")
    opc = input("Ingrese el numero de la opción a ejecutar: ")

    return opc


def calculadora():
    realizarOperacion = False
    mensajeIngresandoValoresIncorrectos = "No se puede continuar, no has ingresado un valor numérico."
    resultado = 0

    numero1 = input("\nIngrese el primer valor: ")
    if numero1.isdigit():
        operacion = input("Escoja la operacion que sea hacer: \n1. suma \n2. Resta \n3. multiplicacion \n4. Division \nIngrese el numero que corresponda a la operacion: ")
        
        if operacion.isdigit():
            numero2 = input("Ingrese el segundo valor: ")

            if numero2.isdigit():
                realizarOperacion = True

            else:
                print(mensajeIngresandoValoresIncorrectos)
        else:
            print(mensajeIngresandoValoresIncorrectos)    
    else:
        print(mensajeIngresandoValoresIncorrectos)
    

    if realizarOperacion:
        if(int(operacion) == 1):
            resultado = int(numero1) + int(numero2)
        elif(int(operacion) == 2):
            resultado = int(numero1) - int(numero2)
        elif(int(operacion) == 3):
            resultado = int(numero1) * int(numero2)
        elif(int(operacion) == 4):
            try:
                resultado = int(numero1) / int(numero2)
            except ZeroDivisionError:
                resultado = "No se puede dividir por 0"
        else:
            resultado = "El numero ingresado de la operacion a relizar no corresponde a ninguna de las opciones."

        print("EL RESULTADO ES: "+ str(resultado))



salir = False
while not salir:
    
    opc_menu = menu()

    if opc_menu.isdigit():
        if(int(opc_menu) == 1):
            calculadora()
        elif(int(opc_menu) == 2):
            salir = True
    else:
        print("Estas ingresando un valor errado.")