from modulos.persistencia import *
from modulos.servicios import *
from modulos.clientes import *
from modulos.instructores import *
from modulos.matriculas import *
from modulos.reportes import *

def guardar_si_corresponde(datos, resultado):

    if resultado:
        guardar_datos(datos)

# =========================================================
# MENÚ ADMINISTRADOR
# =========================================================

def menu_administrador(datos):

    while True:

        print("\n")
        print("=" * 60)
        print("              FORCE TECH")
        print("          MENÚ ADMINISTRADOR")
        print("=" * 60)
        print("1. Registrar cliente\n2. Listar clientes\n3. Cambiar estado de cliente\n4. Registrar servicio\n5. Listar servicios\n6. Registrar instructor")
        print("7. Listar instructores\n8. Registrar matrícula\n9. Listar matrículas\n10. Cancelar matrícula\n11. Registrar asistencia\n12. Registrar evaluación de progreso\n13. Reportes")
        print("0. Volver")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            resultado = registrar_cliente(datos)
            guardar_si_corresponde(datos,resultado)

        elif opcion == "2":
            listar_clientes(datos)

        elif opcion == "3":
            resultado = cambiar_estado_cliente(datos)
            guardar_si_corresponde(datos,resultado)

        elif opcion == "4":
            resultado = agregar_servicio(datos)
            guardar_si_corresponde(datos,resultado)

        elif opcion == "5":
            listar_servicios(datos)


        elif opcion == "6":
            resultado = registrar_instructor(datos)
            guardar_si_corresponde(datos,resultado)

        elif opcion == "7":
            listar_instructores(datos)

        elif opcion == "8":
            resultado = registrar_matricula(datos)
            guardar_si_corresponde(datos,resultado)

        elif opcion == "9":
            listar_matriculas(datos)

        elif opcion == "10":
            resultado = cancelar_matricula(datos)
            guardar_si_corresponde(datos,resultado)

        elif opcion == "11":
            resultado = registrar_asistencia(datos)
            guardar_si_corresponde(datos,resultado)

        elif opcion == "12":
            resultado = registrar_progreso(datos)
            guardar_si_corresponde(datos, resultado)

        elif opcion == "13":
            menu_reportes(datos)

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")
            

# =========================================================
# MENÚ INSTRUCTOR
# =========================================================

def menu_instructor(datos):

    while True:

        print("\n")
        print("=" * 60)
        print("              FORCE TECH")
        print("           MENÚ INSTRUCTOR")
        print("=" * 60)

        print("1. Registrar asistencia\n2. Registrar evaluación de progreso\n3. Listar clientes\n4. Consultar progreso\n0. Volver")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            resultado = registrar_asistencia(datos)
            guardar_si_corresponde(datos,resultado)

        elif opcion == "2":
            resultado = registrar_progreso(datos)
            guardar_si_corresponde(datos,resultado)

        elif opcion == "3":
            listar_clientes(datos)

        elif opcion == "4":
            consultar_progreso(datos)

        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
            

# =========================================================
# MENÚ CLIENTE
# =========================================================

def menu_cliente(datos):

    while True:

        print("\n")
        print("=" * 60)
        print("              FORCE TECH")
        print("             MENÚ CLIENTE")
        print("=" * 60)

        print("1. Consultar perfil\n2. Consultar progreso\n3. Consultar asistencia\n0. Volver")
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            consultar_perfil(datos)

        elif opcion == "2":
            consultar_progreso(datos)

        elif opcion == "3":
            consultar_asistencia(datos)

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")


# =========================================================
# REPORTES
# =========================================================

def menu_reportes(datos):

    while True:

        print("\n")
        print("=" * 60)
        print("                REPORTES")
        print("=" * 60)

        print("1. Listar clientes inscritos\n2. Servicios y capacidad\n3. Instructores activos\n4. Clientes con riesgo alto\n5. Clientes con bajo rendimiento\n6. Progreso de clientes\n7. Reporte de asistencia")
        print("0. Volver")
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            reporte_clientes_inscritos(datos)

        elif opcion == "2":
            reporte_servicios(datos)

        elif opcion == "3":
            reporte_instructores_activos(datos)

        elif opcion == "4":
            reporte_riesgo_alto(datos)

        elif opcion == "5":
            reporte_bajo_rendimiento(datos)

        elif opcion == "6":
            reporte_progreso(datos)

        elif opcion == "7":
            reporte_asistencia(datos)

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")


# =========================================================
# PROGRAMA PRINCIPAL
# =========================================================

def main():

    datos = cargar_datos()
    inicializar_servicios(datos)
    guardar_datos(datos)

    while True:

        print("\n")
        print("=" * 60)
        print("              GIMNASIO FORCE TECH")
        print("          SISTEMA DE GESTIÓN")
        print("=" * 60)

        print("1. Administrador\n2. Instructor\n3. Cliente\n0. Salir")

        opcion = input("\nSeleccione su rol: ").strip()

        if opcion == "1":
            menu_administrador(datos)

        elif opcion == "2":
            menu_instructor(datos)

        elif opcion == "3":
            menu_cliente(datos)

        elif opcion == "0":
            guardar_datos(datos)
            print("\n✅ Información guardada.")
            print("Gracias por utilizar ForceTech.")
            break

        else:
            print("Rol inválido. Intente nuevamente.")

if __name__ == "__main__":
    main()