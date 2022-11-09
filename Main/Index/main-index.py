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

#main - resources

diametro = 6, 7, 8, 9, 10, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39, 42, 45, 52, 56, 60, 64, 68, 72, 76, 80

paso = 1, 1.25, 1.5, 2, 2.25, 3, 3.5, 4, 4.5, 5, 5.5, 6

largo = 1/4, 1/2, 3/4, 1

rosca = "rosca izquierda", "rosca derecha"

cantidad = "cant1 por unidad", "cant2 por kilogramos"

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


while True:
    diametro = input("Indique el diametro")
    if diametro != "6":
        print("Indique un diametro valido")
    else:
        print("Bien")
        break
    continue

while True:
    paso = input("Indique el paso")
    if paso != "1":
        print("Indique un paso valido")
    else:
        print("Bien")
        break
    continue

while True:
    largo = input("Indique el largo")
    if largo != "1/4":
        print("Indique un largo valido")
    else:
        print("Bien")
        break
    continue

while True:
    rosca = input("Indique tipo de rosca")
    if rosca != "rosca izquierda":
        print("Indique un tipo de rosca valido")
    else:
        print("Bien")
        break
    continue

while True:
    cantidad = input("Indique la cantidad")
    if cantidad != "cant1 por unidad":
        print("Indique una cantidad valida")
    else:
        print("Bien")
        break
    continue

