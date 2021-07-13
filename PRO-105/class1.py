import statistics as s
import pandas as p
import plotly.express as px

df = p.read_csv("class1.csv")
marks = df['Marks'].tolist()
median = s.median(marks)
mode = s.mode(marks)
mean = s.mean(marks)

print('median of height: ', median)
print('mode of height: ', mode)
print('mean of height: ', mean)
stDevation = s.stdev(marks)
print('Standard Devation of class1: ',stDevation)

fig = px.scatter(df, x="Student Number",y = "Marks")
fig.update_layout(shapes=[dict(type='line',y0 = mean, y1= mean, x0= 0, x1= len(marks))])

fig.update_yaxes(rangemode='tozero')
fig.show()