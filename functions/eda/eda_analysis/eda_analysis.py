# Módulo: Análisis de EDA - eda_analysis.py
import os, sys
import pandas as pd
from IPython.display import display

def general_information(df, dataset_name):
    """Muestra información general del dataset."""
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
    """Muestra estadísticas descriptivas para columnas numéricas."""
    print("\n--------------------------------------------------")
    print(f"Estadísticas Descriptivas del dataset '{dataset_name}':")
    print("--------------------------------------------------")
    if df.select_dtypes(include=['number']).empty:
        print("No hay columnas numéricas para mostrar estadísticas descriptivas.")
    else:
        display(df.describe())

def corre_matri(df, dataset_name):
    """Muestra la matriz de correlación entre columnas numéricas."""
    print("\n---------------------------------------------")
    print(f"Matriz de Correlación del dataset '{dataset_name}':")
    print("---------------------------------------------")
    numeric_columns = df.select_dtypes(include=['number']).columns
    if len(numeric_columns) < 2:
        print("No hay suficientes columnas numéricas para crear una matriz de correlación.")
    else:
        correlation_matrix = df[numeric_columns].corr()
        display(correlation_matrix)

def categorical_analysis(df, dataset_name):
    """Analiza las variables categóricas del dataset."""
    print("\n-------------------------------------------------")
    print(f"Análisis de variables categóricas en '{dataset_name}':")
    print("-------------------------------------------------")
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    if categorical_columns.empty:
        print("No hay columnas categóricas para analizar.")
    else:
        for col in categorical_columns:
            print(f"\nColumna: {col}")
            print(df[col].value_counts())
            
import pandas as pd
from scipy.stats import zscore

def detect_outliers(df, dataset_name, z_thresh=3):
    """
    Detecta los outliers en las columnas numéricas de un DataFrame utilizando Z-score.
    
    Parámetros:
    df : pandas.DataFrame
        DataFrame con las columnas numéricas.
    dataset_name : str
        Nombre del dataset.
    z_thresh : float
        Umbral de Z-score para considerar un valor como outlier.
    
    Retorna:
    pd.DataFrame
        DataFrame con los valores atípicos.
    """
    # Seleccionar solo las columnas numéricas
    numeric_cols = df.select_dtypes(include=['number'])

    if numeric_cols.empty:
        print("No hay columnas numéricas para detectar outliers.")
        return pd.DataFrame()

    # Eliminar o manejar valores nulos antes de calcular Z-scores
    numeric_cols = numeric_cols.dropna()

    # Calcular los Z-scores
    z_scores = numeric_cols.apply(zscore)

    # Identificar outliers (valores con Z-score mayor que el umbral)
    outliers = (z_scores.abs() > z_thresh)

    # Contar el número de outliers por columna
    outliers_count_per_col = outliers.sum()

    # Mostrar los resultados
    outlier_count = outliers.sum().sum()  # Total de outliers
    print("\n-------------------------------------------------------")
    print(f"Detección de valores atípicos en '{dataset_name}' (Z-Score):")
    print("-------------------------------------------------------")
    
    if outlier_count > 0:
        print(f"Se detectaron {outlier_count} outliers en el dataset.")
        print("Número de outliers por columna:")
        print(outliers_count_per_col)
        outlier_rows = df[outliers.any(axis=1)]
        display(outlier_rows)
    else:
        print("No se detectaron outliers.")
    
    return outliers
