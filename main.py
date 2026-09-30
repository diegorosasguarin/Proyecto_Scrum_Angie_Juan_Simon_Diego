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