from modulos.validaciones import *


SERVICIOS_BASE = [
    {
        "id": 1,
        "nombre": "Clases de yoga",
        "capacidad": 20
    },
    {
        "id": 2,
        "nombre": "Clases de pilates",
        "capacidad": 15
    },
    {
        "id": 3,
        "nombre": "Entrenamiento personalizado",
        "capacidad": 1
    },
    {
        "id": 4,
        "nombre": "Acceso a la piscina",
        "capacidad": 30
    },
    {
        "id": 5,
        "nombre": "Uso del gimnasio general",
        "capacidad": 50
    }
]


def inicializar_servicios(datos):

    if not datos["servicios"]:

        datos["servicios"] = [
            servicio.copy()
            for servicio in SERVICIOS_BASE
        ]
