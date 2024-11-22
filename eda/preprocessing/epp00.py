import sys
import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from functions.eda.explora_analysis import (
    run_general_analysis,
    descriptive_analysis,
    run_visualization_analysis
)

datasets = {
    "contract": "files/datasets/input/contract.csv",
    "internet": "files/datasets/input/internet.csv",
    "personal": "files/datasets/input/personal.csv",
    "phone": "files/datasets/input/phone.csv"
}

def process_dataset(name, path):
    """
    Procesa un dataset específico ejecutando el análisis exploratorio de datos (EDA).

    Esta función carga el dataset desde el archivo CSV proporcionado y ejecuta las funciones de EDA definidas
    en el módulo `explora_analysis`. Realiza un análisis general, descriptivo y de visualización del dataset.

    Args:
    - name (str): Nombre del dataset, utilizado en los mensajes de salida para identificar el dataset.
    - path (str): Ruta del archivo CSV que contiene el dataset a procesar.

    Excepciones:
    - FileNotFoundError: Si el archivo no se encuentra en la ruta especificada.
    - Exception: Captura cualquier otro error que ocurra durante la lectura o el análisis del archivo.
    """
    print(f"\n=== Procesando dataset: {name} ===")
    
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        print(f"Error: El archivo '{path}' no se encontró. Verifica las rutas de los datasets.")
        return
    except Exception as e:
        print(f"Error al leer el archivo '{path}': {e}")
        return
    
    try:
        run_general_analysis(df, name)
        descriptive_analysis(df, name)
        run_visualization_analysis(df, name)
    except Exception as e:
        print(f"Error durante el análisis del dataset '{name}': {e}")

def main():
        for name, path in datasets.items():
            process_dataset(name, path)

if __name__ == "__main__":
    main()

