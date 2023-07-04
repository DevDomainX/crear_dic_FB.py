#!/usr/bin/env python3
# Author: Hans Saldias

from colorama import Fore, Back

print(Fore.CYAN+Back.BLUE+"""
########################################
|| Script para crear diccionarios para terminar escriba salir ||
########################################
""")
print("\npara salir (exit) si ya tetmino de agregar contraseñas\n")
archivo = input("Ingresa el nombre a poner al archivo: ")
archivo = archivo + ".txt"
with open(archivo, "a") as con:
    while True:
        print("Ingrese una contraseña a la vez \n")
        pw = input("Ingrese contraseña: ")
        con.write(f"{pw}\n")
        print("Ingresada siga agregando....\n")
        if pw == "exit":
            print("Para crear otro solo reinicia el script")
            print("craedor: Hans Saldias")
            break
        
