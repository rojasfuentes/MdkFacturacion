import pandas as pd

import pandas as pd

def crear_dataframe(columna, nombres):
    df = pd.DataFrame(columns=[columna]+ nombres) 
    return df

nombres = ['Concepto', 'Tarifa (MXP)', 'Volúmenes contratados', 'Cantidad real', 'Cantidad a cobrar', 'Monto']

df1 = crear_dataframe("FMG" , nombres)
df2 = crear_dataframe("RECEPCIÓN Y ENTRADAS DE PRODUCTO" , nombres)
df3 = crear_dataframe("ETIQUETADO" , nombres)
df4 = crear_dataframe("OCUPACIÓN" , nombres)
df5 = crear_dataframe("MANIPULACIÓN DE NOTA ELECTRÓNICA" , nombres)
df8 = crear_dataframe("RE-ENVÍOS" , nombres)
df9 = crear_dataframe("TRANSPORTE" , nombres)
df10 = crear_dataframe("EMBALAJE" , nombres)
df11 = crear_dataframe("VARIOS" , nombres)
dfcd = crear_dataframe("MANIPULACIÓN" , nombres)

# Resto del código para llenar los DataFrames y trabajar con ellos...



df1.loc[len(df1)] = ['Facturación Mínima Garantizada', 'Por mes',' 2258475.70', '', '1','1','2094672.32']
df2.loc[len(df2)] = ['a) Piezas de entrada  en 48hrs','Por pieza','29.93','27,462','X','11828','354,012.04']
df2.loc[len(df2)] = ['b) Piezas de entrada en 24hrs','Por pieza','41.64','5,052','X','0','$']
df3.loc[len(df3)] = ['a) Etiquetado dentro de 48hrs','Por pieza','1.32',' 27,462','X','5581','7366.92']
df3.loc[len(df3)] = ['b) Etiquetado dentro de 24hrs','Por pieza','1.97','','X','10','$19.70']
df4.loc[len(df4)] = ['a) Hueco pallet a temperatura ambiente (1.0 x 1.2 x 1.2 m)','Por hueco pallet','362.33','811','X','54','19565.82']
df4.loc[len(df4)] = ['b) Módulo de estantería ambiente (1.25 x 0.50 x 2.40 m)','Por modulo','418.77','80','X','0','$-']
df4.loc[len(df4)] = ['c) Módulo de estantería +2 - +8 °C (1.25 x 0.50 x 2.40 m)','Por módulo','1272.78','127','X','30','38183.40']
df4.loc[len(df4)] = ['d) Hueco pallet +2 - +8 °C (1.25 x 0.50 x 2.40 m)','Por hueco pallet','1171.27','84','X','0','$']
df4.loc[len(df4)] = ['e) Módulo de estantería -15 - -20 °C (1.25 x 0.50 x 2.40 m)','Por módulo','1931.54','12','X','0','$']
df5.loc[len(df5)] = ['a) Piezas de salida','Por pieza','22.60','25996','X','3567','$80614.2']
df5.loc[len(df5)] = ['c) Piezas de salida para surtir en  el momento','Por pieza','33.9','','X','16','$542.4']
df8.loc[len(df8)] = ['a) Re-envíos de producto','Por concepto','20% adicional','-','X','1','$27.12']
df9.loc[len(df9)] = ['a) Transporte','Por embarque','Ver tablas','','X','X','$-']
df10.loc[len(df10)] = ['a) Material de Embalaje','Por material','Ver tablas','-','X','x','$-']
df11.loc[len(df11)] = ['a) Hora hombre extra','Por hora hombre','335.99','','X','367','$123308.33']
df11.loc[len(df11)] = ['g)Recurso dedicado','Por mes','48267.78','-','X','1','$48267.78']
df11.loc[len(df11)] = ['Cobro Tiempo extra excedente a  la capacidad de  Salida (Drop-stock)','Por hora hombre','335.99','','X','-','$']
dfcd.loc[len(dfcd)] = ['a) Cajas de entrada 24hrs','Por caja','32.8','3200','X','0','$-']
dfcd.loc[len(dfcd)] = ['c) Cajas de salida  24hrs','Por caja','55.93','3200','X','0','$-']
dfcd.loc[len(dfcd)] = ['d) Acondicionado por caja ','Por caja','74.82','304','X','0','$-']
dfcd.loc[len(dfcd)] = ['d) Piezas inspeccionadas','Por pieza','28.25','-','X','0','$-']


print(df2)
print(df3)
print(df4)
print(df5)
print(df8)
print(df9)
print(df10)
print(df11)
print(dfcd)