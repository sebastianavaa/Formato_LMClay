import pandas as pd
import numpy as np

#Completar información utilizando comillas simples: ''.
#Asegurarse que nombreExcelOriginal y nombreExcelFinal finalicen con .xlsx.
#Asegurarse que el archivo excel a formatear contiene información que pertenece a un mismo año.
nombreExcelOriginal = '/Users/sebastiannava/Downloads/Libro Mayor LINENTEC SPA-2024-01-01-2024-09-30-1730294429.xlsx'
#año = '2024'
#empresa = 'The Clash' #Nombre que aparece en el módulo de "Uploads" de Accountfy, del respectivo card.

def formatearmayor(año, empresa):
    df1 = pd.read_excel(nombreExcelOriginal, header=5)
    condicion1 = (~df1['Cuenta'].isin(['Cuenta', 'Saldo anterior de la cuenta'])) & (~df1['Cuenta'].isna())
    df1 = df1[condicion1]
    condicion2 = (df1['Más Información'].str.contains('apertura', case=False) & ~df1['Más Información'].str.contains('spa', case=False)) # case=False indica que el filtro no es sensible a mayusculas ni minúsculas
    df1 = df1[~condicion2]

    #display(df1.head(5))

    df2 = pd.DataFrame()
    df2['Código de la cuenta'] = df1['Cuenta'].str.slice(0, 10)
    df2['Cuenta'] = df1['Cuenta'].str.slice(11, 110)
    df2['Valor'] = df1['Crédito'] - df1['Débito'] #(Crédito - Débido)
    df2.loc[(df1['Débito'] == 0), 'D/C'] = 'C'
    df2.loc[(df1['Crédito'] == 0), 'D/C'] = 'D'
    df2['Descripción'] = df1['Más Información'].str.slice(0, 120)
    df2['Fecha de la entrada'] = df1['Fecha Contabilización']
    df2['Centro de costos'] = ''
    df2['Empresa'] = empresa
    df2['Informaciones adicionales'] = 'Asiento ' + df1['Nº Asiento'].astype(str)
    df2['Contraparte'] = df1['Contraparte']
    #display(df2.head(5))

    #Debe ser 0, de lo contrario, el código falló.
    sumaValores = df2['Valor'].sum()
    print(sumaValores)
    nombreExcelFinal = f'/Users/sebastiannava/Downloads/Carga - {empresa} - Mayor - 202407 a 202407.xlsx' # Formato: 'Carga - empresa - Mayor - aaaamm a aaaamm.xlsx'

    df2.to_excel(nombreExcelFinal, index=False)