from collections import Counter

# Initialize the list of numbers
numbers = [1, 2, 2, 3, 4, 4, 4, 5]

# Count occurrences
occurrences = Counter(numbers)

# Print the occurrences
for number, count in occurrences.items():
    print(f'Number {number} occurs {count} times.')
