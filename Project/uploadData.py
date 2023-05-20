import pandas as pd
from openpyxl import load_workbook

# Importar los dataframes desde los archivos correspondientes
from salidas import drop_df, stock_df, dropEmergencias_df, stockEmergencias_df
from entradas import stock_entradas_df, stockEmergencias_entradas_df, drop_entradas_df, dropEmergencias_entradas_df
from resumenes import resumen_dropdf, resumen_entradasdf, resumen_stockdf

# Ruta y nombre del archivo de Excel
format_path = r'C:\Users\JFROJAS\Desktop\Facturacion\Archive\Libro1.xlsx'

# Crea un objeto de Excel
writer = pd.ExcelWriter(format_path, engine='openpyxl')
writer.book = load_workbook(format_path)

# Entradas
stock_entradas_df.to_excel(writer, sheet_name='ENTRADAS', index=False)

""" stockEmergencias_entradas_df.to_excel(writer, sheet_name='ENTRADAS EMERGENTES', index=False)
resumen_entradasdf.loc[:, 'Unidades'] = resumen_entradasdf.loc[:, 'Unidades'].astype(int)
resumen_entradasdf.to_excel(writer, sheet_name='RESUMEN ENTRADAS', index=False, startrow=stockEmergencias_entradas_df.shape[0]+2)
drop_entradas_df.to_excel(writer, sheet_name='ENTRADAS DROP', index=False)

# Salidas
stock_df.to_excel(writer, sheet_name='SALIDAS STOCK', index=False)
resumen_stockdf.to_excel(writer, sheet_name='RESUMEN SALIDAS', index=False, startrow=stock_df.shape[0]+2)
stockEmergencias_df.to_excel(writer, sheet_name='EMERGENCIAS STOCK', index=False)
dropEmergencias_df.to_excel(writer, sheet_name='EMERGENCIAS DROP', index=False)
drop_df.to_excel(writer, sheet_name='SALIDAS DROP', index=False)
resumen_dropdf.to_excel(writer, sheet_name='SALIDAS DROP', index=False, startrow=drop_df.shape[0]+2) """

# Guardar el archivo de Excel
writer.save()
writer.close()
