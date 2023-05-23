from tkinter import filedialog
import pandas as pd


#calidadOrd_path = filedialog.askopenfilename(title="Selecciona 'Calidad de la Orden'", filetypes=(("Archivo Csv", "*.csv"),))
#salidas_path = filedialog.askopenfilename(title="Selecciona 'Orden Cliente'", filetypes=(("Archivo Csv", "*.csv"),))
#entradas_path = filedialog.askopenfilename(title="Selecciona 'ITR SC'", filetypes=(("Archivo Csv", "*.csv"),))
#Columna vacia
vacio= pd.Series([], dtype='float64')

calidadOrd = r'C:\Users\JFROJAS\Desktop\Facturacion\Archive\Calidad de la orden.csv'
salidas_path = r'C:\Users\JFROJAS\Desktop\Facturacion\Archive\Expediciones (Facturacion).csv'
entradas_path = r'C:\Users\JFROJAS\Desktop\Facturacion\Archive\ITR SC (Detallado).csv'

salidas_df = pd.read_csv(salidas_path, sep=',', encoding='latin-1',skiprows=2, low_memory=False)
entradas_df = pd.read_csv(entradas_path, sep=',', low_memory=False)
calidad_df = pd.read_csv(calidadOrd, sep=',' ,low_memory=False)

#Calidad de la orden
calidad_df= calidad_df[['ID_de_envío', 'Nombre_del_cliente', 'Fecha_planificada_de_envío', 'SHIP_TO_STATE']]


#Salidas
nuevosNombres = ['Compañia', 'N. MDTK', 'Referencia', 'Fecha creacion', 'Tipo de Pedido', 'Pallet', 'Cajas de Tarimas', 'Cajas Originales', 'Pzas Cajas Originales', 'Piezas', 'Total piezas', 'Total de Líneas', 'Cajas Totales', 'PesoF', 'Peso KG', 'Volumen M3', 'Tipo', 'Estado', 'Lugar de Entrega', 'Nombre Destino', 'Cód Postal', 'Tipo de Proceso', 'Tipo de proceso Desc', 'Temperatura']
salidas_df.columns = nuevosNombres
salidas_df.drop('Referencia', axis=1, inplace=True)
salidas_df['Referencia'] = salidas_df['N. MDTK'].str.lstrip('0')
salidas_df['Index'] = salidas_df.index

df_combinado = salidas_df.merge(calidad_df, left_on='N. MDTK', right_on='ID_de_envío', how='left')
salidas_df['Cliente'] = df_combinado['Nombre_del_cliente']
salidas_df['Fecha de entrega'] = df_combinado['Fecha_planificada_de_envío']
salidas_df['Estado'] = df_combinado['SHIP_TO_STATE']
salidas_df['Vacio'] = vacio

#Entradas
entradas_df['Index'] = entradas_df.index
entradas_df['Vacio'] = vacio
entradas_df['Inicio_Check_in'] = pd.to_datetime(entradas_df['Inicio_Check_in'], errors='coerce')
entradas_df['Inicio_Check_in'].fillna(value=pd.NaT, inplace=True)
entradas_df['Fecha Inicio R'] = entradas_df['Inicio_Check_in'].dt.date
entradas_df['Hora de Recepción'] = entradas_df['Inicio_Check_in'].dt.time



