from modulos.validaciones import *

def buscar_instructor(
    datos,
    identificacion
):

    for instructor in datos["instructores"]:

        if instructor["identificacion"] == identificacion:
            return instructor

    return None


def registrar_instructor(datos):

    print("\n========== NUEVO INSTRUCTOR ==========")

    identificacion = pedir_numero("Identificación: ")
    
    if buscar_instructor(datos,identificacion):
        print("Ya existe un instructor con esa identificación.")
        return False

    nombre = pedir_texto("Nombre completo: ")
    estado = pedir_opcion("Seleccione el estado:",["Activo","Inactivo"])
    instructor = {"identificacion": identificacion,"nombre": nombre,"estado": estado}

    datos["instructores"].append(instructor)

    print("Instructor registrado.")

    return True


def listar_instructores(datos):

    print("\n========== INSTRUCTORES ==========")

    if not datos["instructores"]:

        print("No existen instructores.")
        return

    for instructor in datos["instructores"]:

        print(f"ID: {instructor['identificacion']} | Nombre: {instructor['nombre']} | Estado: {instructor['estado']}")

def listar_instructores_activos(datos):

    print("\n========== INSTRUCTORES ACTIVOS ==========")
    encontrados = False

    for instructor in datos["instructores"]:

        if instructor["estado"] == "Activo":
            encontrados = True
            print(f"{instructor['identificacion']} - {instructor['nombre']}")

    
    if not encontrados:
        print("No hay instructores activos.") 