# Define the start and end values
start = 10
end = 20

# Define the exceptions
exceptions = [12, 16]

# Print numbers from start to end, excluding exceptions
for number in range(start, end + 1):
    if number not in exceptions:
        print(number)
