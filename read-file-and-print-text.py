# Define the file name - replace with whatever your question asks for filename
file_name = 'Questions.txt'

# Read and display the contents of the file
with open(file_name, 'r') as file:
    content = file.read()
    print(content)
