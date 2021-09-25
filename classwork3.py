#tuples
#collection of data in parenthesis any data in an ordered list can be slice or indexing. they are not changeable.ti
# t1 = (False, True, 100)
# t2 = (1,4,9)
# t3 = t1 + t2## it worked because we are not adding anthing to nthe tuples
# print(t3)

#methods
#index()
#count()
# a = (1,4,9)
# del(a)
# print(a)

# my_tuples = "This", "is", "A", "tuple"
# print((my_tuples))# tuples can be written without the parathesis
# first, second, third = "this", "is", "are"
# print(first)

# #unpacking
# first = "john"
# second = "Bull"
# first, second =second, first
# print(first)
# #set is anything written in a curly bracket. set is unordered. a set is changeable.
# s = {"True", "born", 45, "water"}
# s.discard("stella")
# s.remove("hope")

# s.add("john")
# print(s)
# #union
# s = {"true", "born", 45, "50", "water"}
# b = {"mary", "favour", "tunde", 50}
# # #u = s.union(b)
# s.update(b)
# # #d = s.intersection(b)

# print(s)


# print(s.difference(b))
# print(b.difference (s))
# print(s.symmetric_difference(b))
#exercise 2: return a new set of identical items from a given two set
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set3= set1.intersection(set2)
# print(set3)


#remove items 10, 20, 30, from the following set at once
# set1 = {10, 20, 30, 40, 50}
# set1.difference_update({10, 20,30})
# print(set1)

# #exercise 6 return a set of all elemrnt in either A or B , but not in both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1.symmetric_difference(set2))

# #exercise 9 : remove items from set1 that are not commom to both set1 and set2
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# # set1.intersection_update(set2)#this updates the ones that are not comon to  both set by removing them out
# set3 =set1 .intersection(set2)
# print(set3)


#question
#given an array of integers, cal

# from decimal import Decimal
# l1 = [1,1,0,-1,-1]
# for i in l1:
#     positive = []
#     negative = []
#     zero = []
#     if i > 0:
#        positive.append(i)
#     elif i < 0:
#          negative.append(i)
#     else:
#              zero.append(i)
# ratio_p = len(positive)/len(l1)     
# ratio_n = len(negative)/len(l1)
# ratio_zero = len(zero)/len(l1)

# print(round(Decimal(ratio_p), 6))
# print(round(Decimal(ratio_n), 6))
# print(round(Decimal(ratio_zero),6))


# #algorithm.
# #time complexity
# #memory complexity
# # big o notation
# A = {2,4,6}
# B = {3,6,9}
# #sum = A .intersection(B)
# sum2 =A.difference(B)
# sum3 =B .difference(A)
# print(sum3)

# a = {"stella", "chioma", "stella"}
# print(a)

# friends = {'John','Michael','Terry','Eric','Graham'}
# my_friends = {'Reg','Loretta','Colin','John','Graham'}

# a = my_friends.symmetric_difference(friends)
# print(a)
# s1 = {5,6,7,9,9}
# s2 = {1, 6,8,9}
# s3 = {6,9,8,0,5}
# s4 = s3.difference(s1,s2)
# print(type(list(s4)))

# employers = ["stella", "anabel", "wisdom", "salvation", "ann", "jona", "john", "philip", "andrew", "emmanuel"]
# jim_members =["mike", "ann", "stella", "philip", "emmanuel","wisdom"]
# accountants=["wisdom", "salvation", "jona", "philips", "andrew", "emmanuel"]
# result =set(employers).difference(jim_members, accountants)
# print(result)
# employers = {"stella", "anabel", "wisdom", "salvation", "ann", "jona", "john", "philip", "andrew", "emmanuel"}
# jim_members ={"mike", "ann", "stella", "philip", "emmanuel","wisdom"}
# accountants={"wisdom", "salvation", "jona", "philips", "andrew", "emmanuel"}
# employers.difference_update(jim_members, accountants)
# c=employers.difference(jim_members, accountants)
# print(employers)
# # employers.intersection_update(jim_members, accountants)
# print(employers)
students ={"name":"stella", "age":30, "course":["computer sc", "maths","programming"]}
#to loook through a list.
for key,values in students.items():
    print(key, values)

# print(students["name"])
# students["phone"]=555.555

# #if we wamt to update multiole values in a dictionary we could better used the uupdate method
# #students.update({"name":"chisom", "age":25, "course":"computer sc", "interest":"coding"})
# print(students)
# #print(students.get("phone","not found"))

# #the del and pop method
# del students["age"]
# a=students.pop("name")
# print(students)
# print(len(students))
# print(students.keys())
# print(students.values())
# ##the item method prints out every items in the dict.
# print(students.items())


