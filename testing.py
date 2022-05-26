import csv
import pandas as pd
import plotly.express as px
data = pd.read_csv('datos-tipo-cambio-usd-futuro-dolar-frecuencia-diaria.csv', sep = ',')

print(data.head())
print(data.columns)
data1 = data[['indice_tiempo', 'tipo_cambio_bna_vendedor', 'tipo_cambio_a3500','tipo_cambio_mae', 'tipo_cambio_implicito_en_adrs']]

data2 = data[['indice_tiempo', 'volumen_mae', 'interes_abierto_1m', 'futuro_rofex_usd2m',
       'interes_abierto_2m', 'futuro_rofex_usd3m', 'interes_abierto_3m',
       'futuro_rofex_usd4m', 'interes_abierto_4m', 'futuro_rofex_usd5m',
       'interes_abierto_5m', 'futuro_rofex_usd6m', 'interes_abierto_6m']]

print(data.head())

fig = px.line(data1, x = data1.indice_tiempo,y= data1.columns ,title = "DOLAR BLUE")
fig.show()

fig2 = px.line(data2, x = data2.indice_tiempo,y= data2.columns ,title = "VALORES RAROS")
fig2.show()