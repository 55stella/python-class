
import re
while True:




# s_char =["$","#","@"]

  user_input = input("enter your passwords:\n")
  valid:False


  if len(user_input)<6or len(user_input)>12:
     print("password must contain characters from 6 to 12")
     continue
  elif not  re.search("[A-Z]", user_input):
      print("password must contain  upper case character")
      continue
  elif not re.search("[a-z]", user_input):
        print("password must  contain  upper case letter")
        continue
  elif not re.search("[$#@]", user_input):
    print("password must contain at least one special chaacter")
  elif re.search("\s", user_input):
        print("password should not comtain a space")
        continue
  else:
    valid:True
    break
  if(valid):
        print("password is valid")


dict_list =[{"make":"Nokia", "model":216, "color":"Black"},{"make":"MiMax","model":2, "color":"Gold"},
{"make":"Samsung","model":"7", "color":"Blue"}]
dict_list = sorted(dict_list, key = lambda x: x['color'])
print(dict_list)



