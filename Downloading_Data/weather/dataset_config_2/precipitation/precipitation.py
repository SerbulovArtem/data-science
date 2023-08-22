import matplotlib.pyplot as plt
import csv
from datetime import datetime

plt.switch_backend('TkAgg')

filename = 'warsaw_2021_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, precipitation = [], []
    for row in reader:
        try:
            current_date = datetime.strptime('{}-{}-{}'.format(row[0], row[1], row[2]), '%Y-%m-%d')
            precipitation_data = float(row[3])
        except ValueError as e:
            print(e, 'missing data')
        else:
            dates.append(current_date)
            precipitation.append(precipitation_data)

fig = plt.figure(dpi=128, figsize=(10, 6))

plt.plot(dates, precipitation, c='blue', label='Precipitation', alpha=0.7)

plt.title('Precipitation Warsaw, Poland', fontsize=28)

plt.xlabel('', fontsize=18)
fig.autofmt_xdate()

plt.ylabel('Water mass (mm)', fontsize=18)
plt.ylim(0, 40)

plt.tick_params(axis='both', which='major', labelsize=18)

plt.legend()
#plt.show()

plt.savefig('warsaw_2021_visual')