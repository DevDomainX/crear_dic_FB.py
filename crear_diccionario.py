#!/usr/bin/env python3
# Author: Hans Saldias

from colorama import Fore

print(Fore.CYAN+"""
########################################
|| Script para crear diccionarios para terminar escriba salir ||
########################################
""")
print("\npara salir (exit) si ya tetmino de agregar contraseñas\n")
archivo = input("Ingresa el nombte a poner al archivo: ")
archivo = archivo + ".txt"
with open(archivo, "a") as con:
    while True:
        pw = input("Ingrese contraseñas: ")
        con.write(f"{pw}\n")
        if pw == "exit":
            print("Para crear otro solo reinicia el script")
            break
        