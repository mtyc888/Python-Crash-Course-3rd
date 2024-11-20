from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

#declare the path
path = Path('C:/Users/ymarv/OneDrive/Desktop/python/Chapter_16/weather_data/sitka_weather_2021_full.csv')
#use the path to reach the file that you want to read
#read each text and use splitlines() function since it is a comma seperated file
#assign each lines to the variable lines
lines = path.read_text().splitlines()

#assign a reader for whatsever inside variable lines
reader = csv.reader(lines)
#get the first row of the csv file (usually its the header row) and assign it to header_row
header_row = next(reader)
#Extract the data from the file
#we want "PRCP" which is rainfall and it is at index 5
rainfalls = []
dates = []
#we run a for loop to loop through the reader
for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    #run a try-except-else block here incase of missing data
    try:
        rain = float(row[5])
    except ValueError:
        print(f"Missing data on {date}")
    else:
        dates.append(date)
        rainfalls.append(rain)

#After we extract the data, we plot them
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, rainfalls, color='blue')

#format the plot
ax.set_title("Amount of rainfall in sitka 2021")
ax.set_xlabel("Date", fontsize=12)
ax.set_ylabel("Amount of rain", fontsize=12)
ax.tick_params(axis='x', rotation=45)

plt.show()
