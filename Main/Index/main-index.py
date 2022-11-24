#******************************************
# Primer commit main app-prueba
# subir a Github
# index
# ejecutable.exe
# release: 31/10/2022
# Developer: H. Leandro Mangicavalli
#******************************************

from ast import While
from cgitb import reset
from operator import concat
from tkinter import N, Y
import Calendario

#main - resources
deseaComenzar = Y,N
continuar = Y,N
diametro = 6, 7, 8, 9, 10, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39, 42, 45, 52, 56, 60, 64, 68, 72, 76, 80
paso = 1, 1.25, 1.5, 2, 2.25, 3, 3.5, 4, 4.5, 5, 5.5, 6
largo = 1/4, 1/2, 3/4, 1
rosca = "izquierda", "derecha"
cantidad = "unidad", "kilo"

#Variable de contabilidad
cuentaCantidad = 0
cuentaCantidadTotal = cuentaCantidad
cuentaKilos = 0
cuentaKilosTotal = cuentaKilos

#index

#diametro = input ("Indique diametro")
#print("usted a ingresado: " + diametro)

#paso = input ("Indique paso")
#print("usted a ingresado: " + paso)

#largo = input ("Indique largo")
#print("usted a ingresado: " + largo)

#rosca = input ("Indique rosca")
#print("usted a ingresado: " + rosca)

#cantidad = input ("Indique cantidad")
#print("usted a ingresado: " + cantidad)

def deseaComenzar ():

while True:
    deseaComenzar = input("¿Desea comenzar?")
    if deseaComenzar == Y:
        print("Ingrese las medidas a continuación:")
        break
        
    while True:
        diametro = input("Ingrese el diametro")
        if diametro != 6 or 7 or 8 or 9 or 10 or 16 or 18 or 20 or 22 or 24 or 27 or 30 or 33 or 36 or 39 or 42 or 45 or 52 or 56 or 60 or 64 or 68 or 72 or 76 or 80:
            print("Introduzca un diametro valido")
        else:
            print("Correcto")
            break
        continue

    while True:
        paso = input("Ingrese el paso")
        if paso != 1 or 1.25 or 1.5 or 2 or 2.25 or 3 or 3.5 or 4 or 4.5 or 5 or 5.5 or 6:
            print("Introduzca un paso valido")
        else:
            print("Correcto")
            break
        continue

    while True:
        largo = input("Ingrese el largo")
        if largo != 1/4 or 1/2 or 3/4 or 1:
            print("Introduzca un largo valido")
        else:
            print("Correcto")
            break
        continue

    while True:
        rosca = input("Ingrese el tipo de rosca (izquierda/derecha)")
        if rosca != "derecha":
            print("Introduzca un tipo de rosca valido")
        else:
            print("Correcto")
            break
        continue

    while True:
        cantidad = input("Indique la cantidad (unidad/kilo)")
        if cantidad != "unidad":
            print("Indique una cantidad valida")
        else:
            print("Correcto")
            break
        continue


