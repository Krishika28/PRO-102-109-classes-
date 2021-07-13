import pandas as p
import plotly_express as px

df = p.read_csv("Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv")

fig = px.scatter(df, x= "Temperature", y= "Ice-cream Sales( ₹ )", color="Temperature", size = "Ice-cream Sales( ₹ )")
fig.show()