import os
import sys
import argparse
sys.path.append(os.getcwd())  # Esto agrega la ruta actual al path

import params as params  # Importar el archivo de configuración

# Argumentos por línea de comandos ---------------------------------------- 
parser = argparse.ArgumentParser(description="Pipeline para ejecutar epp00.py")
parser.add_argument('--periodo', default=f'{params.periodo_YYYYMM}', help='Periodo en formato YYYYMM')

# Parsear los argumentos
try:
    args = parser.parse_args()
except argparse.ArgumentTypeError as e:
    print(f"Invalid argument: {e}")
    sys.exit(1)

# Información de inicio ---------------------------------------- 
print(f"---------------------------------- \nComenzando proceso para periodo: {args.periodo}\n----------------------------------")

# Definir la extensión de ejecutables para Windows o Linux
if params.sistema_operativo == 'Windows':
    extension_binarios = ".exe"
else:
    extension_binarios = ""

# Ejecutar epp00.py ---------------------------------------- 
# Aquí ejecutamos epp00.py, y le pasamos los parámetros de periodo si es necesario
os.system(f"python{extension_binarios} eda/preprocessing/epp00.py --periodo {args.periodo}")
