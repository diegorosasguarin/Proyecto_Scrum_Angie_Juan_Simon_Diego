import json
import os

ARCHIVO = "datos.json"

def datos_iniciales():
    return {
        "clientes": [],
        "servicios": [],
        "instructores": [],
        "matriculas": []
    }

def cargar_datos():

    if not os.path.exists(ARCHIVO):

        datos = datos_iniciales()
        guardar_datos(datos)

        return datos
    try:

        with open(ARCHIVO,"r",encoding="utf-8") as archivo:
            datos = json.load(archivo)

        datos.setdefault("clientes", [])
        datos.setdefault("servicios", [])
        datos.setdefault("instructores", [])
        datos.setdefault("matriculas", [])
        return datos

    except json.JSONDecodeError:

        print("\nEl archivo datos.json está vacío o tiene un formato incorrecto.")
        print("Se iniciará con datos vacíos.")

        datos = datos_iniciales()
        guardar_datos(datos)

        return datos

    except Exception as error:

        print(f"\nError al cargar los datos: {error}")
        return datos_iniciales()
    
def guardar_datos(datos):

    try:
        with open(ARCHIVO,"w",encoding="utf-8") as archivo:
            json.dump(datos,archivo,indent=4,ensure_ascii=False)

    except Exception as error:
        print(f"Error al guardar los datos: {error}")