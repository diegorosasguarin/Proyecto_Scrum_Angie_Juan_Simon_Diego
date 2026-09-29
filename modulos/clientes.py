from modulos.validaciones import *


ESTADOS = ["En proceso de inscripción","Inscrito","Activo","Inactivo"]

RIESGOS = ["Alto","Medio","Bajo"]

def buscar_cliente(datos, identificacion):

    for cliente in datos["clientes"]:
        if cliente["identificacion"] == identificacion:
            return cliente
    return None

