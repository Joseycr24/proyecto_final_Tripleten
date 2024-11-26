import os
import sys
import argparse
import pandas as pd

# Agregar la carpeta raíz del proyecto a sys.path
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__),'..'))) 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.eda.explora_analysis import run_pipeline

# Argumentos por línea de comandos ----------------------------------------
parser = argparse.ArgumentParser(description="Ejecutar EDA para los datasets")
parser.add_argument('--periodo', type=str, required=True, help="Periodo en formato YYYYMM")
args = parser.parse_args()

# Información de inicio
print(f"---------------------------------- \nComenzando proceso de EDA para el periodo: {args.periodo}\n----------------------------------")

# Lista de datasets (puedes añadir más según sea necesario)
datasets = [
    {'ruta': 'files/datasets/input/contract.csv', 'nombre': 'contract'},
    {'ruta': 'files/datasets/input/internet.csv', 'nombre': 'internet'},
    {'ruta': 'files/datasets/input/personal.csv', 'nombre': 'personal'},
    {'ruta': 'files/datasets/input/phone.csv', 'nombre': 'phone'}
]

# Procesar cada dataset ----------------------------------------
for dataset in datasets:
    dataset_path = dataset['ruta']
    dataset_name = dataset['nombre']
    
    # Verificar que el archivo exista
    if not os.path.exists(dataset_path):
        print(f"Error: El archivo {dataset_path} no existe.")
        continue  # Pasar al siguiente dataset si el actual no existe
    
    # Cargar el dataset
    print(f"Cargando dataset: {dataset_name}")
    df = pd.read_csv(dataset_path)
    
    # Ejecutar el análisis EDA usando la función 'run_pipeline' o cualquier función que tengas
    print(f"Ejecutando EDA para el dataset: {dataset_name}")
    run_pipeline(df, dataset_name, periodo=args.periodo)  # Asumimos que run_pipeline acepta el periodo

print("\n---------------------------------- \nProceso de EDA finalizado.\n----------------------------------")
