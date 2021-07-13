import pandas as p
import plotly.graph_objects as go

df = p.read_csv("data.csv")

student_df = df.loc[df['student_id'] == "TRL_xsl"]
print(student_df)

level_mean = student_df.groupby('level')['attempt'].mean()
print(level_mean)

fig = go.Figure(go.Bar(x = level_mean,y = ['level1','level2','level3','level4'],orientation='h'))
fig.show()