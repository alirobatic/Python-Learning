#String Methods
name = "I am Alireza \n my family name Askari"                   #To write the code across two lines, we use the `\n` character.
print(name)

print(".......................................")

name1 = "I am Alireza \t my family name Askari"                   #We use `\t` to insert a space between two sentences.
print(name1)

print(".......................................")

name2 = "I am Alireza \\ my family name Askari"                   #To place a slash (\) between two sentences, use \\.
print(name2)

print(".......................................")

name3 = "I am Alireza \" my family name Askari"                   #We use " \" to place it between two sentences.
print(name3)

print("////////////////////////////////////////////////")
print("////////////////////////////////////////////////")

greeting = "Hello Mr.Askari"                                     #A string data item can take on various values.
print(greeting)
Last_name = input("Enter your last name:")
greeting = "Hello Mr."
print(greeting, Last_name, sep=" ")

print(".....................................")

Last_name1 = input("Enter your last_name = " )                   #Concatenating two strings with the plus sign (+)
greeting1 ="Ali " + Last_name1
print(greeting1)

print(".....................................")

Last_name2 = input("Enter your last name: ")                      #Concatenating two string variables using f-strings
First_name = input("Enter your first name:")
greeting2 = f"Hello Mr. {last_name2}"
print(greeting)
greeting3 = f"Hello {First_name} {last_name2}"
print(greeting3)                                   













