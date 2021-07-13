import csv

with open("data.csv", newline='') as f:
    data = csv.reader(f)
    list_data = list(data)

list_data.pop(0)
print(list_data)

total = 0

for h in range(len(list_data)):
    height = list_data[h][1]
    total = total+float(height)

mean = total/len(list_data)
print(mean)