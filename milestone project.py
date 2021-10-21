from types import new_class
import ast
import time
def write_to_file(data, username=None):#username has been assigned to none in case we need to call this function without a second parameter
        
     if username is not None:
         note = f'milstone/notes/{user_name}.text'
         with open(note, 'w') as note_file:
             note_file.write(data)
         return

     file = 'milstone/user_details.text'
     with open(file, 'w') as doc_file:
         doc_file.write(f'{data}')
     return
def read_files(username=None):
        if username is not None:
            user_note = f'milstone/notes/{username}.text'#this line of codes will read notes from a specific username if the username exists.
            try:

             with open(user_note, 'r') as note:
                my_note = note.read()

                return my_note
            except Exception as e: #this means that if the note doesnt exist. it should return false
             return False
        user_text = 'milstone/user_details.text' 
        with open(user_text, 'r') as text:
            user_info = text.read()
            final_read = ast.literal_eval(user_info)#this would convert back to a dictionary
            return final_read

user_details=read_files()#here we are aking this function to read the user_details dictionary
#that it has written down anytime we want to log in again
import re
def password_validation(password):

  if(len(password)<6 or len(password)>12):
     print("password must contain characters from 6 to 12")
     valid =False
     
  elif not re.search("[1-9]", password):
     print("password must contain numbeers 1-9")
     valid =False
     
  elif not re.search("[A-Z]", password):
      print("password must contain  upper case character")
      valid=False
      
  elif not re.search("[a-z]", password):
        print("password must  contain  lower case letter")
        valid =False
        
  elif not re.search("[$#@]", password):
        print("password must contain at least one special chaacter")
        valid =False
  elif re.search("\s", password):
        print("password should not comtain a space")
        valid = False
        
  else:
        
        valid=True
        return valid

    








running = True

while running:
    activity=input("enter 's' for signup, l for 'login' and any other key to quit\n")
    if activity =="s":
          a = input('enter  your full name here:\n')
          user_name = input('enter your username here\n')
          if user_name in user_details.keys():
              print('username already exist, try again')
              continue
          else:
             c = input('enter your email here:\n')
             password= input('enter your password here\n')
          if not  password_validation(password):
              continue
          else:

             

          

                user_details[user_name]={}
                user_details[user_name ]['password']= password
                user_details[user_name]['name'] = a#saving name into the dictionary 
                user_details[user_name]['email']=c
                write_to_file(user_details)
                print(f'your username is {user_name} and your password is {password} ')
                
            
    elif activity =="l":
        user_name = input('please enter your user_name here:\n')
        password = input('please enter your password here:\n')


        if user_name in user_details.keys() and password not in user_details.get(user_name).get('password'):
            print('enter a valid password')
            try_again = input( "Did you forget your passsword? y/n\n").lower()
            if try_again=="y":
               question =input('Would you like to change your password?y/n\n').lower()
               if question =="y":
               
                
                user_name =input('enter your username\n')
                if user_name in user_details.keys():

                    full_name = input('enter your fullname\n')
                
                    if full_name in user_details.get(user_name)['name']:
                        reset_password=input('enter your new password\n')
                        if password_validation(reset_password):
                            user_details[user_name]['password']=reset_password
                            write_to_file(user_details)
                            print('password reset successful')
                            continue
                else:
                    print('username doesnt match do you mind to create an account')
                    continue
            
            
    
        
            
            
                
            
        elif user_name in user_details.keys() and password in user_details.get(user_name).get('password'):
            
            
                
            logged_in = True
            while logged_in: 
                action =input   (f"""welcome {user_details.get(user_name).get('name')} w"
            what else whould you like to do?
            
            c to change your password
            n to create your note
            e to edit your note
            r to read your notes
            q  for options
            
            press any other key to quit\n""").lower()
            

                if action == "c":
                    old_password =input('enter your old password here:\n')
                    new_password = input('enter your newn password here:\n')
                    
                    if old_password in user_details.get(user_name).get('password'):
                       if password_validation(new_password):
                          user_details[user_name]['password']=new_password
                          write_to_file(user_details)


                       print(f"your password has been changed succesfully nd your new password is {user_details.get(user_name).get('password')}")
                elif  action =="v":
                      print('here is your profile information')
                    
                      print(f"name:{user_details[user_name]['name']}\n email:{user_details[user_name]['email']}")
                elif action == "q":
                      question =input('do you wish to edit your profile? yes/no\n').lower()
                      if question == "yes":
                          where = input('where do you want to edit? a to edit your name, b to edit your email\n')
                          if where =='a':
                              new_name = input('enter your name here:\n')
                              user_details[user_name]['name']= new_name
                              write_to_file(user_details)
                              print(f"your name has been successfully changed to {user_details.get(user_name).get('name')}")
                          elif where =="b":
                               new_email = input('enter your email here:\n').lower()
                               user_details[user_name]['email']=new_email
                               write_to_file(user_details)
                               print(f"your new email  is {user_details.get(user_name).get('email')}")
                      else:
                          print('sorry to see you go.')
                elif action =='n':
                    print('pleade wait as your note is beiing created')
                    time.sleep(3)
                    a = input('please enter your notes here\n').lower()
                    write_to_file(a, user_name)#here am saving my note against my username in the note files by calling the function on it
                    print('note has been succefully been saved')
                elif action == 'r':
                    time.sleep(2)
                    print("authenticating.....")    
                    read_note = read_files(user_name)
                    if read_note ==False:
                        print('you currently have no notes ')
                        continue
                    else:
                        print(read_note)
                        edit =input('enter e to edit, c to clear and any other key to continue\n').lower()
                        if edit =='e':
                            print('note that editing your notes wuld overwrite the entire notes')
                            warning = input('do you still want to continue with this? y/n\n').lower()
                            if warning =='y':
                                new_note=input('enter your edits here\n')
                                write_to_file(new_note, user_name)
                            else:
                                continue    
                            time.sleep(1)
                        elif edit =='c':
                            clear =input('are you sure that you want to ggo on with this?y/n\n')
                            if clear =='y':
                                write_to_file("", user_name)
                            else:
                                continue
                else:
                        break
    else:
        break    
                    



                    
      
        
        

