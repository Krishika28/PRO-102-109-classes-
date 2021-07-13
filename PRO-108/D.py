import plotly_express as px
import plotly.figure_factory as ff
import pandas as p

df = p.read_csv("data.csv")

fig = ff.create_distplot([df["Weight(Pounds)"].tolist()],["Height Data"], show_hist=False)
fig.show()