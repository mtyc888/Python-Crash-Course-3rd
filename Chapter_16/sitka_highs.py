from pathlib import Path
import csv
import matplotlib.pyplot as plt

#build the path to the csv file
path = Path('C:/Users/ymarv/OneDrive/Desktop/python/Chapter_16/weather_data/sitka_weather_07-2021_simple.csv')
#read the file and chain the splitlines() method to get a list of all lines in the file and assign it to 'lines' variable
lines = path.read_text().splitlines()

#build a reader object, this is an object that can be used to parse each line into a file
reader = csv.reader(lines)
#when given an reader object, the next() function returns the next line in the file, starting from the beginning of the file
#we call next() only once, so we only get the first line of the file
header_row = next(reader)

#Extract high temperatures
highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

#plot the high temperatures
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(highs, color='red')

#format plot 
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()