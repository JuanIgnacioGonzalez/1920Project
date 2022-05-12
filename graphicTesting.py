from re import X
from typing import List
import numpy
import plotly.express as px
import pandas as pd

y = numpy.random.uniform(190, 210, 365)




x = []
for i in range(365):
    x.append(i)
print(x)

color = []
df = pd.DataFrame(y,x)

fig = px.line(df,markers=True , x = df.index , y = df.columns  ,title="DOLAR BLUE EL ULTIMO AÑO")
fig.show()