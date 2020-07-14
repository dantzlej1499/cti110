# Kilometer Converter
# 7/12/2020
# CTI-110 P5T1 - Kilometer Converter
# Joe Dantzler

# This program converts kilometers to miles.
Conversion_Factor = 0.6214

# The main function gets a distance in kilometers and calls
# the show miles function to convert it.
def main():
    # Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    # Display the distance converted to miles.
    show_miles(kilometers)

# The show_miles function converts the parameter km from
# kilometers to miles and displays the result.
def show_miles(km):
    # Calculate miles.
    miles = km * Conversion_Factor

    # Display the miles.
    print(km, 'kilometers equals', miles, 'miles.')

# Call the main function
main()
    
