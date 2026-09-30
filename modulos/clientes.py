from modulos.validaciones import *


ESTADOS = ["En proceso de inscripción","Inscrito","Activo","Inactivo"]

RIESGOS = ["Alto","Medio","Bajo"]

def buscar_cliente(datos, identificacion):

    for cliente in datos["clientes"]:
        if cliente["identificacion"] == identificacion:
            return cliente
    return None

def registrar_cliente(datos):
    print("\n" + "=" * 50)
    print("          REGISTRO DE CLIENTE")
    print("=" * 50)

    identificacion = pedir_numero("Número de identificación: ")

    if buscar_cliente(datos, identificacion):

        print("Ya existe un cliente con esa identificación.")
        return False

    nombres = pedir_texto("Nombres: ")
    apellidos = pedir_texto("Apellidos: ")

    while True:

        direccion = input("Dirección: ").strip()
        if direccion:
            break
        print("La dirección no puede estar vacía.")

    celular = pedir_telefono("Número de celular: ")
    telefono_fijo = pedir_telefono("Número fijo: ")
    estado = pedir_opcion("Seleccione el estado:",ESTADOS)
    riesgo = pedir_opcion("Seleccione el nivel de riesgo:",RIESGOS)
    cliente = {"identificacion": identificacion,"nombres": nombres,"apellidos": apellidos,"direccion": direccion,"celular": celular,
        "telefono_fijo": telefono_fijo,"estado": estado,"riesgo": riesgo,"asistencias": [],"progreso": []}
    
    datos["clientes"].append(cliente)
    print("\nCliente registrado correctamente.")
    return True

def listar_clientes(datos):

    print("\n" + "=" * 50)
    print("             CLIENTES")
    print("=" * 50)

    if not datos["clientes"]:
        print("No hay clientes registrados.")
        return

    for cliente in datos["clientes"]:
        print("-" * 50)
        print(f"Identificación: {cliente['identificacion']}")
        print(f"Nombre: {cliente['nombres']} {cliente['apellidos']}")
        print(f"Dirección: {cliente['direccion']}")
        print(f"Celular: {cliente['celular']}")
        print(f"Teléfono fijo: {cliente['telefono_fijo']}")
        print(f"Estado: {cliente['estado']}")
        print(f"Nivel de riesgo: {cliente['riesgo']}")

def cambiar_estado_cliente(datos):

    identificacion = pedir_numero("Identificación del cliente: ")

    cliente = buscar_cliente(datos,identificacion)

    if cliente is None:
        print("Cliente no encontrado.")
        return False

    print(f"\nEstado actual: {cliente['estado']}")
    nuevo_estado = pedir_opcion("Seleccione el nuevo estado:",ESTADOS)
    cliente["estado"] = nuevo_estado
    print("Estado actualizado.")
    return True

def registrar_asistencia(datos):

    identificacion = pedir_numero("Identificación del cliente: ")
    cliente = buscar_cliente(datos,identificacion)

    if cliente is None:
        print("Cliente no encontrado.")
        return False

    fecha = pedir_fecha("Fecha de asistencia")
    cliente["asistencias"].append(fecha)
    print("Asistencia registrada.")
    return True

def registrar_progreso(datos):
    identificacion = pedir_numero("Identificación del cliente: ")

    cliente = buscar_cliente(datos,identificacion)

    if cliente is None:
        print("Cliente no encontrado.")
        return False

    print("\n========== EVALUACIÓN FÍSICA ==========")

    fecha = pedir_fecha("Fecha de evaluación")

    peso = pedir_entero("Peso en kg: ",1,500)

    resistencia = pedir_entero("Resistencia (1-10): ",1,10)

    fuerza = pedir_entero("Fuerza (1-10): ",1,10)

    flexibilidad = pedir_entero("Flexibilidad (1-10): ",1,10)

    evaluacion = {"fecha": fecha,"peso": peso,"resistencia": resistencia,"fuerza": fuerza,"flexibilidad": flexibilidad}
    cliente["progreso"].append(evaluacion)
    print("Evaluación registrada.")
    return True

def consultar_perfil(datos):

    identificacion = pedir_numero("Identificación del cliente: ")
    cliente = buscar_cliente(datos,identificacion)

    if cliente is None:
        print("Cliente no encontrado.")
        return
    
    print("\n========== PERFIL ==========")
    print(f"Identificación: {cliente['identificacion']}")
    print(f"Nombre: {cliente['nombres']} {cliente['apellidos']}")
    print(f"Dirección: {cliente['direccion']}")
    print(f"Celular: {cliente['celular']}")
    print(f"Teléfono fijo: {cliente['telefono_fijo']}")
    print(f"Estado: {cliente['estado']}")
    print(f"Riesgo: {cliente['riesgo']}")

def consultar_progreso(datos):

    identificacion = pedir_numero("Identificación del cliente: ")
    cliente = buscar_cliente(datos,identificacion)
    if cliente is None:

        print("Cliente no encontrado.")
        return

    print("\n========== PROGRESO ==========")

    if not cliente["progreso"]:
        print("No existen evaluaciones.")
        return
    for numero, evaluacion in enumerate(cliente["progreso"],1):

        print(f"\nEvaluación #{numero}")
        print(f"Fecha: {evaluacion['fecha']}")
        print(f"Peso: {evaluacion['peso']} kg")
        print(f"Resistencia: {evaluacion['resistencia']}/10")
        print(f"Fuerza: {evaluacion['fuerza']}/10")
        print(f"Flexibilidad: {evaluacion['flexibilidad']}/10")

def consultar_asistencia(datos):

    identificacion = pedir_numero("Identificación del cliente: ")
    cliente = buscar_cliente(datos,identificacion)

    if cliente is None:
        print("Cliente no encontrado.")
        return

    print("\n========== ASISTENCIAS ==========")

    if not cliente["asistencias"]:
        print("No existen asistencias.")
        return

    for numero, fecha in enumerate(cliente["asistencias"],1):
        print(f"{numero}. {fecha}")