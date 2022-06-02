import csv
import pandas as pd
import plotly.express as px
import plotly.io as pio


import talib as talib
import numpy

def add_horizontal_lines(graph, y_low, y_high):
       graph.add_hline(y=y_high)
       graph.add_hline(y=y_low)
#print(help(talib.ADX))

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

select_coin = int(input("(1):tipo_cambio_bna_vendedor \n(2):tipo_cambio_a3500 \n(3):tipo_cambio_mae\n(4):tipo_cambio_implicito_en_adrs \nINGRESE LA MONEDA QUE QUIERA USAR-->  "))
select_ind = str(input("INGRESE EL INDICADOR QUE QUIERA USAR-->  ")).upper()

ind_function = getattr(talib, select_ind)

try:
       ind = ind_function(np_closes)
except Exception as e:
       try:
              ind = ind = ind_function(np_closes,np_opens,np_closes)
       except Exception as e:
              print('{}'.format(e))

print(ind)

if select_coin == 1:
       choice = "tipo_cambio_bna_vendedor"
elif select_coin == 2:
       choice = "tipo_cambio_a3500"
elif select_coin == 3:
       choice = "tipo_cambio_mae"
elif select_coin == 4:
       choice = "tipo_cambio_implicito_en_adrs"









data1 = data[['indice_tiempo',choice]]





data1.insert(2,select_ind,ind)
plotly_template = pio.templates["plotly_dark"]

try:
       fig = px.line(data1, x = data1.indice_tiempo,y= data1.columns ,title = '{}'.format(select_ind)+' en {}'.format(choice))
       if select_ind == 'RSI':
              add_horizontal_lines(fig,30,70)
       elif select_ind == '':
              print("No se ha seleccionado ninguna funcion")
       elif select_ind == 'MOM':
              add_horizontal_lines(fig,0,0)       
       fig.update_layout(template=plotly_template)
       fig.show()
except Exception as e:
       print('{}'.format(e))
