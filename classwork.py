first_name ="stella"
last_name = "agbadu"
full_name = first_name + " " + last_name

#print(full_name[7:15:2])#string slicing


#formatting
#name = "desmond"
#price = 40
#print(f"welcome {name}. you are to pay N{price}")

#anotther way to do  it that is formatting
#name= input("tell us who you are:")#this serves as a prompt telling the user to input their name. it accepts any name from the user
# print("welcome {} . /nyou have just signed in".format(name.title()))

#name =input("what is your name ")
#age= input("how old are you ")
#year_of_birth =(2021-int(age))#conversion from one data type to another
#print(f"hello {name}, you were born in  {year_of_birth}, \nwhat can we do for you\n\tsigned\n\tmanagement" )

#name = input("tell us who you are:")
#print(name.title())# this converts the letter to a capital

#startwithmethod

name = "stella is fine"
#print(name.startswith("s"))


name= "my file.pdf".upper()
#print(name.endswith ("pdf"))
#split method
p = " "
print(p.isspace())
fulname = "stella, agbadu, chika"
final_name = fulname.split(',')
#print(final_name)

#join method every item in that iterable must be a string in order to use join.


#write a program to change "i am a boy" to "i-am-a-boy"


sentence = "i am a boy"
final = sentence.split()
word = "-".join(final)
#print(word)



#word_list =['stella', ' agbadu', ' chika']
#joining = "".join(word_list)
#print(joining)

#the replace method is used to replace the old method to new one 
#word ="i am a boy"
#new_word = word.replace(" ", "-")
#print(new_word)
#a doc string is ***
#whrite a program that takes user input, searches for the word and returns the string with the user input
#and returns the string with the user input capitalized. tell the user how many times the string appear regardless
#a= "this is my name, say my name and always say my name"
#b= input("enter your input:")
#word = a.replace("name", "Name")
#sentence = a.count("name")
#print(word)
#print(sentence)

#correction.
a = "this is my name, say my name and always say my name"
b = input("enter your input:\n>").lower
print(f"{a.count(b)} found")
answer = a.replace(b,b.upper())
print(answer)

#given two string s1 and s2; create a new string by appending s2 in the middle of s1

















