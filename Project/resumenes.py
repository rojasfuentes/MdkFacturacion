from salidas import stock_df, drop_df
from entradas import drop_entradas_df
import pandas as pd

#Salidas
resumen_stockdf = stock_df[['Fecha Nota','Total de Piezas']]
resumen_stockdf = resumen_stockdf.groupby('Fecha Nota')['Total de Piezas'].sum().reset_index()
resumen_stockdf['LIMITE DE PIEZAS (1170)']= 1170
resumen_stockdf['Excedente']= resumen_stockdf['Total de Piezas'] - resumen_stockdf['LIMITE DE PIEZAS (1170)']
#stock_df.to_excel(r'C:\Users\JFROJAS\Desktop\Facturacion\Archive\Stock.xlsx', index=False)

total_piezasStock = resumen_stockdf['Total de Piezas'].sum()
total_nuevaColumna_stock = resumen_stockdf['Excedente'].sum()

total_general = pd.DataFrame({'Fecha Nota': ['Total general'],
                           'Total de Piezas': [total_piezasStock],
                           'LIMITE DE PIEZAS (1170)': [''],
                           'Excedente': [total_nuevaColumna_stock]})
resumen_stockdf = resumen_stockdf._append(total_general, ignore_index=True)


resumen_dropdf = drop_df[['Fecha Nota','Total de Piezas']]
resumen_dropdf = resumen_dropdf.groupby('Fecha Nota')['Total de Piezas'].sum().reset_index()
resumen_dropdf['LIMITE DE PIEZAS (1170)']= 1170
resumen_dropdf['Excedente']= resumen_dropdf['Total de Piezas'] - resumen_dropdf['LIMITE DE PIEZAS (1170)']


total_piezasDrop = resumen_dropdf['Total de Piezas'].sum()
total_nuevaColumna_Drop = resumen_dropdf['Excedente'].sum()

total_general_drop = pd.DataFrame({'Fecha Nota': ['Total general'],
                            'Total de Piezas': [total_piezasDrop],
                            'LIMITE DE PIEZAS (1170)': [''],
                            'Excedente': [total_nuevaColumna_Drop]})
resumen_dropdf = resumen_dropdf._append(total_general_drop, ignore_index=True)


#Entradas
resumen_entradasdf = drop_entradas_df[['Fecha de Inicio de Recepción','Unidades']]
resumen_entradasdf.loc[:, 'Unidades'] = resumen_entradasdf['Unidades'].astype(int)
resumen_entradasdf = resumen_entradasdf.groupby('Fecha de Inicio de Recepción')['Unidades'].sum().reset_index()
resumen_entradasdf = resumen_entradasdf.dropna()
resumen_entradasdf['LIMITE DE PIEZAS (1170)']= 1170
resumen_entradasdf['Excedente']= resumen_entradasdf['Unidades'] - resumen_entradasdf['LIMITE DE PIEZAS (1170)']

total_piezasEntradas = resumen_entradasdf['Unidades'].sum()
total_nuevaColumna_Entradas = resumen_entradasdf['Excedente'].sum()

total_general_entradas = pd.DataFrame({'Fecha de Inicio de Recepción': ['Total general'],
                            'Unidades': [total_piezasEntradas],
                            'LIMITE DE PIEZAS (1170)': [''],
                            'Excedente': [total_nuevaColumna_Entradas]})

resumen_entradasdf = resumen_entradasdf._append(total_general_entradas, ignore_index=True)

#print(resumen_stockdf)
#print(resumen_dropdf)
#print(resumen_entradasdf)

