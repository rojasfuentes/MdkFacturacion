from loadData import salidas_df
import pandas as pd

columnas_necesarias = ['Index','Referencia', 'N. MDTK','Fecha creacion','Vacio','Vacio','Vacio','Vacio','Tipo de Pedido','Vacio', 'Peso KG', 'Estado', 'Tipo de proceso Desc','Vacio', 'Vacio', 'Vacio', 'Vacio', 'Vacio', 'Tipo','Total de Líneas','Total piezas','Cliente','Vacio','Vacio','Vacio','Fecha de entrega']
nombres_salidas = ['No.','Ref. Cliente','N.MDTK','Fecha Nota','Confirmacion','Fecha de Entrega','Dias de Entrega','Destino','Observaciones','Cajas','Peso','Prov','Tr','U','E','P','R','S','K','Total de líneas','Total de Piezas','Cliente','Repilogada','CA','Lineas Extras a cobrar','Fecha de Entrega']
#DROP
drop_df = salidas_df[salidas_df['Tipo de Pedido'] == 'DROP']
dropEmergencias_df = drop_df[drop_df['Tipo'] == 'EMERGENCIA']
drop_df = drop_df[drop_df['Tipo'] != 'EMERGENCIA']

drop_df = drop_df[columnas_necesarias]
drop_df.columns = nombres_salidas

dropEmergencias_df = dropEmergencias_df[columnas_necesarias]
dropEmergencias_df.columns = nombres_salidas

#STOCK
stock_df = salidas_df[salidas_df['Tipo de Pedido'] != 'DROP']
stockEmergencias_df = stock_df[stock_df['Tipo'] == 'EMERGENCIA']
stock_df = stock_df[stock_df['Tipo'] != 'EMERGENCIA']

stock_df = stock_df[columnas_necesarias]
stock_df.columns = nombres_salidas

stockEmergencias_df = stockEmergencias_df[columnas_necesarias]
stockEmergencias_df.columns = nombres_salidas

#Concentrado de stock
resumen_stockdf = stock_df[['Fecha Nota','Total de Piezas']]
resumen_stockdf = resumen_stockdf.groupby('Fecha Nota')['Total de Piezas'].sum().reset_index()
resumen_stockdf['LIMITE DE PIEZAS (1170)']= 1170
resumen_stockdf['Excedente']= resumen_stockdf['Total de Piezas'] - resumen_stockdf['LIMITE DE PIEZAS (1170)']
stock_df.to_excel(r'C:\Users\JFROJAS\Desktop\Facturacion\Archive\Stock.xlsx', index=False)

total_piezas = resumen_stockdf['Total de Piezas'].sum()
total_nueva_columna = resumen_stockdf['Excedente'].sum()

total_general = pd.DataFrame({'Fecha Nota': ['Total general'],
                           'Total de Piezas': [total_piezas],
                           'LIMITE DE PIEZAS (1170)': [''],
                           'Excedente': [total_nueva_columna]})


resumen_stockdf = resumen_stockdf._append(total_general, ignore_index=True)
print(resumen_stockdf)