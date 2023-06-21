

# Question 1: Write a program that prompts the user to enter their
# name and their favorite color. Then, create a message that
# combines their name and favorite color to form a personalized
# message. Finally, print the message on the console.
# name=input("What is your name?\n")
# color=input("What is your favourite color?\n")
# print(f"Hello {name}, I like {color} too.")

# Question 2: Write a program that prompts the user to enter a
# sentence. Count and display the number of words in the
# sentence.

# sentence= input("Write a sentence that you want to count?\n")
# splitted=sentence.split(" ")
# no_of_word=len(splitted)
# print(no_of_word)


#this is for character
# no_of_words=len(sentence)
# print(no_of_words)

# Question 3: Write a program that prompts the user to enter their
# full name (first name and last name). Convert the name to
# uppercase and display it in reverse order with a comma
# separating the last name and the first name.

# fullname=input("Insert your first name\n")
# fname,lname=fullname.upper().split()
# print(f"{lname} {fname}")


# Question 4: Write a program that takes a sentence as input and
# replaces all occurrences of a specific word with another word.
# Prompt the user to enter the original sentence, the word to be
# replaced, and the replacement word. Display the modified
# sentence.
#to replace the string in python

# message = input("Write the sentence\n")
# old_word=input(f"Your sentence is '{message}',now insert the word you want to change\n")
# new_word=input(f'write the word you want to replace {old_word} with\n')
# msg=message.replace(old_word,new_word)
# print(msg)

### list
my_list=["mango","chocolate","orange"]
print(my_list[1:])
print(my_list[:1])
print(my_list[0:3])
print(my_list[:-1])

#change value
my_list[0]="potato"
#add in the end of the list
my_list.append("mango")
#insert in between
my_list.insert(1,"tomato")
#remove from the list
my_list.remove("chocolate") #my_list.remove(my_list[2])
#deletes last item and save that item in some variable
forgot =my_list.pop(1)
#for sorting in ascending order
my_list.sort()
#for sorting in descending order
my_list.sort(reverse=True)

print(my_list)
###