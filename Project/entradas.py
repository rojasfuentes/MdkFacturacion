from loadData import entradas_df

drop_entradas_df = entradas_df[entradas_df['Documento'].str.startswith("11")]
stock_entradas_df = entradas_df[~entradas_df['Documento'].str.startswith("11")]

dropEmergencias_df = drop_entradas_df[drop_entradas_df['erp'] != 'Sin Dato']
drop_entradas_df = drop_entradas_df[drop_entradas_df['erp'] == 'Sin Dato']

stockEmergencias_df = stock_entradas_df[stock_entradas_df['erp'] != 'Sin Dato']
stock_entradas_df = stock_entradas_df[stock_entradas_df['erp'] == 'Sin Dato']

nombres_entradas = ['No','No. De Protocolo','Tipo Entrada','Fecha de Protocolo','Ref. Cliente','Fecha de Orden de Compra','Lineas','Unidades','Piezas Etiquetadas <500 kg','Piezas Etiquetadas >500 kg','Fecha de Inicio de Recepción','Hora de Recepción','Fecha de Inicio de Entrada','Fecha de Confirmación de Entrada','Hora de Confirmación de Entrada','Días Entrada MDTK','Observaciones','CA']
columnas_necesarias = ['Index','Documento','RECEIPT_ID_TYPE','Fecha_Etiqueta','Pedido_ERP','Vacio','Lineas2','Cantidad_Recibida','Vacio','Vacio','Fecha Inicio R','Inicio_Check_in','Hora de Recepción','FECHA_CERRADO','FECHA_CERRADO', 'Vacio','Vacio','Vacio']

stock_entradas_df = stock_entradas_df[columnas_necesarias]
stock_entradas_df.columns = nombres_entradas
stockEmergencias_df = stockEmergencias_df[columnas_necesarias]
stockEmergencias_df.columns = nombres_entradas

drop_entradas_df = drop_entradas_df[columnas_necesarias]
drop_entradas_df.columns = nombres_entradas
dropEmergencias_df = dropEmergencias_df[columnas_necesarias]
dropEmergencias_df.columns = nombres_entradas

print(stock_entradas_df.head(5))
print(stockEmergencias_df.head(5))
print(drop_entradas_df.head(5))
print(dropEmergencias_df.head(5))
