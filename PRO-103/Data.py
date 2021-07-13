import pandas as pd
from pandas.core.reshape import tile
from pandas.io.parsers import read_csv
import plotly.express as px

#creating an empty dataFrame
df = pd. DataFrame()
print(df)

#reading line_chart.csv & storing the data in line_data as dataFrame 
line_data = pd.read_csv("line_chart.csv")
print(line_data)

#plotting a line graph
fig = px.line(line_data, x = "Year", y = "Per capita income", color = "Country", title = "Line Chart of Per Capita")

#displaying the graph
#fig.show()
bar_data = pd.read_csv("data.csv")

figure = px.bar(bar_data, x = "Country", y = "InternetUsers")
figure.show()