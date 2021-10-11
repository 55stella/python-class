import time
import random
import re
import ast
customer_details ={}
transactions={}
running =True

def   update_transactions(amount, trans, type, account_numb):
       trans_data ={
       "amount":amount,
       "type": type,
       "trans": trans
       }
       transactions[account_numb].append(trans_data)
while  running:
       activity = input('enter signup to signup and any other key to log in\n')
       if activity == "signup":
         
         pin =input("plesae enter your pin here:\n")
            
         pattern =r'[a-zA-Z]'
         if re.search(pattern,pin):
             print('pin must consist of numbers')
             continue
             
         elif len(pin) < 4:
             print('pin must not be less than four')
             continue
            
         else:
             name = input("enter your name here:\n")
        
            
           
         a  = list(range(10))
         random.shuffle(a)
         account_numb="".join(str(i)for i in a)
         customer_details[account_numb] ={}
         customer_details[account_numb]["pin"]=pin
         customer_details[account_numb]['name']=name
         customer_details[account_numb]["balance"]=0
         
         transactions[account_numb] = []
         print(transactions)
         with open('bank_app.text', 'w')as stella:
                 for key, value in customer_details.items():
                    stella.write('%s:%s\n' %(key, value))
         with open('bank_app.text', 'r') as john:
             for key, value in customer_details.items():
              baby = john.read()
              a = ast.literal_eval(baby)


        
         print(customer_details)
               
        
         print(f"Congratulations, {name} your account has been created.your account number is {account_numb}")
         continue

    
       else:
        
        
        
        print("enter your login details below")
         
         
         
             
        account_numb= input("enter your account number\n")
        pin =input("enter your account pin\n")
         
        if account_numb in customer_details.keys():
           user_pin = customer_details.get(account_numb).get("pin")
            
           
           if user_pin ==pin:
                       
        
        
            logged_in = True
            while logged_in: 
             action = input(f"""Welcome, {customer_details.get(account_numb).get('name')}
        
             What would you like to do?
             w for withdrawal
             d for deposit
             t for transfer
             b for balance
             a for account statement

     

             Press any other key to quit\n>>""").lower()
             
             
             
            


                
                  
        
              
                
            
                
            
         
        
        
             if action  =="d":
       
                  reciever = input("enter account number:\n") 
                  amount =float(input("enter the amount\n"))
                  name = input("enter your name:\n")
                  customer_details[account_numb]["balance"]+=amount

                #   trans_data={
                #        'amount':amount,
                #        'type':'credit',
                #         'trans':'Deposit'
                #    }
                #   transactions[account_numb].append(trans_data)
                #   print(transactions)
                   
                #   print(customer_details)
                  update_transactions(amount, 'credit', 'Deposit', account_numb)
                  with open('bank_app.text','a')as stella:
                      for key, value in transactions.items():
                          stella.write('%s:%s\n' %(key,value))
                  with open ('bank_app.text','r') as john:
                       baby = john.read()
                       a = ast.literal_eval(baby)
                        
                      
                  print(customer_details)
                  print(transactions)
         
        
             
             
         
            
                  if   reciever in customer_details.keys():
                      print(f"you have successfully deposited {amount} into your account . your balance is {customer_details.get(account_numb).get('balance')}") 
                      continue
                  else:
                    print("enter a valid account number")
                    break
       
          
         
           
        

             elif action =="w":
        
                 a= input("enter your account number\n")
                 b= input("enter your pin\n")
                 amount = int(input("enter amount\n"))
                 if amount<= customer_details.get(account_numb).get('balance') and a in customer_details.get(account_numb):












                     customer_details[account_numb]['balance']-=amount
                     print(f"withdrawal sucessful, your balance is {customer_details.get(account_numb).get('balance')}")
                    

                     

              
               
               
                    
                    
                
                    # trans_data ={
                    # 'amount':amount,
                    # 'trans_type':'debit',
                    # 'trans':'withdrawals'
                    # }
                    # transactions[account_numb].append(trans_data)
                    # print(transactions)

                     update_transactions(amount, 'Debit', 'withdrawals', account_numb)
                     
                     with open('bank_app.text', 'a') as stella:
                        for key, value in transactions.items():
                            stella.write("%s:%s\n" %(key, value))
                     with open('bank_app.text', 'r') as john:
                        for key, value in transactions.items():
                         baby = john.read()
                         a = ast.literal_eval(baby)
                                 
                     print(transactions)
                     print(customer_details)


              
                 else:
                     print('insufficient funds')
                     continue

                      
                      
                  
                   
                    
                 
                 
                
                
           
            
               
             elif action =="t":
                 amount = float(input('please enter the amount that you want to transfer\n'))
                 reciever_account= input('please enter the reciever account number\n')
                 reciever = customer_details.get(reciever_account,0)
                 if reciever:
                  if amount > customer_details.get(account_numb).get('balance'):
                     print("insufficent balance gerout")
                
                  else:
                   customer_details[account_numb]['balance']-=amount
                   with open('bank_app.text', 'a')as stella:
                       for key, value in transactions.items():
                           stella.write('%s:%s\n' %(key,value))
                   with open('bank_app.text', 'r') as john:
                       baby = john.read()
                       a = ast.literal_eval

                #    trans_data = {
                #        'amount':amount,
                #         'trans_type':'debit',
                #         'transaction':'transfer'
                #    }
                #    transactions[account_numb].append(trans_data)#here we are saving the transaction details 
                   #into a dictionary transaction. remember we assigned our transaction[account _num]to a list.
                   update_transactions(amount, 'debit', 'transfer', account_numb)
                   reciever['balance']+=amount
                   with open('bank_app.text', 'a') as stella:
                       for key, value in transactions. items():
                           stella.write('%s:%s\n' %(key,value))
                   with open('bank_app.text', 'a') as john:
                      baby = john.read()
                      a = ast.literal_eval(baby)

                   print("transfer successful")
                   print(customer_details)
                   print(transactions)
                #    beneficiary_trans_data ={
                #        'amount':amount,
                #         'trans_type':'credit',
                #          'trans':'transfer',
                #    }
                #    transactions[account_numb].append(beneficiary_trans_data)
                   update_transactions(amount, 'credit', 'transfer', reciever_account)
                   print(transactions)
         
           
                 else:
                  print("this account number does not exist re enter your account number")
                 continue


             elif action == 'b':
                 print(f"{customer_details[account_numb].get('balance')}\n")
             elif action =='a':
                 if len(transactions[account_numb])>0:
                     last_5_transactions = transactions[account_numb][-5:]
                     for transaction in last_5_transactions:
                         print('here is your last 5 transactions')
                         print("amount: " , transaction['amount'])
                         print("transaction type:", transaction['type'])
                         print("transaction reference:",transaction['trans'] )
                         #here we put the transaction details containig the last 5 transactions in a 
                         #for loop.
                 else:
                     print('enter a valid account number and pin')


             

             
              
             
                   
            
                      
    
#     Build a simple bank program that:
# 1. Allows customers to create account with pin and automatically generate account number.
# 2. Customers can login using their account number and pin
# 3. Can withdraw money
# 4. Can deposit money
# 5. Can transfer money to other customers in the bank program  

# import random
# import time

# user_data = {}
# keep_running = True


# while keep_running:
#     user_activity = input("Enter s to signup and any other key to login\n>>").lower()
#     if user_activity=='s':
#         name = input("Name:\n>>")
#         pin = input("Enter 4 digit pin:\n>>")
        
#         num = [str(i) for i in range(10)]
#         acc = ['9']
#         acc.extend([random.choice(num) for i in range(9)])
#         account_num = "".join(acc)
#         data = [('name', name), ('pin', pin), ('balance', 0)]
#         user_data[account_num] = {}
#         user_data[account_num].update(data)
#         print(user_data)
#         print(f"Your account has been successfully activated. Your account number is {account_num}. And your current balance is NGN0.\nPlease login to deposit and perform other transactions.")
        
#         progress = input("Enter p to do something else and any key to quit.\n>>").lower()
#         if progress == 'p':
#             continue
#         else:
#             break
#     else:
#         print("Enter login details below".title())
#         account_num = input("Account num:\n>>")
#         pin = input("Enter 4 digit pin:\n>>")
        
#         account_details = user_data.get(account_num, False)#this is a kind connecting to the value of the dictionary inside the dictionary
#         if account_details and account_details.get('pin')==pin:
#             action = input(f"""Welcome, {account_details.get('name')}!
# What would you like to do?
#     w for withdrawal
#     d for deposit
#     t for transfer
# Press any other key to quit\n>>""").lower()
#             if action == 'w':
#                 amount = float(input("Enter amount to withdraw\n>>"))
                
#                 if amount >= account_details.get('balance', 0):
#                     time.sleep(2)
#                     print("Insufficiant funds")
#                     print("Session Expired")
                    
#                     progress = input("Enter p to do something else and any key to quit.\n>>").lower()
#                     if progress == 'p':
#                         continue
#                     else:
#                         break
#                 else:
#                     account_details['balance']-=amount
#                     print('Please take your cash')
#                     progress = input("Enter p to do something else and any key to quit.\n>>").lower()
#                     if progress == 'p':
#                         continue
#                     else:
#                         break
#             elif action == 'd':
#                 amount = float(input("Enter amount to deposit\n>>"))
                
                
#                 account_details['balance']+=amount
#                 print('Deposit complete')
#                 progress = input("Enter p to do something else and any key to quit.\n>>").lower()
#                 if progress == 'p':
#                     continue
#                 else:
#                     break   
#             elif action == 't':
#                 amount = float(input("Enter amount to transfer\n>>"))
#                 recepient_account = input("Enter destination account number\n>>")
                
#                 recepient = user_data.get(recepient_account, False)
#                 if recepient:
#                     if amount >= account_details.get('balance', 0):
#                         print("Insufficient funds. GERROUT!")
#                     else:
#                         account_details['balance']-=amount
#                         recepient['balance']+=amount
#                         print("Transfer successful. Gerrout!")
#                         progress = input("Enter p to do something else and any key to quit.\n>>").lower()
#                         if progress == 'p':
#                             continue
#                         else:
#                             break
#                 else:
#                     print('No active customer for this account number. Gerrout!')
#                     progress = input("Enter p to do something else and any key to quit.\n>>").lower()
#                     if progress == 'p':
#                         continue
#                     else:
#                         break
                
                
#         else:
#             print("Please enter a valid account number and pin")
