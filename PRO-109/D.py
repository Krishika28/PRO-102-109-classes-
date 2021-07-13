import plotly_express as px
import plotly.figure_factory as ff
import pandas as p
import statistics as s
import plotly.graph_objects as go

df = p.read_csv("data.csv")
list = df["Weight(Pounds)"].tolist()

mean = s.mean(list)
mode = s.mode(list)
median = s.median(list)
st = s.stdev(list)

print("Standard Devation: ",st)
print("Mean: ",mean)
print("Mode: ",mode)
print("Median: ",median)

fig = ff.create_distplot([df["Weight(Pounds)"].tolist()],["Height Data"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17], mode = "lines", name = "mean"))
fig.show()