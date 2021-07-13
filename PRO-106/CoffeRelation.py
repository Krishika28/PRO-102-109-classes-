import pandas as p
import plotly_express as px

coffee_df = p.read_csv("cups of coffee vs hours of sleep.csv")

fig = px.scatter(coffee_df, x= "Coffee in ml", y= "sleep in hours", color="week", size = "Coffee in ml")
fig.show()