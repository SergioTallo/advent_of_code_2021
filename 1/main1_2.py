# Initialize counter to store the results
counter = 0

# Open file with the inputs and store every line (as an int) in an element of a list
with open('input.txt') as f:
    values = [int(i) for i in f.readlines()]

# Initialize element with the sum of the first three values
prev_value = (values[0] + values[1] + values[2])

# Go through every element (starting with the second one and till the element (last -2))
for i in range(1, len(values) - 2):
    # Sum the values of the element and the next two ones in a new value
    value = (values[i] + values[i+1] + values[i+2])
    # Compare with the value previously stored
    if value > prev_value:
        counter += 1
    # The new value becomes the old value to be compared with the next one
    prev_value = value

# Print the results
print(counter)
