import os, sys
from functions.eda.eda_analysis import eda_analysis
from functions.eda.eda_visualization import eda_visualization
from functions.eda.eda_optimization.eda_optimization import optimize_memory
sys.path.append(os.getcwd())

def run_eda_analysis(df, dataset_name, periodo=None):
    eda_analysis.general_information(df, dataset_name)
    eda_analysis.null_data(df, dataset_name)
    eda_analysis.random_sample(df, dataset_name)
    eda_analysis.unique_values(df, dataset_name)
    eda_analysis.descript_statis(df, dataset_name)
    eda_analysis.corre_matri(df, dataset_name)
    eda_analysis.categorical_analysis(df, dataset_name)
    eda_analysis.detect_outliers(df, dataset_name)

def run_visualization(df, dataset_name, periodo=None):
    # Llamadas para otros gráficos interactivos
    eda_visualization.interactive_histogram(df, dataset_name)
    eda_visualization.interactive_boxplots(df, dataset_name)
    eda_visualization.plot_scatter(df, dataset_name)
    
    # Gráficos categórico-numéricos automáticos
    print("\nGenerando gráficos categórico-numéricos...")
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    numerical_columns = df.select_dtypes(include=['number']).columns

    for cat_col in categorical_columns:
        for num_col in numerical_columns:
            print(f"Generando gráfico para '{cat_col}' vs '{num_col}'...")
            # Asegúrate de pasar 'dataset_name' también
            eda_visualization.plot_categorical_vs_numerical(df, cat_col, num_col, dataset_name)

def run_pipeline(dataset, dataset_name="DatasetName", periodo=None):
    # **Optimización de memoria antes de cualquier análisis**
    print("\nPaso 1: Optimización de memoria.")
    optimized_df = optimize_memory(dataset, dataset_name)

    # **Análisis exploratorio de datos (EDA)**
    print("\nPaso 2: Análisis exploratorio de datos (EDA).")
    run_eda_analysis(optimized_df, dataset_name, periodo)  # Pasar 'periodo' si es necesario

    # **Visualizaciones**
    print("\nPaso 3: Generación de visualizaciones.")
    run_visualization(optimized_df, dataset_name, periodo) 
