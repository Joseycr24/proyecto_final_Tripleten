#Modulo crear_formatos_fecha.py
import calendar
from datetime import datetime

import calendar
from datetime import datetime

def crear_formatos_fecha(periodo_YYYYMM):
    """
    Crea formatos de fecha a partir de un periodo en formato YYYYMM.

    Parameters:
    - periodo_YYYYMM (str): Periodo en formato YYYYMM.

    Returns:
    Tuple: Contiene el periodo original, fecha de inicio como objeto datetime,
           y las fechas de inicio y fin en formato 'YYYY-MM-DD'.
    """
    try:
        # Validar formato del periodo
        if len(periodo_YYYYMM) != 6 or not periodo_YYYYMM.isdigit():
            raise ValueError("El periodo debe estar en formato 'YYYYMM'.")

        # Extraer año y mes
        anio = int(periodo_YYYYMM[:4])
        mes = int(periodo_YYYYMM[4:])

        # Fecha de inicio
        dia_inicio = 1
        anio_mes_dia_formato_ini_date = datetime(anio, mes, dia_inicio)
        anio_mes_dia_formato_ini = anio_mes_dia_formato_ini_date.strftime('%Y-%m-%d')

        # Fecha de fin
        dia_fin = calendar.monthrange(anio, mes)[1]
        anio_mes_dia_formato_fin_date = datetime(anio, mes, dia_fin)
        anio_mes_dia_formato_fin = anio_mes_dia_formato_fin_date.strftime('%Y-%m-%d')

        return (periodo_YYYYMM, anio_mes_dia_formato_ini_date, anio_mes_dia_formato_ini, anio_mes_dia_formato_fin)
    
    except ValueError as e:
        print(f"Error al procesar el periodo: {e}")
        raise
