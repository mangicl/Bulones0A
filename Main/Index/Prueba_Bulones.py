from ast import While
from cgitb import reset
from operator import concat
from tkinter import N, Y

deseaComenzar = Y,N
continuar = Y,N
seleccion = 0
diametro = [6, 7, 8, 9, 10, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39, 42, 45, 52, 56, 60, 64, 68, 72, 76, 80]
paso = [1, 1.25, 1.5, 2, 2.25, 3, 3.5, 4, 4.5, 5, 5.5, 6]
largo = [1/4, 1/2, 3/4, 1]
rosca = "izquierda", "derecha"
cantidad = "unidad", "kilo"

cuentaCantidad = 0
cuentaCantidadTotal = cuentaCantidad
cuentaKilos = 0
cuentaKilosTotal = cuentaKilos


while True:
    deseaComenzar = input("¿Desea comenzar? (Y para SI / N para NO)")
    if deseaComenzar != N:
        print("Ingrese las datos a continuación:")
    elif deseaComenzar == N:
        print("")
        print("Hasta pronto")
        print("")
        break
    
    while True:
        if seleccion != 5:
            print("""Seleccione el tipo de operacion:
            1) Bulones de rosca derecha
            2) Bulones de rosca izquierda
            3) Seguir comprando
            4) Salir""")
        seleccion = int(input("Elija una opcion: "))
        if seleccion == 1:
            print(" ")
            print("Rosca derecha seleccionada")
            print(" ")

            while True:
                diametro = int(input("Ingrese el diametro: "))
                if diametro != 6:
                    print("Introduzca un diametro valido")
                else:
                    print("Diametro valido")
                    break
                continue
