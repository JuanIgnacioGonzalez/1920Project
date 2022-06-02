import pandas as pd
import plotly.express as px
import numpy as np
import sklearn
from sklearn import linear_model 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.utils import shuffle
data = pd.read_csv('datos-tipo-cambio-usd-futuro-dolar-frecuencia-diaria.csv', sep = ',')

#data1 = data[["indice_tiempo","tipo_cambio_bna_vendedor","tipo_cambio_a3500","tipo_cambio_mae","volumen_mae","tipo_cambio_implicito_en_adrs","futuro_rofex_usd1m","interes_abierto_1m","interes_abierto_2m","interes_abierto_3m","interes_abierto_4m","interes_abierto_5m","interes_abierto_6m"]]



data = data[["tipo_cambio_bna_vendedor","tipo_cambio_a3500","tipo_cambio_mae","volumen_mae","tipo_cambio_implicito_en_adrs","futuro_rofex_usd1m","interes_abierto_1m","interes_abierto_2m","interes_abierto_3m","interes_abierto_4m","interes_abierto_5m","interes_abierto_6m"]]
data = data.loc[10000:15000]

print(data.head())

predit = "tipo_cambio_bna_vendedor"

x = np.array(data.drop([predit],1))
y = np.array(data[predit])

x_train, y_train, x_test, y_test = sklearn.model_selection.train_test_split(x,y,test_size=0.1)

linear = linear_model.LinearRegression()
print(x_train)
linear.fit(x_train,y_train)
acc = linear.score(x_test,y_test)
print(acc)
