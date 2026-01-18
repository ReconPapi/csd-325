#Robert Ruiz 18 Jan 2026 Module 1.2 Assignment
#This program counts down the number of bottles on the wall based on user input
def main():
    # Ask the user for the starting number
    start = int(input("Enter number of bottles: "))

    #End the program if the user enters a number less than 1
    if start < 1:
        print("You need to buy some beer buddy")
        return

    # Call the countdown function
    countdown(start)

    # Final message
    print("Time to buy more beer!")

def countdown(bottles):
    # Count down from the starting number to 1
    while bottles > 1:
        print(f"{bottles} bottle(s) of beer on the wall, {bottles} bottle(s) of beer.")
        print(f"Take one down, pass it around, {bottles - 1} bottle(s) of beer on the wall.\n")
        bottles -= 1

    # When the countdown reaches 1 bottle
    print("1 bottle(s) of beer on the wall, 1 bottle(s) of beer.")
    print("Take it down, pass it around, 0 bottle(s) of beer on the wall!\n")


# Run the program
main()