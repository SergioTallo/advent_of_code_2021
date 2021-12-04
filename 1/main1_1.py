# Initialize counter to store the results
counter = 0

# Open file with the inputs and store every line (as an int) in an element of a list
with open('input.txt') as f:
    values = [int(i) for i in f.readlines()]

# Go through every element of the list (starting with the second) and compare every element with the previous one
for i in range(1, len(values)):
    # If the element is bigger than the previous one increase the counter by one
    if values[i] > values[i-1]:
        counter += 1

# Show the results
print(counter)
