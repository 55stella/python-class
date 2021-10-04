#write a program that takes input from user askking him for a list of  total  prices of items bought in 7days bought in 7days by 
#a customer
#calculate the sum
#calculate the average
#return a stdout(standard output)telling how much he has spent and the average amount .

# num_list  = input("enter the list of the total prices:").split(",")
# numbers = list(map(lambda string:int(string),num_list))
# sum_total = sum(numbers)

# average = sum_total/len(numbers)
# print(sum_total)
# print(average)




#mapping
# li = [1, 2, 3,4,5]

# print(list(map(lambda i: i**2,li)))
#zip() joins both elements together
# c = ["002", "014", "029"]
# p = [200, 400, 2015]
# d = dict(zip(c,p))
# e = list(zip(c,p))
# print(d)
#IF THERE are of  different length , it will delete the one that doesnt have a partner
#enumerate  it returns the indexs and the value. it basically returns it in list of tuples though you need to convert it to list.
#eg
# f = list(enumerate(c))
# print(f)
# #filter
# my_list =[2,3,5,7,8,20,4,1,9]
# name_list = list(filter(lambda a: a%2!=0, my_list))
# print(my_list)
# num = [20, 31, 45, 60, 10, 77]          
# my_filter = filter(lambda x : x % 2, num)        
# print(list(my_filter))




#range : this gives number within a specific range. a range will always give a range object but we need to convert it to a list.
#print(range(2,5,2))

#time module. you import
# import time
# print(time.time())
# print(time.gmtime())
# print(time.localtime())#this gives us our local time
# user = input("enter your name:\n")
# print("creating account, please wait...")

# time.sleep(3)
# print(',')

# time.sleep(1)
# print("congratulations , account has been created")


import random
my_list = [2,3,5,3,1,4,56,3]
b =random.shuffle(my_list)

# print(b)
# a = "1235"
# b = int(a)
# c = random(b)
# print(c)
#print(range(0,9))

print(random.choice(my_list))
print(random.sample(my_list, 4))
# print(my_list)
# random.seed(2)
print(random.randrange(3,10))
# from datetime import datetime
#print(datetime.now().weekday())
# date = datetime.now()
# print(datetime.strftime(date, "%A %d %B %Y", ))
# #strftim used to display the date and time i string formate or in full format.



#conditionals are rules that guides a particularoperation
# import random
# print("welcome to this game")
# list_of_numbers =[0, 34, 23, 12, 5, 67,4, 24, 79, 33, 7,8,2]

# choice = input(f"Guess number from {list_of_numbers}:\n")
# random.shuffle(list_of_numbers)
# com_choice = random.choice(list_of_numbers)
# if choice == com_choice:
#     print("you win")
# else:
#         print("e be like say you loose")
# print(com_choice)
# import random

# choices = ["R", "P", "S"]

# my_choice = input(f"Guess from: {choices}\n")
# comput_choice = (random.choice(choices))
# if (comput_choice =="P" and my_choice =="R" or
#     comput_choice =="S" and my_choice =="P" or
#     comput_choice =="R" and my_choice == "S"):
#     print("computer win")   
# elif (my_choice =="R" and comput_choice =="P"or
#      my_choice =="P" and comput_choice =="S" or
#      my_choice =="S"  and comput_choice =="R"):
#      print("i win")
# elif my_choice ==comput_choice:
#     print("there is a tie") 
# else:
#        print("you lost the game")
# import random
# print("R","k", "S" "game")
# user = input("enter your username to play:\n")
# print(f"computer vs {user}")
# time.sleep(3)
# print(",")
# time.sleep(1)
# print("loading....")
# time.sleep(1)
# choice = ["R","P","S"]
# human = input("enter your choice here:\n")
# computer= random.choice(choice)
# if human == computer:
#     print("its a tie")
# elif human ==choice[1] and computer == choice[0]:
#     print("you loose")
# elif human ==choice[2] and computer == choice[1]:
#     print("you loose")
# elif human == choice[1] and computer == choice[2]:
#     print("you loose")  
# elif computer==choice[1] and human == choice[0]:
#     print("you win ")
# elif computer == choice[2] and human == choice[1]:
#      print("you win")
# elif computer ==choice[1] and human == choice[2]:
#     print("you win")    
# else:
#     print("incorrect input, pls enter R, P,S")


# my_list = [1,2,4,6]
# print(list(map(lambda i:i**2, my_list)))
    

# my_list =[1,2,3,4,5]
# b =map(lambda x: x*x, my_list)

# print(list(b))
