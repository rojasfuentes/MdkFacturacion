import pandas as pd
import numpy as np

# Abre el archivo de Excel existente
ocupacion_path = r'C:\Users\JFROJAS\Desktop\Facturacion\Archive\Nueva carpeta\OCUPACIÓN 04.2023.xlsx'
df_ocupacion = pd.read_excel(ocupacion_path, header=0, skiprows= 2 )
df_ocupacionT = df_ocupacion.T
#eliminar el encabezado
#df_ocupacionT = df_ocupacionT.iloc[1:]
#usar segunda fila como encabezado
df_ocupacionT.columns = df_ocupacionT.iloc[0]

total_huecosplts = df_ocupacionT['RACKS 60CM'].values[1] + df_ocupacionT['Racks 1,20'].values[1] + df_ocupacionT['Racks 1,80 '].values[1] + df_ocupacionT['Instrumentos'].values[1] + df_ocupacionT['Embalaje'].values[1] + df_ocupacionT['TRANSITO '].values[1]
total_modulosest = df_ocupacionT['Temp. Congelación -15° / -20°C'].values[1] + df_ocupacionT ['Temp. Congelación -70°C'].values[1]


print(df_ocupacion)
