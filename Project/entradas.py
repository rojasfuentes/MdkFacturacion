import pandas as pd
from loadData import entradas_df

drop_entradas_df = entradas_df[entradas_df['Documento'].str.startswith("11")]
stock_entradas_df = entradas_df[~entradas_df['Documento'].str.startswith("11")]


dropEmergencias_entradas_df = drop_entradas_df[drop_entradas_df['erp'] != 'Sin Dato']
drop_entradas_df = drop_entradas_df[drop_entradas_df['erp'] == 'Sin Dato']

stockEmergencias_entradas_df = stock_entradas_df[stock_entradas_df['erp'] != 'Sin Dato']
stock_entradas_df = stock_entradas_df[stock_entradas_df['erp'] == 'Sin Dato']

nombres_entradas = ['No','No. De Protocolo','Tipo Entrada','Fecha de Protocolo','Ref. Cliente','Fecha de Orden de Compra','Lineas','Unidades','Piezas Etiquetadas <500 kg','Piezas Etiquetadas >500 kg','Fecha de Inicio de Recepción','Hora de Recepción','Fecha de Inicio de Entrada','Fecha de Confirmación de Entrada','Hora de Confirmación de Entrada','Días Entrada MDTK','Observaciones','CA']
columnas_necesarias = ['Index','Documento','RECEIPT_ID_TYPE','Fecha_Etiqueta','Pedido_ERP','Vacio','Lineas2','Cantidad_Recibida','Vacio','Vacio','Fecha Inicio R','Inicio_Check_in','Hora de Recepción','FECHA_CERRADO','FECHA_CERRADO', 'Vacio','Vacio','Vacio']

stock_entradas_df = stock_entradas_df[columnas_necesarias]
stock_entradas_df.columns = nombres_entradas
stockEmergencias_entradas_df = stockEmergencias_entradas_df[columnas_necesarias]
stockEmergencias_entradas_df.columns = nombres_entradas

drop_entradas_df = drop_entradas_df[columnas_necesarias]
drop_entradas_df.columns = nombres_entradas
dropEmergencias_entradas_df = dropEmergencias_entradas_df[columnas_necesarias]
dropEmergencias_entradas_df.columns = nombres_entradas

stock_entradas_df['Unidades'] = stock_entradas_df['Unidades'].str.replace(',', '').astype(int)
stockEmergencias_entradas_df['Unidades'] = stockEmergencias_entradas_df['Unidades'].str.replace(',', '').astype(int)


numEle_stockEntradas = stock_entradas_df['No'].count()
sumLineas_stockEntradas = stock_entradas_df['Lineas'].sum()
sumUnidades_stockEntradas = stock_entradas_df['Unidades'].sum()

sumUnidades_stockEmergenciasEntradas = stockEmergencias_entradas_df['Unidades'].sum()


columns_dfFS = pd.DataFrame([stock_entradas_df.columns], columns=stock_entradas_df.columns)
new_row = pd.DataFrame([[numEle_stockEntradas, '', '', '', '', '', sumLineas_stockEntradas, sumUnidades_stockEntradas, '', '', '', '', '', '', '', '', '', '']], columns=stock_entradas_df.columns)
final_stock_entradas_df = pd.concat([new_row, stock_entradas_df, columns_dfFS], ignore_index=True)

columns_dfFSE = pd.DataFrame([stockEmergencias_entradas_df.columns], columns=stockEmergencias_entradas_df.columns)
new_rowdfSE = pd.DataFrame([[stockEmergencias_entradas_df['No'].count(), '', '', '', '', '', stockEmergencias_entradas_df['Lineas'].sum(), sumUnidades_stockEmergenciasEntradas, '', '', '', '', '', '', '', '', '', '']], columns=stockEmergencias_entradas_df.columns)
final_stockEmergencias_entradas_df = pd.concat([new_rowdfSE, stockEmergencias_entradas_df, columns_dfFSE], ignore_index=True)

columns_dfFD = pd.DataFrame([drop_entradas_df.columns], columns=drop_entradas_df.columns)
new_rowdfD = pd.DataFrame([[drop_entradas_df['No'].count(), '', '', '', '', '', drop_entradas_df['Lineas'].sum(), drop_entradas_df['Unidades'].sum(), '', '', '', '', '', '', '', '', '', '']], columns=drop_entradas_df.columns)
final_drop_entradas_df = pd.concat([new_rowdfD, drop_entradas_df, columns_dfFD], ignore_index=True)

columns_dfFDE = pd.DataFrame([dropEmergencias_entradas_df.columns], columns=dropEmergencias_entradas_df.columns)
new_rowdfDE = pd.DataFrame([[dropEmergencias_entradas_df['No'].count(), '', '', '', '', '', dropEmergencias_entradas_df['Lineas'].sum(), dropEmergencias_entradas_df['Unidades'].sum(), '', '', '', '', '', '', '', '', '', '']], columns=dropEmergencias_entradas_df.columns)
final_dropEmergencias_entradas_df = pd.concat([new_rowdfDE, dropEmergencias_entradas_df, columns_dfFDE], ignore_index=True)




# Imprimir el dataframe resultante
#print(final_stock_entradas_df)
#print(final_stockEmergencias_entradas_df)
print(final_dropEmergencias_entradas_df)