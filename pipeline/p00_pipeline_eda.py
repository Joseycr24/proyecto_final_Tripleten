import os
import sys
from pathlib import Path

# Agregar el directorio raíz del proyecto al sys.path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

# Ahora importa las funciones desde su ubicación correcta
from functions.eda.explora_analysis import (
    run_general_analysis,
    descriptive_analysis,
    run_visualization_analysis
)

def create_output_directory():
    output_dir = Path("visualization/eda_preprocessing")
    output_dir.mkdir(parents=True, exist_ok=True)  # Crear la carpeta si no existe
    
def main():
    """
    Ejecuta el pipeline de análisis exploratorio de datos (EDA) para el proyecto.

    Este script coordina el flujo de trabajo del análisis exploratorio de datos (EDA) ejecutando varios
    pasos de procesamiento. En este caso, primero ejecuta el script 'epp00.py', que realiza un preprocesamiento
    inicial de los datos. Este pipeline se puede expandir en el futuro para incluir pasos adicionales como limpieza de datos
    o entrenamiento de modelos.

    Pasos actuales:
    - Ejecución del script de preprocesamiento: `epp00.py`
    - Posibilidad de añadir más pasos (por ejemplo, limpieza de datos y modelado). 

    Este archivo forma parte del pipeline para asegurar que todos los pasos de EDA se ejecuten correctamente
    antes de proceder con otros análisis o el entrenamiento de modelos.
    """
    print("=== Iniciando el pipeline de EDA ===")
    
    # Definir la ruta del archivo de preprocesamiento
    preprocessing_script = "eda/preprocessing/epp00.py"
    
    # Verificar si el archivo de preprocesamiento existe
    if os.path.exists(preprocessing_script):
        try:
            # Ejecutar el script de preprocesamiento
            result = os.system(f"python {preprocessing_script}")

            # Verificar si el script se ejecutó correctamente
            if result != 0:
                print(f"El script {preprocessing_script} terminó con errores.")
            else:
                print(f"El script {preprocessing_script} se ejecutó correctamente.")
        
        except Exception as e:
            print(f"Error al ejecutar el script de preprocesamiento: {e}")
    
    else:
        print(f"Error: No se encuentra el archivo {preprocessing_script}")

    print("=== Pipeline de EDA completado ===")

if __name__ == "__main__":
    main()
