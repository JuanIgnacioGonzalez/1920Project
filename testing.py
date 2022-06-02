import csv
import pandas as pd
import plotly.express as px
import plotly.io as pio


import talib as talib
import numpy

def add_horizontal_lines(graph, y_low, y_high):
       graph.add_hline(y=y_high)
       graph.add_hline(y=y_low)


data = pd.read_csv('datos-tipo-cambio-usd-futuro-dolar-frecuencia-diaria.csv', sep = ',')

#print(data.head())
#print(data.columns)

#print(data.index)
#print(data.index[-1])

#print(data.columns)

#print(data['tipo_cambio_implicito_en_adrs'])

closes = [0]
opens = [0]

cont = 1
while cont <= int(data.index[-1]):
       closes.append(data['tipo_cambio_implicito_en_adrs'][cont])
       opens.append(data['tipo_cambio_implicito_en_adrs'][cont-1])
       cont = cont+1


np_closes = numpy.array(closes)
np_opens = numpy.array(opens)

select_ind = str(input()).upper()

ind_function = getattr(talib, select_ind)

try:
       ind = ind_function(np_closes)
except Exception as e:
       try:
              ind = ind = ind_function(np_closes,np_opens,np_closes)
       except Exception as e:
              print('{}'.format(e))

print(ind)

data1 = data[['indice_tiempo','tipo_cambio_implicito_en_adrs']]
data1.insert(2,select_ind,ind)
plotly_template = pio.templates["plotly_dark"]

try:
       fig = px.line(data1, x = data1.indice_tiempo,y= data1.columns ,title = "DOLAR BLUE")
       if ind == 'RSI':
              add_horizontal_lines(fig,30,70)
       
       fig.update_layout(template=plotly_template)
       fig.show()
except Exception as e:
       print('{}'.format(e))
