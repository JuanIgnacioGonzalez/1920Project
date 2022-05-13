from calendar import calendar
from re import X
from typing import List
import numpy
import plotly.express as px
import pandas as pd

y = numpy.random.exponential(190, 365)

x = index=pd.date_range('2021-01-01', periods=365)
print(x)
df = pd.DataFrame(y, x)


"""
for i in range(365):
    x.append(i)


color = []
df = pd.DataFrame(y,x)
"""

rangoy = [0,300]
fig = px.line(df,markers=True ,range_y=rangoy,x = df.index , y = df.columns  ,title="DOLAR BLUE EL ULTIMO AÑO")
for idx, trace in enumerate(fig["data"]):
     trace["name"] = "dolar blue/ars" 

fig.update_xaxes(calendar = "gregorian")
fig.update_xaxes(gridwidth=3)
fig.update_xaxes(linewidth=5)
print(df)
fig.show()