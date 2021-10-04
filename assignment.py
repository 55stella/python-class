# x = 7
# g=2*(x)**3-4*(x)
# print(g)

# naira = 200
# dollar = 30
# naira_to_dollar =dollar * naira
# print(naira_to_dollar)
import time
import random
print("welcome to rock paper scissors game. do you want to play this ggame")
a =input("enter 'yes'  to continue")

time.sleep(3)
print("authenticating")
time.sleep(1)
print("....")
game = ["r","p","s"]
human = input("enter your choice here:").lower()
computer = random.choice(game)
if human ==computer:
    print("its a tie")

if(human =="r" and computer =="s")or (human =="p" and computer =="r") or (human =="s" and computer=="p"):
        print("human win")
elif(computer =="r" and human =="s") or(computer =="p" and human =="r") or (computer=="s" and human =="p"):
        print("computer win")
else:
        print("input is invalid")     
    
        


        