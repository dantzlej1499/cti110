# Feet to inches
# 7/12/2020
# CTI-110 P5T2 - Feet to inches
# Joe Dantzler

# Constant for the number of inches per foot.
Inches_Per_Foot = 12

# main function
def main():
    # Get a number of feet from the user.
    feet = int(input('Enter a number on feet: '))

    # Convert that to inches.
    print(feet, 'equals', feet_to_inches(feet), 'inches.')

# The feet_to_inches function converts feet to inches.
def feet_to_inches(feet):
    return feet * Inches_Per_Foot

#Call the main function.
main()
