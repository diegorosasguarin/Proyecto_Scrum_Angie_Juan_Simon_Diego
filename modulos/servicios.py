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
def buscar_servicio(datos, id_servicio):

    for servicio in datos["servicios"]:

        if servicio["id"] == id_servicio:
            return servicio

    return None


def listar_servicios(datos):

    print("\n" + "=" * 50)
    print("             SERVICIOS")
    print("=" * 50)

    if not datos["servicios"]:

        print("No existen servicios.")
        return

    for servicio in datos["servicios"]:

        print(
            f"{servicio['id']}. "
            f"{servicio['nombre']} "
            f"| Capacidad: "
            f"{servicio['capacidad']}"
        )


def agregar_servicio(datos):

    print("\n========== NUEVO SERVICIO ==========")

    nombre = pedir_texto("Nombre del servicio: ")

    capacidad = pedir_entero("Capacidad máxima: ",1,1000)

    nuevo_id = 1

    if datos["servicios"]:

        nuevo_id = max(
            servicio["id"]
            for servicio in datos["servicios"]
        ) + 1

    nuevo_servicio = {
        "id": nuevo_id,
        "nombre": nombre,
        "capacidad": capacidad
    }

    datos["servicios"].append(nuevo_servicio)

    print("✅ Servicio registrado.")

    return True
