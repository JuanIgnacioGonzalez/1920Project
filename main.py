import csv
from turtle import width
import pandas as pd
import plotly.express as px
import plotly.io as pio
import talib as talib
import numpy

def add_horizontal_lines(graph, y_low, y_high):
    graph.add_hline(y=y_high, line_width=3, line_dash="dash", line_color="gray")

    graph.add_hline(y=y_low, line_width=3, line_dash="dash", line_color="gray")

data = pd.read_csv("datos-tipo-cambio-usd-futuro-dolar-frecuencia-diaria.csv", sep=",")

#tomar datos desde csv, luegos convertirlos a numpy array
closes = [0]
opens = [0]
indicador_confirmation = False
cont = 1
while cont <= int(data.index[-1]):
    closes.append(data["tipo_cambio_implicito_en_adrs"][cont])
    opens.append(data["tipo_cambio_implicito_en_adrs"][cont - 1])
    cont = cont + 1

np_closes = numpy.array(closes)
np_opens = numpy.array(opens)

#seleccion de activo por consola
select_coin = int(
    input(
        "(1):tipo_cambio_bna_vendedor (Banco Nacion) \n(2):tipo_cambio_a3500 (Mayorista) \n(3):tipo_cambio_mae (Electronico)\n(4):tipo_cambio_implicito_en_adrs (Dolar Informal) \nINGRESE LA MONEDA QUE QUIERA USAR-->  "
    )
)

#seleccion de indicador/es para chart
print('A continuacion, los indicadores disponibles')
for i in talib.get_function_groups():
       print(' ')
       print(i)
       print(talib.get_function_groups()[i])
while True:
       
       select_ind = str(
              input(
              "INGRESE EL INDICADOR QUE QUIERA USAR, SI NO QUIERE ANALIZAR INGRESE N-->  "
              )
       ).upper()
       if select_ind == "N":
              ind_function = "N"
              select_ind = "SIN INDICADOR"

              break

       try:
              ind_function = getattr(talib, select_ind)
              ind = ind_function(np_closes)
              indicador_confirmation = True
              break
       except AttributeError:
              print("ATRIBUTO NO ENCONTRADO, Intente nuevamente")

       except Exception as e:
              try:
                     ind_function = getattr(talib, select_ind)
                     ind =  ind_function(np_closes, np_opens)
                     indicador_confirmation = True
                     break
              except Exception as e:
                     try:
                            ind_function = getattr(talib, select_ind)
                            ind =  ind_function(np_closes, np_opens, np_closes)
                            indicador_confirmation = True
                            
                            break
                     except Exception as e:
                            try:
                                   ind_function = getattr(talib, select_ind)
                                   ind =  ind_function( np_opens, np_closes, np_opens, np_closes)
                                   indicador_confirmation = True
                                   break
                            except Exception as e:
                                   print("ATRIBUTO NO ENCONTRADO, Intente nuevamente")

print(ind)
#analisis de datos ingresados por consola
if select_coin == 1:
    choice = "tipo_cambio_bna_vendedor"
elif select_coin == 2:
    choice = "tipo_cambio_a3500"
elif select_coin == 3:
    choice = "tipo_cambio_mae"
elif select_coin == 4:
    choice = "tipo_cambio_implicito_en_adrs"

#ploteo de grafico 
data1 = data[["indice_tiempo", choice]]
if indicador_confirmation == True:
    data1.insert(2, select_ind, ind)

plotly_template = pio.templates["plotly_dark"]

try:
    fig = px.line(
       data1,
       x=data1.indice_tiempo,
       y=data1.columns,
       title="{}".format(select_ind) + " en {}".format(choice),
    )
    if select_ind == "RSI":
       add_horizontal_lines(fig, 30, 70)

    elif select_ind == "MOM":
       add_horizontal_lines(fig, 0, 0)
    if indicador_confirmation == False:
       print("GRAFICANDO SIN INDICADOR")

    fig.update_layout(template=plotly_template)
    # fig.update_layout(yaxis_range=[0,250])
    fig.update_yaxes(dtick=10)
    # fig.update_xaxes(showgrid=False,zeroline=False)

    fig.show()
except Exception as e:
    print("{}".format(e))
