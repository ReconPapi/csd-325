#This program converts miles to kilometers

CONVERSION_FACTOR = 1.60934 

def main():
    #display intro screen.
    intro()

    try:
        #Get number of miles
        miles_needed = float(input("Enter the number of miles: "))

        #Convert miles to kilometers
        miles_to_kilometers(miles_needed)

    except:
        print("An exception occured, try again by entering only a number")

    #The intro function displays an introductory screen.
def intro():
    print('This program converts measurements')
    print('in miles to kilometers.')
    print('For your reference the formula is:')
    print(' 1 mile = 1.60934 kilometers')
    
    #The miles_to_kilometers function accepts a number of
    #miles and displays the equivalent number of ounces
def miles_to_kilometers(miles):
    kilometers = miles * CONVERSION_FACTOR
    print(f"{miles} miles converts to {kilometers:.3f}kilometers")

#Standard guard so imports don't auto run
if __name__== "__main__" :main()

    #call the main function
if __name__ == "__main__":    
    main()
