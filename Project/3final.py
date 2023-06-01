import pandas as pd
from entradas import sumUnidades_stockEntradas, sumUnidades_stockEmergenciasEntradas
from ocupacion import total_huecosplts, total_modulosest, ocupacionAmbiente, ocupacionTempRefri, ocupacionTempControl, ocupacionTempConge

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

tarifa = [0.0782, 2094672.32, 27.76, 41.64, 1.22, 1.00, 336.05 ,388.40 ,1180.47 ,1086.32 ,1791.45, 20.96, 31.44, '20% adicional', 'Ver tablas', 'Ver tabla',311.62 ,44767.00 ,311.62 ]
df1Tarifa = round(tarifa[1]* (1+tarifa[0]),2)
df1.loc[len(df1)] = ['Facturación Mínima Garantizada', 'Por mes',df1Tarifa, '', '1','1',tarifa[1]]


df2Tarifa1 = round(tarifa[2]* (1+tarifa[0]),2)
df2Volumenes1 = 27462.25
df2CantidadR1 =  sumUnidades_stockEntradas
df2CantidadC1 = df2CantidadR1 - df2Volumenes1 if df2CantidadR1 > df2Volumenes1 else 0
df2Monto1 = df2Tarifa1 * df2CantidadC1
df2Volumenes2 = 505
df2CantidadR2 = sumUnidades_stockEmergenciasEntradas
df2CantidadC2 = df2CantidadR2 - df2Volumenes2 if df2CantidadR2 > df2Volumenes2 else 0
df2Monto2 = tarifa[3] * df2CantidadC2
df2.loc[len(df2)] = ['a) Piezas de entrada  en 48hrs','Por pieza',df2Tarifa1,df2Volumenes1, df2CantidadR1, df2CantidadC1, '$ ' + str(df2Monto1)]
df2.loc[len(df2)] = ['b) Piezas de entrada en 24hrs','Por pieza',tarifa[3],df2Volumenes2,df2CantidadR2,df2CantidadC2, '$ ' + str(df2Monto2)]


df3Tarifa1 = round(tarifa[4]* (1+tarifa[0]),2)
df3Volumenes1 =  27462
df3CantidadR1 =  33044
df3CantidadC1 = df3CantidadR1 - df3Volumenes1 if df3CantidadR1 > df3Volumenes1 else 0
df3Monto1 = round(df3Tarifa1 * df3CantidadC1, 2)
df3Tarifa2 = round(tarifa[5]* (1+tarifa[0]),2)
df3CantidadR2 = 10
df3Monto2 = tarifa[5] * df3CantidadR2
df3.loc[len(df3)] = ['a) Etiquetado dentro de 48hrs','Por pieza',df3Tarifa1, df3Volumenes1, df3CantidadR1,df3CantidadC1,'$' + str(df3Monto1)]
df3.loc[len(df3)] = ['b) Etiquetado dentro de 24hrs','Por pieza',df3Tarifa2,'',df3CantidadR2, df3CantidadR2,'$' + str(df3Monto2)]


df4Tarifa1 = round(tarifa[6]* (1+tarifa[0]),2)
df4Volumenes1 =  811
df4CantidadR1 = total_huecosplts
df4CantidadC1 = df4CantidadR1 - df4Volumenes1 if df4CantidadR1 > df4Volumenes1 else 0
df4Monto1 = round(df4Tarifa1 * df4CantidadC1, 2)
df4Tarifa2 = round(tarifa[7]* (1+tarifa[0]),2)
df4Volumenes2 =  80
df4CantidadR2 = ocupacionAmbiente
df4CantidadC2 = df4CantidadR2 - df4Volumenes2 if df4CantidadR2 > df4Volumenes2 else 0
df4Monto2 = round(df4Tarifa2 * df4CantidadC2, 2)
df4Tarifa3 = round(tarifa[8]* (1+tarifa[0]),2)
df4Volumenes3 = 127
df4CantidadR3 = ocupacionTempRefri
df4CantidadC3 = df4CantidadR3 - df4Volumenes3 if df4CantidadR3 > df4Volumenes3 else 0
df4Monto3 = round(df4Tarifa3 * df4CantidadC3, 2)
df4Tarifa4 = round(tarifa[9]* (1+tarifa[0]),2)
df4Volumenes4 =  84
df4CantidadR4 = ocupacionTempControl
df4CantidadC4 = df4CantidadR4 - df4Volumenes4 if df4CantidadR4 > df4Volumenes4 else 0
df4Monto4 = round(df4Tarifa4 * df4CantidadC4, 2)
df4Tarifa5 = round(tarifa[10]* (1+tarifa[0]),2)
df4Volumenes5 =  12
df4CantidadR5 = ocupacionTempConge
df4CantidadC5 = df4CantidadR5 - df4Volumenes5 if df4CantidadR5 > df4Volumenes5 else 0
df4Monto5 = round(df4Tarifa5 * df4CantidadC5, 2)
df4.loc[len(df4)] = ['a) Hueco pallet a temperatura ambiente (1.0 x 1.2 x 1.2 m)','Por hueco pallet', df4Tarifa1, df4Volumenes1, df4CantidadR1, df4CantidadC1,'$' + str(df4Monto1)]
df4.loc[len(df4)] = ['b) Módulo de estantería ambiente (1.25 x 0.50 x 2.40 m)','Por modulo', df4Tarifa2, df4Volumenes2, df4CantidadR2, df4CantidadC2,'$' + str(df4Monto2)]
df4.loc[len(df4)] = ['c) Módulo de estantería +2 - +8 °C (1.25 x 0.50 x 2.40 m)','Por módulo', df4Monto3, df4Volumenes3, df4CantidadR3, df4CantidadC3,'$' + str(df4Monto3)]
df4.loc[len(df4)] = ['d) Hueco pallet +2 - +8 °C (1.25 x 0.50 x 2.40 m)','Por hueco pallet', df4Tarifa4, df4Volumenes4, df4CantidadR4, df4CantidadC4,'$' + str(df4Monto4)]
df4.loc[len(df4)] = ['e) Módulo de estantería -15 - -20 °C (1.25 x 0.50 x 2.40 m)','Por módulo', df4Tarifa5, df4Volumenes5, df4CantidadR5, df4CantidadC5,'$' + str(df4Monto5)]

df5Tarifa1 = round(tarifa[11]* (1+tarifa[0]),2)
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


""" print(df2)
print(df3)
print(df4)
print(df5)
print(df8)
print(df9)
print(df10)
print(df11)
print(dfcd) """