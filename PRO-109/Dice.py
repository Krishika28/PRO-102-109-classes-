import random as r
import plotly_express as px
import plotly.figure_factory as ff
import statistics as s
import plotly.graph_objects as go

count = []
sum_list = []

for i in range(0,1000):

    dice1 = r.randint(1,6)
    dice2 = r.randint(1,6)

    sum = dice1+dice2

    sum_list.append(sum)
    count.append(i)

print(sum_list)


mean = s.mean(sum_list)
mode = s.mode(sum_list)
median = s.median(sum_list)
st = s.stdev(sum_list)

print("Standard Devation: ", st)
print("Mean: ",mean)
print("Mode: ",mode)
print("Median: ",median)

sd1_start, sd1_end = mean - st, mean + st
sd2_start, sd2_end = mean - (2*st), mean + (2*st)

count_data1 = 0
count_data2 = 0
for i in sum_list:
    if(i > sd1_start and i<sd1_end):
        count_data1 = count_data1 +1
    if(i > sd2_start and i<sd2_end):
        count_data2 = count_data2 +1 

percentage_data1 = (count_data1/len(sum_list)) *100
percentage_data2 = (count_data2/len(sum_list)) *100

print(percentage_data1)
print(percentage_data2)

fig = ff.create_distplot([sum_list],["dice result"], show_hist=False)
#mean
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17], mode = "lines", name = "mean"))
#1st sd
fig.add_trace(go.Scatter(x=[sd1_start, sd1_start], y=[0,0.17], mode = "lines", name = "1st Standard Devation"))
fig.add_trace(go.Scatter(x=[sd1_end, sd1_end], y=[0,0.17], mode = "lines", name = "1st Standard Devation"))
#2nd sd
fig.add_trace(go.Scatter(x=[sd2_start, sd2_start], y=[0,0.17], mode = "lines", name = "2nd Standard Devation"))
fig.add_trace(go.Scatter(x=[sd2_end, sd2_end], y=[0,0.17], mode = "lines", name = "2nd Standard Devation"))

fig.show()