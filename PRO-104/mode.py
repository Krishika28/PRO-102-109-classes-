import pandas as p
import statistics as s

df = p.read_csv("data.csv")
height = df['Height(Inches)'].tolist()
median = s.median(height)
mode = s.mode(height)
mean = s.mean(height)

print('median of height: ', median)
print('mode of height: ', mode)
print('mean of height: ', mean)