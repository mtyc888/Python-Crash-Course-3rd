from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime
#build the path to the csv file
path = Path('C:/Users/ymarv/OneDrive/Desktop/python/Chapter_16/weather_data/sitka_weather_2021_simple.csv')
#read the file and chain the splitlines() method to get a list of all lines in the file and assign it to 'lines' variable
lines = path.read_text().splitlines()

#build a reader object, this is an object that can be used to parse each line into a file
reader = csv.reader(lines)
#when given an reader object, the next() function returns the next line in the file, starting from the beginning of the file
#we call next() only once, so we only get the first line of the file
header_row = next(reader)

#Extract high temperatures
highs = []
lows = []
dates = []
for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    try:    
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        highs.append(high)
        dates.append(date)
        lows.append(low)

#plot the high temperatures
plt.style.use('classic')
fig, ax = plt.subplots()
#alpha=0 makes the lines transparent, alpha=1 makes the line opaque ,alpha=0.5 makes the line lighter
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
#blue shading between the 2 lines
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
#format plot 
ax.set_title("Daily High & Low Temperatures, 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
#fig.autofmt_xdate() draws the date labels diagonally to prevent them from overlapping
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
#set the limits of just the y-axis
ax.set_ylim(10,140)
plt.show()