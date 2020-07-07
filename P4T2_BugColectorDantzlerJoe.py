# Bug Collector
# 7/5/2020
# CTI-110 P4T2 - Bug Collector
# Joe Dantzler

# Initialize the accumulator
total=0

# Get the bugs collected each day.
for day in range(1,8):
    # Prompt the user.
    print('Enter the bugs collected on day', day)

    # Input the number of bugs.
    bugs = int(input())
    total += bugs

# Display the total bugs.
print('You collected a total of', total, 'bugs.')
