# a = [10, 1,5, 20,1,2,10,10]

# a[3]=25# changing the item in the list to 25
# print(a)
# #adding two lists together by + operator
# a = [3,6,7]
# b= [8,9,10]
# full_list = a + b
# #print(full_list)#similar to concatination in strings

# a = [8,7,2,4]
# b =[4,2,9,0]

# #a.append(12)
# #print(a)
# a.extend(b)
# print(a)
# # #create a new list of userNames. then write a program to input from user. requesting for his first and last name. generate a user
# # #name for him. the username should comprise of the first 3 words of his lastname and thr last two words of his first name. add this
# # #to his user name to the list of the username and print an ouput telling him an account has been created

# usernames=["stella,", "chika", "agbadu","bella1"]
# first_name = input("enter your firstname here:").title()
# last_name = input("enter your last name here:")

# final_username = last_name[:3]+first_name[-2:]
# usernames.append(final_username)
# print(usernames)
# print(f" hello {first_name} \nthank you for signing up.your account\n has been su created\nyour account id is {final_username} \n\tcheers\n\t admin\n\t" )


# #given the list below:
# a=[500, 200,[200, 500,700,[250,800],250],[1000]] #add 700 and 800 to the end of the list.

# b = a[2][2]

# c= a[2][3][1]
# answer = b+c
# a3 =a[3]
# a3.append(answer)

#print(a)
# #exercise 2
# #find the last position of a substring "emma" in a given string
# str1 = "Emma is a data scientist who knows python. Emma works at google."
# a = str1.rindex("Emma")# used to find the right index of a string. you can also use rfind method to find the left index
# print(a)#note there is nothing like lfind
#copy method
# a_list =[1, 2, 4,6]
# b = a_list
# c =a_list.copy()
# d = a_list[0]= 4




# print(b)
# print(c)
# print(d)

##remove and pop
# a =[0,1,2,3,4] 
# a.remove(1)
# print(a)
# a = [0,1,2,3,4]

# popped_element = a.pop(-1)
# print(popped_element)
 #pop removes an element and pops it ou. it returns the value so that we can store it.

#insert - takes elemnt and insert into a specified position in a list.
#list_ = [567,890,5678,]
#print(list_)
#list_.insert(1, "i just got inserted")
#print(list_)





# #copy will return a copy of the list


# sort and reverse
# list_ = [49, 17, 27, 37,19,22,48,0]
# list_.sort()
# print(list_)
# list_.reverse()
# print(list_)
# #it works with alphabets only not when you add numbers.i.e alphabets only, then numbers only

# print(type(range(5)))

# str1 = "PYnative"
# print(str1[1:4], str1[:5], str1[4:], str1[0:-1], str1[:-1])
# str1 = "my isname isisis jameis isis is bond"
# sub = "is"
# print(str1.count(sub,4))
# mystring = "pynative"
# l = [None]*10
#print(l)
#print(len(l))
# samplelist = [10,20,30,40]
# del  samplelist[0:6]
# print(samplelist)
# alist =[5,10,15,25]
# print(alist[::-2])#:: helps to pick steps in a string.
# reslist =[x+y for x in ["hello", "Good"  ] for y in ["dear","bye "]]
# print(reslist)
    
    
# a = [8,7,2,4,]
# b = [4,2,9,0]
# c = a+b 
# print(c)
# a.extend(b)
# print(a)
# txt = "I love apples, apple are my favorite fruit"

# x = txt.count("apple", 10, 24)

# print(x)

# a = [81, 82, 83]
	
# b = a[:]       # make a clone using slice
# print(a == b)
# print(a is b)
# print(b)
# toppings = ['pepperoni', 'sausage', 'mushroom']
# toppings.pop(1)
# print(toppings)
# total = toppings.pop(1)
# print(total)