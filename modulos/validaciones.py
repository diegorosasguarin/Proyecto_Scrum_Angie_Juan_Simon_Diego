import re
from datetime import datetime


def pedir_texto(mensaje):
    while True:
        dato = input(mensaje).strip()

        if dato == "":
            print("Este campo no puede estar vacío.")
            continue

        if any(char.isdigit() for char in dato):
            print("Este campo no debe contener números.")
            continue

        return dato


def pedir_numero(mensaje):
    while True:
        dato = input(mensaje).strip()

        if dato.isdigit():
            return dato

        print("Debe ingresar solamente números.")

