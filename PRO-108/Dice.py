import random as r
import plotly_express as px
import plotly.figure_factory as ff

count = []
sum_list = []

for i in range(0,100):

    dice1 = r.randint(1,6)
    dice2 = r.randint(1,6)

    sum = dice1+dice2

    sum_list.append(sum)
    count.append(i)

print(sum_list)

#fig = px.bar(x=sum_list, y=count)

fig = ff.create_distplot([sum_list],["dice result"])
fig.show()