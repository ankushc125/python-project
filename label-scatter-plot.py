import matplotlib.pyplot as plt
# ensure you run this command - pip3 install matplotlib

# Sample data
x = [1, 2, 3, 4, 5]  # List of x values
y = [2, 3, 5, 7, 11]  # List of y values

# Create a scatter plot
plt.scatter(x, y)

# Add labels and title
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Simple Scatter Plot')

# Show the plot
plt.show()
