import time
import random
customer_details ={}
while True:
    activity = input("login or signup or deposit or withdrawal\n").lower()
    if activity == "login":
       account_numb= input("enter your account number\n")
       pin =input("enter your account pin\n")

       if account_numb in customer_details.keys():
           user_pin = customer_details.get(account_numb).get("pin")
           
           if user_pin ==pin:
              print("log in successful")
              continue
           else:
            print("enter a valid account number and  pin")
            continue
       else:
            print("there is no active user with this pin")
            continue
    elif activity == "signup":
       while True:
        pin =input("plesae enter your pin here:\n")
        name = input("enter your name here:\n")
        a  = list(range(0,9))
        random.shuffle(a)
        account_numb="".join(str(i)for i in a)
        
        print(f"Congratulations, {name} your account has been created.your account number is {account_numb}")
        customer_details[account_numb] ={}
        customer_details[account_numb]["pin"]=pin
        customer_details[account_numb]["balance"]=0
        print(customer_details)
        break
    elif activity =="deposit":
       while True:
         reciever = input("enter the recievers account number:\n") 
         amount = int(input("enter the amount\n"))
         name = input("enter your name:\n")
         customer_details[account_numb]["balance"]+=amount
         
          
         if reciever in customer_details.keys():
            print(f"you have successfully deposited {amount} into your account . your balance is {customer_details.get(account_numb).get('balance')}") 
            break
         else:
            print("enter a valid account number")
            continue
    elif activity =="withdrawal":
        while True:
           a= input("enter your account number\n")
           b= input("enter your pin\n")
           amount = int(input("enter amount\n"))
           if a in customer_details.keys():
              
              customer_details[account_numb]["balance"]-=amount
              print(f"withdrawal sucessful, your balance is {customer_details.get(account_numb).get('balance')}")
              break
           elif amount > customer_details.get(account_numb).get('balance'):
                print("insufficient funds")
                continue
           else:
             print("invalid pin and account number sign up.")
             continue
      