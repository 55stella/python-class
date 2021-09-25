#to chamge the value of a dictionary
#my_diction = {"pet": "dog","color":"Brown"}
#my_diction["color"] = "yellow"
#my_diction["pet"]
#my_diction.get("pet")
#my_diction.get("stella",2)
# my_diction["country"] = "nigeria"
# print(my_diction)
#dictionary methods
#1.copy
#get()
#how to creat a new key
#pop

# to get all the keys availabel in a dictionary
# my_dict ={"name": "jerry", "courses":["Data science", "Backend"], "scores":{"data science": 20,"backend":15.7,},}
# # my_dict.get("course", "computer")
# # my_dict["course"] = "computer"
# # print(my_dict)
# # a = input("enter your course:")
# # b = input("enter your score here:")
# # # my_dict["courses"].append(a)
# # # print(my_dict)

# # my_dict["scores"][a] = b
# # #pop
# #a = my_dict.pop("name")
# var = my_dict.pop("scores")
# my_dict.update({"result":var})
# # # my_dict["result"]=var

# print(my_dict)

#print(my_dict)

#items always return a list of tuples. grouping of key value pair in tuples
#updates
#we are updating one particular dictionary with another dictionary
# my_dictionary ={"name":"john", "gender":"MALE"}
# my_dictionary.update({"key":"value"})
# list_of_tuples = [("john", "Abuja"),("nigeria","canada")]
# my_dictionary.update(list_of_tuples)
# print(my_dictionary)
#pop
#DATA CONVERSION
# a = my_dict["result"]
# print(type(a))
#you can only change string to integer if the string is a number
# print(type(my_dict.keys()))
# list1 =[1,2,3,4,5]
# print(str(list1))
# print(list(my_dict))


# change brads salary to 8500 from a given python dictionary

# sampleDict = {
#     "emp1":{"name":"jhon", "salary":7500},
#     "emp2":{"name":"Emma", "salary": 8000},
#     "emp3":{"name":"Brad","salary":6500}
# }
# sampleDict["emp3"]["salary"] = 8500
# print(sampleDict)

#write a program that takes in  the user details and saves it in the user dictionary following the format below
# users = {"username":{"firstname":"firstname", "lastname":"lastname"}}
users = {}
firstname = input("enter your firstname: ")
lastname = input("enter your lastname: ")
username=firstname[:2]+ lastname[:-2:]
users[username] ={}
 #here we want to access the next dictionary of first and lastname
users[username].update({"firstname": firstname})
users[username].update({"lastname": lastname})#here we are updating inside the second dict

print(users)

#given the list below:
#[2,2,4,6,7,2,4,4,3,6,2,1]. write a program to remove duplicates from the list and sort it
#expected output [1,2,3,4,6,7]
# l1 = [2,2,4,6,7,2,4,4,3,6,2,1]
# l2 = set(l1)
# l3 = list(l2)
# l3.sort()
# print(l3)

#write a program to convert a list of multiple integers to a single integer
# ["11","55", "33"]
# a = ["11", "55","33"]
# c = "".join(a)
# #b = a[0] + a[1] + a[2] 
# print(c)

#print(int(b))

#5write a program to unpack a tuple into several variables
# my_tuple =(1, 2, 3, 4, )
# c,d,e,f=my_tuple
# print(c)
# print(d)
# print(e)
# print(f)

# #write a program to covert the tuple below to a string
# one_tuple = ("U","n","i","v","e","r","s","i","t","y")

# tuple_to_string = "".join(one_tuple)
# print(tuple_to_string)



# total_n0_of_students =9
# english_newpaper ={1,2,3,4,5,6,7,8}
# french_newspaper ={10, 1, 2, 3, 11, 21, 55, 6 ,8}
# c = french_newspaper.symmetric_difference(english_newpaper)
# print(len(c))



# num_english = input()
# english = input()
# num_french =input()
# french = input()

# words_english = set(english.split())
# words_french = set(french.split())

# final = words_english.symmetric_difference(words_french)
# # print(final)
# print(len(final))