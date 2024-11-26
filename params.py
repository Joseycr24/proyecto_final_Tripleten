#Modulo params.py
# Librerias ---------------------------------------- 
import platform
from functions.formatos_fecha.crear_formatos_fecha import *


# Sistema operativo
sistema_operativo = platform.system()

# Entrenamiento o ejecución
bool_entrtenamiento = False  # Cambiar a True si deseas activar el modo entrenamiento

# Fecha por defecto (formato YYYYMM)
periodo_YYYYMM_por_defecto = "202411"
periodo_YYYYMM, anio_mes_dia_formato_ini_date, anio_mes_dia_formato_ini, anio_mes_dia_formato_fin = crear_formatos_fecha(periodo_YYYYMM_por_defecto)


