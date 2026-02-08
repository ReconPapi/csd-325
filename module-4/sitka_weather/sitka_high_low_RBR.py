#Added menu instructions for Highs, Lows, or Exit
#Added user input to select highs, lows, or exit
#Added support for low temperatures (read lows and plot in blue)
#Added loop (while True) so program repeats until user exits
#Added exit message and clean exit using sys.exit()
#Added import sys to support exit process
#Saved as sitka_high_low_<your initials>.py for Module 4

#This program shows a graph of temperatures from a csv file based on user input

import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    #Get dates and temps from files
    dates, highs, lows = [], [] ,[]
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[5])
        highs.append(high)

        low = int(row[6])
        lows.append(low)

while True:
    #Display menu and options to select
    print("\nWelcome to the Temperature Viewer Menu, Please make a selection below")
    print("Highs - To View High Temperatures")
    print("Lows - To View Low Temperatures")
    print("Exit - To Exit Program")

    #Get choice from user
    choice = input("Enter your choice: ").strip().lower()

    #exit message
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

    #message for invalid input
    else:
        print("Invalid choice. Please enter Highs, Lows, or Exit.")