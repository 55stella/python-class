#No 1. write a python program to clone a list. my_list = ["this", true, "student", 45,66.43]
my_list = ["this", True, "student", 45, 66.43]
#b = my_list.copy()
b = my_list[:]
print(b)

#No2  Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#  Sample List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output = ['Green', 'White', 'Black']

# sample_list =['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# sample_list.remove('Red')
# sample_list.remove('Pink')
# sample_list.remove('Yellow')

# print(sample_list)
#correction 
sample_list =['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
a = sample_list.pop(0)
b = sample_list.pop(3)
c = sample_list.pop(3)# here, everytime we pop out something, the index re adjust to the next one
print(sample_list)

#No 3Write a program that takes in the user input of his favourite colour and adds it to an existing list of colours.
color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
user_color = input('enter your favourite color here:\n')
color_list.append(user_color)
print(color_list)
#No 4
 # Add item 7000 after 6000 in the following Python List
#Given: list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
#Expected output:[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

#list1[2][2].append(7000)
#a = list1[4]

#list1[2][2].insert(2,7000)

print(list1)


