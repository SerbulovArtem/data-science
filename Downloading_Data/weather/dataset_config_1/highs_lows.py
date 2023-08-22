import matplotlib.pyplot as plt
import csv
from datetime import datetime

plt.switch_backend('TkAgg')

filename = 'data/death_valley_2021_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[6])
            low = int(row[7])
        except ValueError as e:
            print(e, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


fig = plt.figure(dpi=128, figsize=(10, 6))

plt.plot(dates, highs, c='red', label='High Temperature', alpha=0.7)
plt.plot(dates, lows, c='blue', label='Low Temperature', alpha=0.7)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title('Weather Statistics Death Valley, California', fontsize=24)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()

plt.ylabel('Temperature (F)', fontsize=16)
plt.ylim(10, 140)

plt.tick_params(axis='both', which='major', labelsize=16)

plt.legend()
#plt.show()
plt.savefig('death_valley_2021_visual.png')
