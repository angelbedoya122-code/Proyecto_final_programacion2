import pandas as pd
import numpy as np

'''DataFrame del ejercicio'''
data = {
    'parcial1': [1.87, 0.78, 3.01, 4.16, 1.52, 3.06, 2.28, 2.96, 0.33, 1.52],
    'parcial2': [4.75, 0.78, 3.54, 1.06, 2.62, 0.70, 3.93, 0.23, 4.74, 0.49],
    'parcial3': [3.66, 0.29, 0.10, 0.91, 2.16, 1.46, 1.00, 3.04, 4.83, 3.42],
    'parcial4': [2.99, 4.33, 4.85, 0.92, 1.46, 1.83, 2.57, 0.85, 4.04, 2.20],
}
index = pd.Index([f'Estudiante{i}' for i in range(10)], name='nombre')
df = pd.DataFrame(data, index=index)

'''Pandas 1'''
def DecilFinal(estudiante):
    promedio = df.mean(axis=1)
    deciles = pd.qcut(promedio, 10)
    return deciles.loc[estudiante]

'''Pandas 2'''
def RankingFinal():
    df_ranking = df.copy()
    df_ranking['nota_final'] = df_ranking.mean(axis=1)
    df_ranking = df_ranking.sort_values(by='nota_final', ascending=False)
    df_ranking.index = range(1, len(df_ranking)+1)
    return df_ranking

'''Punto 3 pandas'''
def AprobadosPorParcial(umbral=3.0):
    aprobados = (df >= umbral).sum()
    return aprobados

'''Punto 4 pandas'''
def TendenciaEstudiante(estudiante):
    notas = df.loc[estudiante].values
    x = np.arange(len(notas))
    m, b = np.polyfit(x, notas, 1) 
    if m > 0:
        return 'mejora'
    elif m < 0:
        return 'desmejora'
    else:
        return 'estable'