import csv
import pandas as pd
import plotly.express as px
import plotly.io as pio


import talib as talib
import numpy

data = pd.read_csv('datos-tipo-cambio-usd-futuro-dolar-frecuencia-diaria.csv', sep = ',')

#print(data.head())
#print(data.columns)

print(data.index)
print(data.index[-1])

print(data.columns)

print(data['tipo_cambio_implicito_en_adrs'])

closes = []

cont = 0
while cont <= int(data.index[-1]):
       closes.append(data['tipo_cambio_implicito_en_adrs'][cont])
       cont = cont+1

np_closes = numpy.array(closes)

ind_function = getattr(talib, 'MOM')

ind = ind_function(np_closes)

print(ind)

#print(z)
#rsi = talib.x(np_closes)



data1 = data[['indice_tiempo','tipo_cambio_implicito_en_adrs']]
data1.insert(2,'rsi',ind)
plotly_template = pio.templates["plotly_dark"]

try:
       fig = px.line(data1, x = data1.indice_tiempo,y= data1.columns ,title = "DOLAR BLUE")
       fig.add_hline(y=70)
       fig.add_hline(y=30)
       fig.update_layout(template=plotly_template)
       fig.show()
except Exception as e:
       print('{}'.format(e))
