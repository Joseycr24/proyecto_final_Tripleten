import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
from pathlib import Path

# ------------------------------------------------------------
# Funciones Individuales para EDA
# ------------------------------------------------------------

def general_information(df, dataset_name):
    """
    Muestra información general del dataset, como el número de entradas, columnas, 
    tipos de datos y la memoria utilizada.

    Parámetros:
    df : pandas.DataFrame
        El DataFrame que contiene los datos a analizar.
    dataset_name : str
        El nombre del dataset, utilizado en los mensajes de salida.

    Ejemplo:
    general_information(df, "clientes_dataset")
    """
    print("\n-------------------------------------------")
    print(f"Información General del dataset '{dataset_name}':")
    print("-------------------------------------------")
    df.info()


def null_data(df, dataset_name):
    """
    Muestra la cantidad de datos nulos en cada columna del dataset.

    Parámetros:
    df : pandas.DataFrame
        El DataFrame que contiene los datos a analizar.
    dataset_name : str
        El nombre del dataset, utilizado en los mensajes de salida.

    Ejemplo:
    null_data(df, "clientes_dataset")
    """
    print("\n--------------------------------------------------")
    print(f"Cantidad de datos nulos en el dataset '{dataset_name}':")
    print("--------------------------------------------------")
    nulls = df.isnull().sum()
    display(nulls.to_frame(name="Cantidad de Nulos"))


def random_sample(df, dataset_name, n=30):
    """
    Muestra una muestra aleatoria de filas del dataset.

    Parámetros:
    df : pandas.DataFrame
        El DataFrame que contiene los datos a analizar.
    dataset_name : str
        El nombre del dataset, utilizado en los mensajes de salida.
    n : int, opcional (por defecto 30)
        El número de filas a mostrar en la muestra aleatoria.

    Ejemplo:
    random_sample(df, "clientes_dataset", n=10)
    """
    print("\n-----------------------------------------")
    print(f"Muestra Aleatoria del dataset '{dataset_name}':")
    print("-----------------------------------------")
    sample = df.sample(n)
    display(sample)


def unique_values(df, dataset_name):
    """
    Muestra la cantidad de valores únicos por columna en el dataset.

    Parámetros:
    df : pandas.DataFrame
        El DataFrame que contiene los datos a analizar.
    dataset_name : str
        El nombre del dataset, utilizado en los mensajes de salida.

    Ejemplo:
    unique_values(df, "clientes_dataset")
    """
    print("\n----------------------------------------------------")
    print(f"Cantidad de valores únicos del dataset '{dataset_name}':")
    print("------------------------------------------------------")
    unique_values = df.nunique()
    display(unique_values.to_frame(name="Cantidad de Valores Únicos"))


def descript_statis(df, dataset_name):
    """
    Muestra estadísticas descriptivas para las columnas numéricas del dataset, 
    incluyendo el conteo, la media, la desviación estándar, los valores mínimo y máximo, 
    y los percentiles.

    Parámetros:
    df : pandas.DataFrame
        El DataFrame que contiene los datos a analizar.
    dataset_name : str
        El nombre del dataset, utilizado en los mensajes de salida.

    Ejemplo:
    descript_statis(df, "clientes_dataset")
    """
    print("\n--------------------------------------------------")
    print(f"Estadísticas Descriptivas del dataset '{dataset_name}':")
    print("--------------------------------------------------")
    if df.select_dtypes(include=['number']).empty:
        print("No hay columnas numéricas para mostrar estadísticas descriptivas.")
    else:
        display(df.describe())

def corre_matri(df, dataset_name):
    """
    Muestra la matriz de correlación entre las columnas numéricas del dataset.

    Parámetros:
    df : pandas.DataFrame
        El DataFrame que contiene los datos a analizar.
    dataset_name : str
        El nombre del dataset, utilizado en los mensajes de salida.

    Ejemplo:
    corre_matri(df, "clientes_dataset")
    """
    print("\n---------------------------------------------")
    print(f"Matriz de Correlación del dataset '{dataset_name}':")
    print("---------------------------------------------")
    numeric_columns = df.select_dtypes(include=['number']).columns
    if len(numeric_columns) < 2:
        print("No hay suficientes columnas numéricas para crear una matriz de correlación.")
    else:
        correlation_matrix = df[numeric_columns].corr()
        display(correlation_matrix)

        
def basic_histogram(df, dataset_name):
    """
    Genera histogramas para cada columna numérica en el dataset, mostrando la distribución de los valores.

    Parámetros:
    df : pandas.DataFrame
        El DataFrame que contiene los datos a analizar.
    dataset_name : str
        El nombre del dataset, utilizado en los mensajes de salida.

    Ejemplo:
    basic_histogram(df, "clientes_dataset")
    """   
    numeric_columns = df.select_dtypes(include=['number']).columns

    # Crear directorios para cada dataset dentro de "visualization/eda_preprocessing"
    output_dir = Path(f"visualization/eda_preprocessing/{dataset_name}")
    output_dir.mkdir(parents=True, exist_ok=True)  # Crear las carpetas si no existen
    
    for column in numeric_columns:
        plt.figure(figsize=(10, 6))
        plt.hist(df[column].dropna(), bins=30, color='skyblue', edgecolor='black')
        plt.title(f'Histograma de {column} en el dataset {dataset_name}')
        plt.xlabel(column)
        plt.ylabel('Frecuencia')
        plt.tight_layout()
        plt.show()
        
        # Guardar la gráfica en el directorio de salida correspondiente al dataset
        output_path = output_dir / f"{dataset_name}_histogram_{column}.png"
        plt.savefig(output_path)  # Guardar la gráfica
        plt.close()  # Cerrar la figura para liberar memoria

def basic_boxplots(df, dataset_name):
    """
    Genera diagramas de caja (boxplots) para cada columna numérica del dataset, mostrando la distribución 
    de los datos y los posibles valores atípicos.

    Parámetros:
    df : pandas.DataFrame
        El DataFrame que contiene los datos a analizar.
    dataset_name : str
        El nombre del dataset, utilizado en los mensajes de salida.

    Ejemplo:
    basic_boxplots(df, "clientes_dataset")
    """

    numeric_columns = df.select_dtypes(include=['number']).columns
    
    # Crear directorios para cada dataset dentro de "visualization/eda_preprocessing"
    output_dir = Path(f"visualization/eda_preprocessing/{dataset_name}")
    output_dir.mkdir(parents=True, exist_ok=True)  # Crear las carpetas si no existen

    for column in numeric_columns:
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df, y=column, palette='coolwarm')
        plt.title(f'Boxplot de {column} en el dataset {dataset_name}')
        plt.ylabel(column)
        plt.tight_layout()
        plt.show()
        
        # Guardar la gráfica en el directorio de salida correspondiente al dataset
        output_path = output_dir / f"{dataset_name}_boxplot_{column}.png"
        plt.savefig(output_path)  # Guardar la gráfica
        plt.close()  # Cerrar la figura para liberar memoria
        
        

def scatter_matrix_plot(df, dataset_name):
    """
    Genera una matriz de dispersión (pairplot) para las columnas numéricas del dataset, permitiendo visualizar 
    las relaciones entre cada par de variables.

    Parámetros:
    df : pandas.DataFrame
        El DataFrame que contiene los datos a analizar.
    dataset_name : str
        El nombre del dataset, utilizado en los mensajes de salida.

    Ejemplo:
    scatter_matrix_plot(df, "clientes_dataset")
    """
    numeric_columns = df.select_dtypes(include=['number']).columns

    # Crear directorios para cada dataset dentro de "visualization/eda_preprocessing"
    output_dir = Path(f"visualization/eda_preprocessing/{dataset_name}")
    output_dir.mkdir(parents=True, exist_ok=True)  # Crear las carpetas si no existen

    if len(numeric_columns) > 1:
        pairplot = sns.pairplot(df[numeric_columns], diag_kind='kde')
        pairplot.fig.suptitle(f'Matriz de Dispersión del dataset {dataset_name}', y=1.02)
        plt.show()
        
        # Guardar la gráfica en el directorio de salida correspondiente al dataset
        output_path = output_dir / f"{dataset_name}_scatter_matrix.png"
        pairplot.savefig(output_path)  # Guardar la gráfica
        plt.close()  # Cerrar la figura para liberar memoria
        
    else:
        print("No hay suficientes columnas numéricas para crear una matriz de dispersión.")


def remove_duplicate_rows(df, dataset_name, subset=None, inplace=False):
    """
    Elimina las filas duplicadas en el dataset, basándose en las columnas especificadas en `subset`.
    Si `inplace=True`, modifica el DataFrame original.

    Parámetros:
    df : pandas.DataFrame
        El DataFrame que contiene los datos a analizar.
    dataset_name : str
        El nombre del dataset, utilizado en los mensajes de salida.
    subset : list, opcional
        Lista de columnas sobre las cuales identificar duplicados. Si no se especifica, se considerarán todas las columnas.
    inplace : bool, opcional (por defecto False)
        Si es True, los duplicados se eliminarán directamente en el DataFrame original. Si es False, se devuelve un nuevo DataFrame sin duplicados.

    Ejemplo:
    remove_duplicate_rows(df, "clientes_dataset", inplace=True)
    """
    print("--------------------------------------------------")
    print(f"Duplicados en el dataset '{dataset_name}':")
    print("--------------------------------------------------")
    duplicate_rows_before = df.duplicated(subset=subset).sum()
    if duplicate_rows_before > 0:
        if inplace:
            df.drop_duplicates(subset=subset, inplace=True)
            print(f"Se eliminaron {duplicate_rows_before} filas duplicadas.")
        else:
            result = df.drop_duplicates(subset=subset)
            print(f"Se eliminaron {duplicate_rows_before} filas duplicadas.")
            return result
    else:
        print("No se encontraron filas duplicadas.")
        return None if inplace else df

# ------------------------------------------------------------
# Ejecuciones Completas
# ------------------------------------------------------------

def run_general_analysis(df, dataset_name):
    """
    Ejecuta un análisis general sobre el dataset, mostrando información básica y ejemplos aleatorios.
    
    Este análisis incluye:
    - Información general del dataset.
    - Cantidad de datos nulos en cada columna.
    - Valores únicos por columna.
    - Muestra aleatoria de filas.

    Parámetros:
    df : pandas.DataFrame
        El DataFrame que contiene los datos a analizar.
    dataset_name : str
        El nombre del dataset, utilizado en los mensajes de salida.

    Ejemplo:
    run_general_analysis(df, "clientes_dataset")
    """
    general_information(df, dataset_name)
    null_data(df, dataset_name)
    unique_values(df, dataset_name)
    random_sample(df, dataset_name)


def descriptive_analysis(df, dataset_name):
    """
    Ejecuta un análisis descriptivo sobre el dataset, mostrando estadísticas y correlaciones entre variables.
    
    Este análisis incluye:
    - Estadísticas descriptivas de las columnas numéricas.
    - Matriz de correlación de las columnas numéricas.
    - Eliminación de filas duplicadas.

    Parámetros:
    df : pandas.DataFrame
        El DataFrame que contiene los datos a analizar.
    dataset_name : str
        El nombre del dataset, utilizado en los mensajes de salida.

    Ejemplo:
    descriptive_analysis(df, "clientes_dataset")
    """
    descript_statis(df, dataset_name)
    corre_matri(df, dataset_name)
    remove_duplicate_rows(df, dataset_name, inplace=True)

def run_visualization_analysis(df, dataset_name):
    """
    Ejecuta un análisis de visualización de los datos, generando gráficos para explorar la distribución y las relaciones, 
    y guarda las gráficas en el directorio especificado.

    Este análisis incluye:
    - Histogramas para columnas numéricas.
    - Diagramas de caja (boxplots) para detectar outliers.
    - Matriz de dispersión (pairplot) para explorar relaciones entre variables numéricas.

    Parámetros:
    df : pandas.DataFrame
        El DataFrame que contiene los datos a analizar.
    dataset_name : str
        El nombre del dataset, utilizado en los mensajes de salida.

    Ejemplo:
    run_visualization_analysis(df, "clientes_dataset")
    """
    basic_histogram(df, dataset_name)
    basic_boxplots(df, dataset_name)
    scatter_matrix_plot(df, dataset_name)

