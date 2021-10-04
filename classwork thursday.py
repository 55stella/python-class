#loop
#this is a way of going over a line of code
#for loop:do this for a time frame


# my_num = range(5)
# print(list(my_num))


# for i in range(5):
#     print(i+1)

# money = "9, 10,11,12".split(',')
# a = []
# for i in money:
#     a.append(int(i))
#     print(a)

# a =[1,2,3,4,5,6,7,8,9]
# #normal for loop 
# b =[]
# if i %2 ==0:
#  b.append(i)
    #list comprehension 
# a =[1,2,3,4,5,6,7,8,9]
# b =[i for i in a if i %2 ==0 ]
# print(b)

# a = [(0, "sheldon"), (1,"penny")]
# for e in a:
#     print(e[0])
# for e in a:
#     print(e)
# a = [1, 2, 3, 4]
# for j in a:
#     print((j))

#nested for loops
# a =[0,1,2]
# b = [2,4,6]
# c=[]
# for i in a:
#     for x in b:
#         c.append(i+x)
#         print(c)
#write a python program that can return list
# list1 =[10,20,30,40]
# list2=[100,200,300,400]

# list2.reverse()
# for x, y in zip(list1, list2):
#     print(x,y)  

# import re 
# import time
# firstname = input("enter your firstname:")
# lastname = input("enter your lastname:")
# user_email = input("enter your email:")
# password =input("enter your password here:")


# time.sleep(2)
# print(",")
# print("login")
# email = input("enter your email address here:")
# password= input("enter your password here:")




 
# while True:

#  if len(password)<6or len(password)>12:
#     print("password must contain characters from 6 to 12")
#     continue
#  elif not  re.search("[A-Z]", password):
#     print("password must contain  upper case character")
#     continue
#  elif not re.search("[a-z]", password):
#         print("password must  contain  upper case letter")
#         continue
#  elif not re.search("[$#@]", password):
#     print("password must contain at least one special chaacter")
#  elif re.search("\s", password):
#         print("password should not comtain a space")
#         continue
#  else:
#   valid:True
#  break
# if(valid):
#   print("password is valid")
# if  user_email == email and password == password:
#     isvalid:True


#while loop will keep runnig as long as a condition is met.
# x = 10
# while x >0:
#     print(x)
#     x-=1
# x =True
# while x:
#     print("i am a boy")
#     break

# # x = 1
# # while x <5:
# #  print(2)
# #  x+=1


# # length1 = input("enter the first size\n")
# # length2 = input("enter the second side\n")
# # length3 = input("enter the third side\n")

# # if length1 ==length2==length3:
# #     print("equilateral triangle")
# # elif(length1==length2) or (length2==length3) or (length1 ==length3):
# #     print("isosoles")
# # else:
# #  print("scalene")
# x =1
# while x <4:
#  print(2)
#  x+=1
a = [1,2,3,4,5]

my_str = "".join(str(e) for e in a)
print(my_str)

# a = [1, 2, 3, 4, 5]
# for i in a:
#     print(i)