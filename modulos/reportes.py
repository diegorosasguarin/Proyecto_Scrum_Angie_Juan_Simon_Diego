from modulos.clientes import *
from modulos.servicios import *
from modulos.instructores import *


def reporte_clientes_inscritos(datos):

    print("\n========== CLIENTES INSCRITOS ==========")

    encontrados = False

    for cliente in datos["clientes"]:

        if cliente["estado"] in [
            "Inscrito",
            "Activo"
        ]:

            encontrados = True
            print(f"{cliente['identificacion']} - {cliente['nombres']} {cliente['apellidos']} - {cliente['estado']}")

    if not encontrados:

        print("No existen clientes inscritos.")


def reporte_servicios(datos):

    print("\n========== SERVICIOS Y CAPACIDAD ==========")

    if not datos["servicios"]:

        print("No existen servicios.")
        return

    for servicio in datos["servicios"]:

        ocupados = 0

        for matricula in datos["matriculas"]:

            if (matricula["servicio_id"] == servicio["id"] and matricula["estado"] == "Activa"):

                ocupados += 1

        disponibles = (servicio["capacidad"] - ocupados)

        print("-" * 55)
        print(f"Servicio: {servicio['nombre']}")
        print(f"Capacidad máxima: {servicio['capacidad']}")
        print(f"Cupos ocupados: {ocupados}")
        print(f"Cupos disponibles: {disponibles}")


def reporte_instructores_activos(datos):

    print("\n========== INSTRUCTORES ACTIVOS ==========")

    encontrados = False

    for instructor in datos["instructores"]:

        if instructor["estado"] == "Activo":
            encontrados = True
            print(f"{instructor['identificacion']} - {instructor['nombre']}")

    if not encontrados:

        print("No hay instructores activos.")


def reporte_riesgo_alto(datos):
    print("\n========== CLIENTES CON RIESGO ALTO ==========")

    encontrados = False

    for cliente in datos["clientes"]:

        if cliente["riesgo"] == "Alto":

            encontrados = True

            print(f"{cliente['identificacion']} - {cliente['nombres']} {cliente['apellidos']}")

    if not encontrados:
        print("No existen clientes con riesgo alto.")


def calcular_rendimiento(evaluacion):

    return (
        evaluacion["resistencia"]
        + evaluacion["fuerza"]
        + evaluacion["flexibilidad"]
    ) / 3


def reporte_bajo_rendimiento(datos):

    print("\n========== BAJO RENDIMIENTO ==========")

    encontrados = False
    for cliente in datos["clientes"]:

        if not cliente["progreso"]:
            continue

        ultima_evaluacion = (cliente["progreso"][-1])

        promedio = calcular_rendimiento(ultima_evaluacion)

        if promedio < 5:

            encontrados = True
            print(f"{cliente['identificacion']} - {cliente['nombres']} {cliente['apellidos']} | Promedio: {promedio:.2f}")

    if not encontrados:

        print("No existen clientes con bajo rendimiento.")


def reporte_progreso(datos):

    print("\n========== PROGRESO DE CLIENTES ==========")

    if not datos["clientes"]:

        print("No existen clientes.")
        return

    for cliente in datos["clientes"]:

        print("\n" + "-" * 55)

        print(f"Cliente: {cliente['nombres']} {cliente['apellidos']}")

        if not cliente["progreso"]:

            print("Sin evaluaciones registradas.")
            continue

        for numero, evaluacion in enumerate(cliente["progreso"],1):
            promedio = calcular_rendimiento(evaluacion)
            print(f"\nEvaluación #{numero}")
            print(f"Fecha: {evaluacion['fecha']}")
            print(f"Peso: {evaluacion['peso']} kg")
            print(f"Resistencia: {evaluacion['resistencia']}/10")
            print(f"Fuerza: {evaluacion['fuerza']}/10")
            print(f"Flexibilidad: {evaluacion['flexibilidad']}/10")
            print(f"Promedio: {promedio:.2f}/10")


def reporte_asistencia(datos):

    print("\n========== REPORTE DE ASISTENCIA ==========")

    for cliente in datos["clientes"]:

        print("-" * 50)
        print(f"{cliente['nombres']} {cliente['apellidos']}")
        print(f"Total asistencias: {len(cliente['asistencias'])}")