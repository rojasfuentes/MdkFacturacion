import pandas as pd
import openpyxl


# Abre el archivo de Excel existente
archivo_existente = r"C:\Users\JFROJAS\Desktop\Facturacion\Archive\PRUEBAA.xlsx"
libro_existente = openpyxl.load_workbook(archivo_existente)

# Crea una nueva hoja
nueva_hoja = libro_existente.create_sheet(title="Hoja1")

# Guarda los cambios en el archivo existente
libro_existente.save(archivo_existente)