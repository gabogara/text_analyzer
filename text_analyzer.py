#I receive the text in a string variable named text
text= input("Please enter text: ")

#convert the string to an auxiliary list
text_arr= list(text)

#I pass the entire text string in lowercase letters for comparison
lowercase_list = [x.lower() for x in text_arr]

#I receive what is necessary for requirement 1
char1= input("Please enter a letter to search for in the text: ")
char2= input("Please enter a letter to search for in the text: ")
char3= input("Please enter a letter to search for in the text: ")

#I show the results of the number of times the supplied letters appear in the text.
print(f"There are/is {lowercase_list.count(char1)} times the letter {char1}")
print(f"There are/is {lowercase_list.count(char2)} times the letter {char2}")
print(f"There are/is {lowercase_list.count(char3)} times the letter {char3}")

#It calculated the number of words in the text
print(f"The number of words in the text is:: {len(text.split())}")

#It calculated the first and last letters in the text
print(f"The first letter of the text is: {text[0]}")

number_char=len(text)
print(f"The last letter of the text is: {text[number_char-1]}")


#The word order is inverted.
splited_arr= text.split()
splited_arr.reverse()

final_str=' '.join(splited_arr)
print(f"The word order is inverted. The result is: {final_str}")

#the Python word is searched for in the text
splited_arr2= text.split()
logic = 'python' in splited_arr2
means={True:"the Python word was found in the text",False:"the Python word was not found in the text"}
print(means[logic])