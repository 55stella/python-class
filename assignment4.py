#soln
<<<<<<< HEAD
# num_subscriptin =int(input())
# first_newspaper = input()
# num_subscription2 =int(input())
# second_newspaper = input()


# split_set1 = set(first_newspaper.split())#going to print a list
# split_set2= set(second_newspaper.split())
# final = split_set1.intersection(split_set2)

# print(len(final))
# #print(final)


#rock paper scissors
import random
print("welcome to the game")
print("Rock paper scissors")
choice = input("Enter 'h' for help or 'p' to play:")
help = """"
this is a simple game that follows the rule below
Rock wins papaer

choices are for rock, p for paper and s for scissors
you have only one chance. can you beat me?
"""
print(help)

player_choice = input("whta do you choose\n").lower()
choices = ["r", "p","s"]
random.shuffle(choice)
com_choice = random.choice(choice)

if player_choice in choices:
   if(player_choice =="r" and com_choice =="s")or(player_choice =="p" and com_choice =="r") or (player_choice =="s" and com_choice =="p"):
      print("you win")

   elif (com_choice=="r" and player_choice =="s")or(com_choice =="p" and player_choice=="r")or(com_choice=="s" and player_choice=="p"):
     print("computer win")
   else:
        print("its a tie!")
else:
    print("invalid input. you loose!")        
=======
num_subscriptin =input()
first_newspaper =input()
num_subscription2 =input()
second_newspaper = input()


split_set1 = set(first_newspaper.split())
split_set2= set(second_newspaper.split())
final = split_set1.intersection(split_set2)
print(final)


>>>>>>> 40dc77f9520af49eb7bd9e062e87ced3daeadf10
