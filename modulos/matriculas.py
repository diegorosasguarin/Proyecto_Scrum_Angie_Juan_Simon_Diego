from modulos.validaciones import *
from modulos.clientes import buscar_cliente
from modulos.servicios import buscar_servicio
from modulos.instructores import buscar_instructor


def contar_matriculas_servicio(
    datos,
    id_servicio
):

    cantidad = 0

    for matricula in datos["matriculas"]:

        if (matricula["servicio_id"] == id_servicio and matricula["estado"] == "Activa"):
            cantidad += 1
    return cantidad

def cliente_tiene_servicio(datos,identificacion,id_servicio):

    for matricula in datos["matriculas"]:

        if (matricula["cliente_id"] == identificacion and matricula["servicio_id"] == id_servicio and matricula["estado"] == "Activa"):
            return True
    return False

def registrar_matricula(datos):

    print("\n" + "=" * 50)
    print("            NUEVA MATRÍCULA")
    print("=" * 50)

    identificacion = pedir_numero("Identificación del cliente: ")

    cliente = buscar_cliente(datos,identificacion)

    if cliente is None:

        print("El cliente no existe.")
        return False

    if cliente["estado"] == "Inactivo":

        print("No se puede matricular un cliente inactivo.")
        return False

    print("\n========== SERVICIOS ==========")

    for servicio in datos["servicios"]:

        ocupados = contar_matriculas_servicio(datos,servicio["id"])

        disponibles = (servicio["capacidad"] - ocupados)

        print(f"{servicio['id']}. {servicio['nombre']} | Cupos disponibles: {disponibles}")

    id_servicio = pedir_entero("ID del servicio: ")

    servicio = buscar_servicio(datos,id_servicio)

    if servicio is None:

        print("El servicio no existe.")
        return False

    if cliente_tiene_servicio(datos,identificacion,id_servicio):

        print("El cliente ya está matriculado en este servicio.")
        return False

    ocupados = contar_matriculas_servicio(datos,id_servicio)

    if ocupados >= servicio["capacidad"]:
        print("No hay cupos disponibles.")
        return False

    print("\n========== INSTRUCTORES ACTIVOS ==========")

    instructores_activos = [instructor
        for instructor in datos["instructores"]
        if instructor["estado"] == "Activo"
    ]

    if not instructores_activos:

        print("No existen instructores activos.")
        return False

    for instructor in instructores_activos:

        print(f"{instructor['identificacion']} - {instructor['nombre']}")

    id_instructor = pedir_numero("Identificación del instructor: ")

    instructor = buscar_instructor(datos,id_instructor)

    if (instructor is None or instructor["estado"] != "Activo"):
        print(" Instructor inválido o inactivo.")
        return False

    fecha_inicio = pedir_fecha("Fecha de inicio")
    duracion = pedir_entero("Duración en meses: ",1,120)

    matricula = {
        "cliente_id": identificacion,
        "servicio_id": id_servicio,
        "instructor_id": id_instructor,
        "fecha_inicio": fecha_inicio,
        "duracion": duracion,
        "estado": "Activa"
    }

    datos["matriculas"].append(matricula)

    print("\nMatrícula registrada correctamente.")
    return True
