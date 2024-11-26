import os
import sys
import argparse
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.eda.explora_analysis import run_pipeline

parser = argparse.ArgumentParser(description="Ejecutar EDA combinado para los datasets")
parser.add_argument('--periodo', type=str, required=True, help="Periodo en formato YYYYMM")
args = parser.parse_args()

print(f"---------------------------------- \nComenzando proceso de EDA combinado para el periodo: {args.periodo}\n----------------------------------")

datasets = {
    'contract': 'files/datasets/input/contract.csv',
    'internet': 'files/datasets/input/internet.csv',
    'personal': 'files/datasets/input/personal.csv',
    'phone': 'files/datasets/input/phone.csv'
}

dataframes = {}

for name, path in datasets.items():
    if not os.path.exists(path):
        print(f"Error: El archivo {path} no existe. Omitiendo...")
        continue

    print(f"Cargando dataset: {name}")
    dataframes[name] = pd.read_csv(path)

# Combinar datasets
print("Combinando datasets...")
telecom = (
    dataframes['contract']
    .merge(dataframes['personal'], on="customerID", how='outer')
    .merge(dataframes['internet'], on="customerID", how='outer')
    .merge(dataframes['phone'], on="customerID", how='outer')
)

# Crear una copia de telecom
telecom_copy = telecom.copy()

# Guardar telecom_copy en un archivo CSV en la ubicación especificada
output_path = 'files/datasets/intermedia/telecom_copy.csv'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Crear directorio si no existe
telecom_copy.to_csv(output_path, index=False)

print(f"Dataset combinado guardado en: {output_path}")

print("Ejecutando análisis EDA para el dataset combinado...")
run_pipeline(telecom, "telecom_combined", periodo=args.periodo)

print("\n---------------------------------- \nProceso de EDA combinado finalizado.\n----------------------------------")
