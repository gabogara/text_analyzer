#I receive the text in a string variable named text
text = input("Please enter text: ")

# Convert the string to an auxiliary list
text_arr = list(text)

# Create a lowercase version of the text list for case-insensitive comparisons
lowercase_list = [char.lower() for char in text_arr]

# Get user input for characters to search
char1 = input("Please enter a letter to search for in the text: ")
charx1 = char1.lower()
char2 = input("Please enter a letter to search for in the text: ")
charx2 = char2.lower()
char3 = input("Please enter a letter to search for in the text: ")
charx3 = char3.lower()

# Count occurrences of each character and display results
print(f"There are/is {lowercase_list.count(charx1)} times the letter {charx1}")
print(f"There are/is {lowercase_list.count(charx2)} times the letter {charx2}")
print(f"There are/is {lowercase_list.count(charx3)} times the letter {charx3}")

# Calculate the number of words in the text
num_words = len(text.split())
print(f"The number of words in the text is: {num_words}")

# Get the first and last letters of the text
first_letter = text[0]
last_letter = text[-1]
print(f"The first letter of the text is: {first_letter}")
print(f"The last letter of the text is: {last_letter}")

# Reverse the word order and display the result
reversed_text = ' '.join(reversed(text.split()))
print(f"The word order is inverted. The result is: {reversed_text}")

# Search for a word in the text and display the result
search_word = input("Please enter a word to search for in the text: ")
search_word = search_word.lower()
found = search_word in text.lower().split()
result = "the word was found in the text" if found else "the word was not found in the text"
print(f"{result}")