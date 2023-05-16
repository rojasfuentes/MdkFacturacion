from loadData import df

nombres_salidas = ['No.','Ref. Cliente','N.MDTK','Fecha Nota','Confirmacion','Fecha de Entrega','Dias de Entrega','Destino','Observaciones','Cajas','Peso','Prov','Tr','U','E','P','R','S','K','Total de líneas','Total de Piezas','Cliente','Repilogada','CA','Lineas Extras a cobrar','Fecha de Entrega']
#DROP
drop_df = df[df['Tipo de Pedido'] == 'DROP']
dropEmergencias_df = drop_df[drop_df['Tipo'] == 'EMERGENCIA']

drop_df = drop_df[['Index','Referencia', 'N. MDTK','Fecha creacion','Vacio','Vacio','Vacio','Vacio','Tipo de Pedido','Vacio', 'Peso KG', 'Estado', 'Tipo de proceso Desc','Vacio', 'Vacio', 'Vacio', 'Vacio', 'Vacio', 'Tipo','Total de Líneas','Total piezas','Cliente','Vacio','Vacio','Vacio','Fecha de entrega']]
drop_df.columns = nombres_salidas

dropEmergencias_df = dropEmergencias_df[['Index','Referencia', 'N. MDTK','Fecha creacion','Vacio','Vacio','Vacio','Vacio','Tipo de Pedido','Vacio', 'Peso KG', 'Estado', 'Tipo de proceso Desc','Vacio', 'Vacio', 'Vacio', 'Vacio', 'Vacio', 'Tipo','Total de Líneas','Total piezas','Cliente','Vacio','Vacio','Vacio','Fecha de entrega']]
dropEmergencias_df.columns = nombres_salidas

#STOCK
stock_df = df[df['Tipo de Pedido'] != 'DROP']
stockEmergencias_df = stock_df[stock_df['Tipo'] == 'EMERGENCIA']

stock_df = stock_df[['Index','Referencia', 'N. MDTK','Fecha creacion','Vacio','Vacio','Vacio','Vacio','Tipo de Pedido','Vacio', 'Peso KG', 'Estado', 'Tipo de proceso Desc','Vacio', 'Vacio', 'Vacio', 'Vacio', 'Vacio', 'Tipo','Total de Líneas','Total piezas','Cliente','Vacio','Vacio','Vacio','Fecha de entrega']]
stock_df.columns = nombres_salidas

stockEmergencias_df = stockEmergencias_df[['Index','Referencia', 'N. MDTK','Fecha creacion','Vacio','Vacio','Vacio','Vacio','Tipo de Pedido','Vacio', 'Peso KG', 'Estado', 'Tipo de proceso Desc','Vacio', 'Vacio', 'Vacio', 'Vacio', 'Vacio', 'Tipo','Total de Líneas','Total piezas','Cliente','Vacio','Vacio','Vacio','Fecha de entrega']]
stockEmergencias_df.columns = nombres_salidas

stock_df.to_excel(r'C:\Users\JFROJAS\Desktop\Facturacion\Archive\Stock.xlsx', index=False)
print(stock_df.head(5))