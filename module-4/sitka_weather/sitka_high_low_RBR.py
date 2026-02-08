import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [] ,[]
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[5])
        highs.append(high)

        low = int(row[6])
        lows.append(low)

while True:
    print("\nWelcome to the Temperature Viewer Menu, Please make a selection below")
    print("Highs - To View High Temperatures")
    print("Lows - To View Low Temperatures")
    print("Exit - To Exit Program")

    choice = input("Enter your choice: ").strip().lower()

    if choice == 'exit':
        print("Thank you for using the temperature viewer. Goodbye!")
        sys.exit()

    elif choice == 'highs':
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice == 'lows':
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    else:
        print("Invalid choice. Please enter Highs, Lows, or Exit.")