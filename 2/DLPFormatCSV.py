import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

data = pd.read_csv('MAC000069.csv', usecols=[1], skiprows=[0], header=None, nrows=224)

dataframe = []
for index, row in data.iterrows():
    row_array = [float(x) for x in row.values[0].split()]
    if len(row_array) == 48:
        dataframe.append(row_array)


with open('OutputMAC000069.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(dataframe)

time_values = np.arange(0, 24, 0.5)

fig, ax = plt.subplots(figsize=(12, 6))

for i, row_array in enumerate(dataframe):
    ax.plot(time_values, row_array, label=f'Day {i+1}')


ax.set_title('Daily Load Profile Curve for user MAC000069')
ax.set_xlabel('Time (hours)')
ax.set_ylabel('Consumption in KWH')
ax.legend()
plt.show()
