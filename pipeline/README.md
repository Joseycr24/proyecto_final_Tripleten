# **Pipeline de Análisis Exploratorio de Datos (EDA)**

Este repositorio contiene el pipeline de Análisis Exploratorio de Datos (EDA) para el proyecto de predicción de la tasa de cancelación de clientes de un operador de telecomunicaciones. El pipeline coordina y ejecuta varios pasos del proceso EDA para preparar los datos antes de proceder con otros análisis o la construcción de modelos predictivos.

## *Descripción*

Este script automatiza el flujo de trabajo para realizar un análisis exploratorio de datos (EDA) en el proyecto. El propósito principal es ejecutar los pasos iniciales de procesamiento y análisis de los datos para facilitar la posterior construcción de modelos de predicción.

Los pasos incluidos en este pipeline son:

*   **Preprocesamiento de datos:** Ejecución de un script externo para realizar un preprocesamiento básico de los datos.
*   **Análisis descriptivo:** Análisis estadístico de las variables numéricas y categóricas.
*   **Visualización de datos:** Generación de gráficos para entender mejor las relaciones entre las variables y la distribución de los datos.

## Instalación

Para usar este pipeline, asegúrate de tener Python instalado en tu entorno y las bibliotecas necesarias.

### *Requisitos Previos*

1.  **Python 3.8+ :**
Asegúrate de tener instalada una versión compatible de Python.

2.  **Instalación de dependencias :**
Todas las bibliotecas necesarias están listadas en el archivo requirements.txt.

## Uso

*   **Ejecutar el pipeline de EDA:** Para ejecutar el análisis exploratorio de datos, solo necesitas ejecutar el script principal 'main.py'. Esto ejecutará el script de preprocesamiento epp00.py, que se encarga de limpiar y preparar los datos. A continuación, el pipeline continuará con el análisis descriptivo y la visualización de los datos.
*   **Personalizar el análisis:** Si deseas agregar más pasos de preprocesamiento o análisis en el futuro, puedes modificar los scripts dentro de la carpeta /functions/eda/ y /eda/preprocessing/.

## *Ejecución del Pipeline*

Para ejecutar el análisis exploratorio de datos, solo tienes que ejecutar el script principal 'main.py':

Este script realizará las siguientes acciones:

1.  Ejecutará el archivo de preprocesamiento (epp00.py).
2.  Ejecutará el análisis general sobre los datos.
3.  Ejecutará el análisis descriptivo y las visualizaciones.

## *Personalización*

Puedes modificar el flujo de trabajo agregando más pasos de procesamiento o análisis según las necesidades de tu proyecto. Por ejemplo, puedes agregar pasos adicionales como la limpieza de datos, transformaciones adicionales o el entrenamiento de modelos de machine learning.

## *Contribuciones*

Si deseas contribuir al desarrollo de este script o mejorar su funcionalidad, por favor abre un pull request o crea un issue en el repositorio.

## Autor

Este script es parte del proyecto de data science de **Proyecto Final Telecom de Triplenten**. Este proyecto está orientado a la predicción de la tasa de cancelación de clientes de un operador de telecomunicaciones utilizando análisis exploratorio de datos (EDA) y modelos de Machine Learning para mejorar la retención de clientes y optimizar estrategias comerciales.