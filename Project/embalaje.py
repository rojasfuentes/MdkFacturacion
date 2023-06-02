import pandas as pd
import numpy as np

# Abre el archivo de Excel existente
embalaje_path = r"C:\Users\JFROJAS\Desktop\Facturacion\Archive\Nueva carpeta\Embalaje Drops (8).xlsx"

df_embalaje = pd.read_excel(embalaje_path, sheet_name='Embalaje Drops', skiprows= 6)

df_embalaje.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 19'], axis=1, inplace=True)

# solo las columnas numéricas
numeric_columns = df_embalaje.select_dtypes(include=[np.number])
column_totals = numeric_columns.sum()
# Nueva fila
totals_row = pd.DataFrame(column_totals).T

totals_row['Compañía'] = ''
totals_row['Pedido'] = ''
totals_row['Fecha Pedido'] = 'Total:'

# Agrega fila
df_embalaje = pd.concat([df_embalaje, totals_row], ignore_index=True)

h_siemmens = totals_row['Hielera Siemens Chica'].values[0] + totals_row['Hielera Siemens Mediana'].values[0]
h_medistik = totals_row['H11'].values[0] + totals_row['H14'].values[0] + totals_row['H17'].values[0] + totals_row['H19'].values[0] + totals_row['H26'].values[0]
h_60hrs = totals_row['BMBCH3'].values[0] + totals_row['BMBCH4'].values[0]
cj_medistik = totals_row['BMBC1'].values[0] + totals_row['BMBC3'].values[0] + totals_row['BMBC4'].values[0] + totals_row['BMBC6'].values[0] + totals_row['BMBC9'].values[0] + totals_row['BMBC11'].values[0]
geles = totals_row['Hielera Siemens Grande Conge'].values[0]
hielo_seco = totals_row['Hielo Seco'].values[0]
total_cjHmedistik = h_siemmens + h_medistik + h_60hrs + cj_medistik

dataResumen = {
    'Hielera Siemens': [h_siemmens],
    'Hielera Medistik': [h_medistik],
    'Hielera 60hrs': [h_60hrs],
    'Caja Medistik': [cj_medistik],
    'Geles': [geles],
    'Hielo Seco': [hielo_seco],
    'Total Caja / Hielera Medistik': [total_cjHmedistik]
}

df_resumenEmbalaje = pd.DataFrame(dataResumen)
#Transponer el dataframe
df_resumenEmbalaje = df_resumenEmbalaje.T
