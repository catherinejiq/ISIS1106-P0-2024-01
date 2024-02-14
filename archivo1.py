import re
import os.path

# Función para leer un archivo y retornar su contenido
def recuperar_contenido_archivo(ubi_archivo: str):
    contenido = ""
    if os.path.isfile(ubi_archivo):
        with open(ubi_archivo, 'r') as file:
            lineas = [line.strip() for line in file.readlines() if line.strip()]
            contenido = contenido.join(lineas)
    else:
        print("El archivo especificado no existe")

    return contenido

variables_definidas = {}
funciones_definidas = {}

VAR_DEF_REGEX = r'\(defvar\s+([a-zA-Z][a-zA-Z0-9]*)\s+([a-zA-Z0-9]+)\)'
FUN_DEF_REGEX = r'\(defun\s+([a-zA-Z][a-zA-Z0-9]*)\s*\(([^)]*)\)\s*(.*?)\)'
FUN_CALL_REGEX = r'\(([a-zA-Z][a-zA-Z0-9]*)\s+([^)]*)\)'


def analizar_definicion_variable(comando):
    coincidencia = re.match(VAR_DEF_REGEX, comando)
    if coincidencia:
        nombre_variable = coincidencia.group(1)
        variables_definidas[nombre_variable] = True
        return True
    return False


def analizar_definicion_funcion(comando):
    coincidencia = re.match(FUN_DEF_REGEX, comando)
    if coincidencia:
        nombre_funcion = coincidencia.group(1)
        lista_parametros = coincidencia.group(2).split()
        funciones_definidas[nombre_funcion] = lista_parametros
        return True
    return False


def analizar_llamada_funcion(comando):
    coincidencia = re.match(FUN_CALL_REGEX, comando)
    if coincidencia:
        nombre_funcion = coincidencia.group(1)
        parametros = coincidencia.group(2).split()
        if nombre_funcion in funciones_definidas:
            parametros_definidos = funciones_definidas[nombre_funcion]
            if len(parametros) == len(parametros_definidos):
                return all(parametro in variables_definidas or parametro.isdigit() for parametro in parametros)
    return False

# Función para analizar el programa completo
def analizar_programa(lineas_programa):
    for linea in lineas_programa:
        comando = linea.strip()
        if comando:
            if not (analizar_definicion_variable(comando) or 
                    analizar_definicion_funcion(comando) or 
                    analizar_llamada_funcion(comando)):
                print("no")
                return
    print("yes")

# Función principal
def main():
    ruta_archivo = input("Ingrese la ruta al archivo del programa del robot: ")
    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas_programa = archivo.readlines()
            analizar_programa(lineas_programa)
    except FileNotFoundError:
        print("Archivo no encontrado.")

if __name__ == "__main__":
    main()
