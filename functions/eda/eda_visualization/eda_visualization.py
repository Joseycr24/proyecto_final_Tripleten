# Módulo: Visualización del EDA - eda_visualization.py
import os, sys
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
from itertools import combinations
sys.path.append(os.getcwd())

def plot_correlation_heatmap(df, dataset_name):
    """
    Genera un mapa de calor (heatmap) de la matriz de correlación entre las columnas numéricas.

    Args:
        df (pd.DataFrame): El DataFrame que contiene los datos.
        dataset_name (str): El nombre del dataset, utilizado en el título del gráfico.

    Returns:
        None
    """
    # Seleccionar solo las columnas numéricas
    numeric_columns = df.select_dtypes(include=['number']).columns

    if len(numeric_columns) > 1:
        # Calcular la matriz de correlación
        corr_matrix = df[numeric_columns].corr()

        # Crear el gráfico de correlación (heatmap)
        plt.figure(figsize=(12, 8))  # Ajusta el tamaño según sea necesario
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, vmin=-1, vmax=1)

        # Título del gráfico
        plt.title(f'Matriz de Correlación - {dataset_name}')
        
        # Mostrar el gráfico
        plt.show()

    else:
        print("No hay suficientes columnas numéricas para crear una matriz de correlación.")

def interactive_histogram(df, dataset_name):
    """Genera histogramas para columnas numéricas sin abrir el navegador."""
    numeric_columns = df.select_dtypes(include=['number']).columns
    for column in numeric_columns:
        plt.figure(figsize=(10, 6))
        plt.hist(df[column], bins=30, edgecolor='black')
        plt.title(f'Histograma de {column} - {dataset_name}')
        plt.xlabel(column)
        plt.ylabel('Frecuencia')
        plt.show() 

def interactive_boxplots(df, dataset_name):
    """Genera diagramas de caja para columnas numéricas sin abrir el navegador."""
    numeric_columns = df.select_dtypes(include=['number']).columns
    for column in numeric_columns:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=df[column])
        plt.title(f'Boxplot de {column} - {dataset_name}')
        plt.show() 
                
def plot_scatter(df, dataset_name):
    """Genera gráficos de dispersión interactivos entre columnas numéricas."""
    # Validar las entradas
    if not isinstance(df, pd.DataFrame):
        raise ValueError("El argumento 'df' debe ser un DataFrame de pandas.")
    if not isinstance(dataset_name, str) or not dataset_name.strip():
        raise ValueError("El argumento 'dataset_name' debe ser un string no vacío.")
    
    # Seleccionar columnas numéricas
    numeric_columns = df.select_dtypes(include=['number']).columns

    # Validar que haya al menos dos columnas numéricas
    if len(numeric_columns) < 2:
        print(f"El dataset '{dataset_name}' no tiene suficientes columnas numéricas para gráficos de dispersión.")
        return  # Salir de la función

    # Crear directorio para guardar gráficos
    output_dir = Path(f"visualization/eda_preprocessing/{dataset_name}")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generar gráficos de dispersión entre todas las combinaciones de columnas numéricas
    for col_x, col_y in combinations(numeric_columns, 2):  # Aquí usamos combinations
        fig = px.scatter(df, x=col_x, y=col_y,  title=f'Dispersión entre {col_x} y {col_y} - {dataset_name}')
        fig.show()
        fig.write_html(output_dir / f"{dataset_name}_scatter_{col_x}_{col_y}.html")


def plot_categorical_vs_numerical(df, cat_col, num_col, dataset_name):
    plt.figure(figsize=(10, 6))
    plt.title(f'{dataset_name} - {cat_col} vs {num_col}')

    sns.boxplot(x=cat_col, y=num_col, data=df)
    
    plt.show()

def plot_bar_chart(df, dataset_name):
    """
    Genera un gráfico de barras interactivo con frecuencias absolutas para variables categóricas."""
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    for column in categorical_columns:
        # Obtener conteo de valores y resetear índice
        value_counts = df[column].value_counts().reset_index()
        value_counts.columns = [column, "count"]  

        fig = px.bar(value_counts, x=column, y="count",
                     title=f'Frecuencia de {column} en {dataset_name}')
        fig.update_layout(xaxis_title=column, yaxis_title="Frecuencia")
        fig.show()

def interactive_scatter_matrix_plot(df, dataset_name):
    """
    Genera una matriz de dispersión interactiva para las columnas numéricas del dataset, permitiendo visualizar 
    las relaciones entre cada par de variables.

    Parámetros:
    df : pandas.DataFrame
        El DataFrame que contiene los datos a analizar.
    dataset_name : str
        El nombre del dataset, utilizado en los mensajes de salida.
    """
    numeric_columns = df.select_dtypes(include=['number']).columns

    # Crear directorios para cada dataset dentro de "visualization/eda_preprocessing"
    output_dir = Path(f"visualization/eda_preprocessing/{dataset_name}")
    output_dir.mkdir(parents=True, exist_ok=True)  # Crear las carpetas si no existen

    if len(numeric_columns) > 1:
        fig = px.scatter_matrix(df, dimensions=numeric_columns, title=f'Matriz de Dispersión del dataset {dataset_name}')
        fig.update_layout(width=1000, height=800)
        
        # Mostrar la gráfica de forma interactiva
        fig.show()
        
        # Guardar la gráfica como archivo HTML para interactividad
        output_path = output_dir / f"{dataset_name}_scatter_matrix.html"
        fig.write_html(output_path)  # Guardar la gráfica interactiva
    else:
        print("No hay suficientes columnas numéricas para crear una matriz de dispersión.")
