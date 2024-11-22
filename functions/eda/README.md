# **explora_analysis.py**

## *Descripción*

'explora_analysis.py' contiene una serie de funciones para facilitar el Análisis Exploratorio de Datos (EDA) en diferentes datasets. Las funciones están diseñadas para ser reutilizables y modularizadas, permitiendo realizar análisis generales, estadísticos, de visualización y limpieza de datos de manera eficiente.

Este archivo es una parte clave del pipeline de análisis de datos y se importa en otros scripts principales para ejecutar análisis EDA.

## *Funciones Principales*

A continuación se describen las funciones que proporciona este archivo para el análisis exploratorio de datos:

*   **general_information(df, dataset_name):** Muestra información general del dataset (estructura, tipo de datos, etc.).
*   **null_data(df, dataset_name):** Muestra la cantidad de datos nulos en cada columna del dataset.
*   **random_sample(df, dataset_name, n=30):** Muestra una muestra aleatoria de filas del dataframe.
*   **unique_values(df, dataset_name):** Muestra la cantidad de valores únicos por columna.
*   **descript_statis(df, dataset_name):** Muestra estadísticas descriptivas para las columnas numéricas.
*   **corre_matri(df, dataset_name):** Muestra la matriz de correlación para las columnas numéricas.
*   **basic_histogram(df, dataset_name):** Genera histogramas para las columnas numéricas.
*   **basic_boxplots(df, dataset_name):** Genera diagramas de caja (boxplots) para las columnas numéricas.
*   **scatter_matrix_plot(df, dataset_name):** Genera una matriz de dispersión (pairplot) para las columnas numéricas.
*   **remove_duplicate_rows(df, dataset_name, subset=None, inplace=False):** Elimina filas duplicadas del dataframe.

## *Ejecuciones Completas*

Existen funciones adicionales para ejecutar un análisis completo:

*   **run_general_analysis(df, dataset_name):** Ejecuta un análisis general, mostrando información básica, valores nulos, valores únicos, y una muestra aleatoria.
*   **descriptive_analysis(df, dataset_name):** Ejecuta un análisis descriptivo, mostrando estadísticas descriptivas, matriz de correlación, y eliminando filas duplicadas.
*   **run_visualization_analysis(df, dataset_name):** Ejecuta un análisis de visualización, generando histogramas, boxplots y una matriz de dispersión.

## *Requisitos Previos*

1.  **Python 3.8+ :**
Asegúrate de tener instalada una versión compatible de Python.

2.  **Instalación de dependencias :**
Todas las bibliotecas necesarias están listadas en el archivo requirements.txt.

## *Uso*

Para utilizar las funciones de este archivo, debes importar las funciones necesarias y ejecutarlas sobre un DataFrame cargado.

## *Contribuciones*

Si deseas contribuir al desarrollo de este script o mejorar su funcionalidad, por favor abre un pull request o crea un issue en el repositorio.

## Autor

Este script es parte del proyecto de data science de **Proyecto Final Telecom de Triplenten**. Este proyecto está orientado a la predicción de la tasa de cancelación de clientes de un operador de telecomunicaciones utilizando análisis exploratorio de datos (EDA) y modelos de Machine Learning para mejorar la retención de clientes y optimizar estrategias comerciales.