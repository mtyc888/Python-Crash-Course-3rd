import matplotlib.pyplot as plt
from datetime import date
from pathlib import Path
import csv

#path
path = Path('C:/Users/ymarv/OneDrive/Desktop/python/Chapter_16/weather_data/data_NY.csv')


lines = path.read_text().splitlines()

reader = csv.reader(lines)

header_row = next(reader)

#get the data 
high_test = None
low_test = None
date_test = None

for num, column in enumerate(header_row):
    if column == 'TMAX':
        high_test = num
    if column == 'TMIN':
        low_test = num
    if column == 'DATE':
        date_test = num

if high_test is None or low_test is None or date_test is None:
    print('Missing columns detected')

highs = []
lows = []
dates = []

for row in reader:
    #skip rows that are too short
    print("s:", len(row))
    print("f:", max(high_test, low_test, date_test))
    if len(row) <= max(high_test, low_test, date_test):
        continue
    try:
        high = float(row[high_test])
        low = float(row[low_test])
        date_var = row[date_test]
    except ValueError:
        print(f"Missing data on {date_var}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(date_var)

#plot the data
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')
fig.autofmt_xdate()

#format the plot
ax.set_title("Temperature Low & High in New York")
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Temperature (F)',fontsize=12)

plt.show()