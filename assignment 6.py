
import re
while True:






  user_input = input("enter your passwords:\n")
  


  if(len(user_input)<6 or len(user_input)>12):
     print("password must contain characters from 6 to 12")
     valid =False
     continue
  elif not re.search("[1-9]", user_input):
     print("password must contain numbeers 1-9")
     valid =False
     continue
  elif not re.search("[A-Z]", user_input):
      print("password must contain  upper case character")
      valid=False
      continue
  elif not re.search("[a-z]", user_input):
        print("password must  contain  lower case letter")
        valid =False
        continue
  elif not re.search("[$#@]", user_input):
        print("password must contain at least one special chaacter")
        valid =False
  elif re.search("\s", user_input):
        print("password should not comtain a space")
        valid = False
        continue
  else:
        print("password is valid")
        valid=True
        break

    


# dict_list =[{"make":"Nokia", "model":216, "color":"Black"},{"make":"MiMax","model":2, "color":"Gold"},
# {"make":"Samsung","model":"7", "color":"Blue"}]
# dict_list = sorted(dict_list, key = lambda x: x['color'])
# print(dict_list)

# c =[1,2,]
# x = map(lambda a, b : a * b, c)
# print(list(x))
# x = lambda a, b:a * b
# print(x(5,6))
# x = lambda a, b : a * b
# print(x(5, 6))
# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))