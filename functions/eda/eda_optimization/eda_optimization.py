# Módulo: Optimización del EDA - eda_optimization.py
import os, sys
import numpy as np
import pandas as pd
sys.path.append(os.getcwd())

def optimize_memory(df, dataset_name, verbose=True):
    """
    Optimiza el uso de memoria de un DataFrame convirtiendo columnas
    a tipos más adecuados (int, float, categoría).

    Parámetros:
    df : pandas.DataFrame
        DataFrame a optimizar.
    dataset_name : str
        Nombre del dataset para mensajes de salida.
    verbose : bool
        Si es True, muestra el uso de memoria antes y después de la optimización.

    Retorno:
    pd.DataFrame
        DataFrame optimizado en memoria.
    """
    print(f"\n-------------------------------------------")
    print(f"Optimización de memoria para el dataset '{dataset_name}':")
    print(f"-------------------------------------------")
    start_mem = df.memory_usage(deep=True).sum() / 1024**2
    if verbose:
        print(f"Memoria inicial del DataFrame: {start_mem:.2f} MB")
    
    for col in df.columns:
        col_type = df[col].dtypes
        
        if col_type == 'object':
            num_unique = df[col].nunique()
            num_total = len(df[col])
            if num_unique / num_total < 0.5:
                df[col] = df[col].astype('category')
        
        elif col_type == 'float64':
            df[col] = df[col].astype('float32')
        
        elif col_type == 'int64':
            if df[col].min() >= np.iinfo('int8').min and df[col].max() <= np.iinfo('int8').max:
                df[col] = df[col].astype('int8')
            elif df[col].min() >= np.iinfo('int16').min and df[col].max() <= np.iinfo('int16').max:
                df[col] = df[col].astype('int16')
            elif df[col].min() >= np.iinfo('int32').min and df[col].max() <= np.iinfo('int32').max:
                df[col] = df[col].astype('int32')
    
    end_mem = df.memory_usage(deep=True).sum() / 1024**2
    if verbose:
        print(f"Memoria optimizada del DataFrame: {end_mem:.2f} MB")
        print(f"Reducción de memoria: {100 * (start_mem - end_mem) / start_mem:.1f}%")
    
    return df