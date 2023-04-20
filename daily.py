import matplotlib.pyplot as plt

# Read the data from file
with open('MAC000069_223days.csv') as f:
    data = f.read()

# Split the data into rows and columns
rows = data.strip().split('\n')
columns = [row.split(', ') for row in rows]

# Extract the date and 30-minute interval readings from each row
dates = []
readings = []
for row in columns:
    dates.append(row[0])
    readings.append([float(x) for x in row[1].split()])

# Calculate the daily load curve by summing the 30-minute interval readings for each day
daily_load_curve = []
for readings_per_day in readings:
    daily_load_curve.append(sum(readings_per_day))

# Plot the daily load curve using matplotlib
plt.plot(dates, daily_load_curve)
plt.xlabel('Date')
plt.ylabel('KWH')
plt.title('Daily Load Curve')
plt.show()
