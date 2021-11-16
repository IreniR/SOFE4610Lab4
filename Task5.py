import matplotlib.pyplot as plt
import csv

data = []
with open('temperature.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(str(row[0]))
print(data)
plt.figure(1)
plt.plot(data)
plt.ylabel('Temperature')
plt.show()
