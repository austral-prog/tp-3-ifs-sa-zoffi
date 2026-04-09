def positive():
    """
    Ejercicio 1 - Clasificar Número

    Leer un número entero mediante input(). Determinar si es positivo, negativo o cero
    e imprimir el resultado correspondiente.

    Ejemplo:
        Para la entrada "5", la salida esperada es:
        El numero es positivo

        Para la entrada "-3", la salida esperada es:
        El numero es negativo

        Para la entrada "0", la salida esperada es:
        El numero es cero
    """
    num=int(input("escriba un numero: "))
    if num>0:
        print("El numero es positivo")
    elif num==0:
        print("El numero es cero")
    elif num<0:
        print("El numero es negativo")
#positive()