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

def pedir_entero(mensaje, minimo=None, maximo=None):
    while True:
        dato = input(mensaje).strip()

        try:
            numero = int(dato)

            if minimo is not None and numero < minimo:
                print(f"El valor mínimo es {minimo}.")
                continue

            if maximo is not None and numero > maximo:
                print(f"El valor máximo es {maximo}.")
                continue

            return numero

        except ValueError:
            print("Debe ingresar un número entero.")


def pedir_telefono(mensaje):
    while True:
        telefono = input(mensaje).strip()

        if telefono.isdigit() and len(telefono) in (7, 10):
            return telefono

        print("El teléfono debe tener 7 o 10 dígitos.")


def pedir_opcion(mensaje, opciones):
    while True:

        print(f"\n{mensaje}")

        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")

        seleccion = input("Seleccione una opción: ").strip()

        if seleccion.isdigit():

            numero = int(seleccion)

            if 1 <= numero <= len(opciones):
                return opciones[numero - 1]

        print("Opción inválida. Intente nuevamente.")


def pedir_fecha(mensaje):
    while True:

        fecha = input(f"{mensaje} (DD/MM/AAAA): ").strip()

        if not re.match(r"^\d{2}/\d{2}/\d{4}$", fecha):
            print("Formato incorrecto.")
            continue

        try:
            datetime.strptime(fecha, "%d/%m/%Y")
            return fecha

        except ValueError:
            print("La fecha no es válida.")


def pedir_si_no(mensaje):
    while True:

        respuesta = input(f"{mensaje} (S/N): ").strip().upper()

        if respuesta == "S":
            return True

        if respuesta == "N":
            return False

        print(" Responda únicamente S o N.")
