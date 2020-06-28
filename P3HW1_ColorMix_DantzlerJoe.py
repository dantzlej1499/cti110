#CTI-110
#P3HW1 - Color Mixer
#Joe Dantzler
#6/26/2020

# Color Mixer

# The colors red, blue, and yellow are known as primary colors because they
#cannot be made by mixing other colors. When you mix two primary colors, you
# get a secondary color.
# When you mix red and blue, you get purple. When you mix red and yellow, you
# get orange. When you mix and yellow, you get green.

primaryColor1 = input( 'Please enter primary color 1: ')
primaryColor2 = input( 'Please enter primary color 2: ')

Print()

if (primaryColor1 == 'red' and primaryColor2 == 'blue') or \
   (primaryColor1 == 'blue' and primaryColor2 == 'red' ):
    print( primaryColor1 + 'mixed with' + primaryColor2 + ' is purple ')
elif (primaryColor1 == 'red' and primaryColor2 == 'yellow') or \
     (primaryColor1 == 'yellow' and primaryColor2 == 'red'):
    print( primaryColor1 + 'mixed with' + primaryColor2 + ' is orange ')
elif (primaryColor1 == 'blue' and primaryColor2 == 'yellow') or \
     (primaryColor1 == 'yellow' and primaryColor2 == 'blue'):
    print( primaryColor1 + 'mixed with' + primaryColor2 + ' is green ')
else:
    print( ' At least on of your colors, ' + primaryColor1 + 'and' + \
           primaryColor2 + ' is not a primaryColor ')
