#write a function to calculate the following statistical measures
#1. mean 2. meadian 3. mode. 4.standard deviation 5 . varians
num = [1,6,7,8,2,3,0,6,4,1,0,3,7,8,9]


# def mean(list1):
#     total = sum(num)
#     result = total/len(num)

#     return result
# print(mean(num))

def median(number):
    

   a = len(number)
   middle = a//2#fiing the middle of the input when divided by 2.
   #print(middle)
   print(sorted([middle+1]))
   print(sorted(number))
   print(a)
   print(sorted[middle-1])
   if a%2:
        return sorted(number)[middle]
   else:
         
      return sum(sorted(number)[middle-1:middle+1])/2


#print(median(num))

# #standard deviation
# def standard_deviation(list1):
#     length = len(num)
#     total = [i - mean(num)**2 for i in num]
#     final_result = total **0.5
#     total_sum = final_result/length
#     return total_sum

# def variance(num):
#     st = standard_deviation(num)
#     return st**2

# #mode
# def mode(num):
#     freq= {}
#     for i in num:
#         if i in num:
#             if i in freq.keys():
#                 freq[i]+=1#this is how we would be saving the highest number by im
#             else:
#                 freq[i]=1
#             max_key =max(freq, key = freq.get)
#             return max_key


# #prime numbers
# def prim(num):
#     if num<=1:
#         return False
#     if num==2:
#         return True
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
# print(prim(5))


 
# myfile =open('file i/name.txt', mode = 'r')
# #myfile.write('am writing this here because am a learner')
# # to write multiple lines
# #myfile.writelines(['this is line1\n', 'this is line2\n','\t this is a tab.'])
# text = myfile.read()
# print(text)
# # texts = myfile.readlines()
# for text in texts:
#  print(texts)


# with open('mary.txt', 'w')as paul:
#     paul.write('my name is paul')
# import ast
# d = {
#      "name":"paul"
#  }
# with open('des.txt', 'w') as paul:
#      paul.write(f'{d}')

# with open('des.txt', 'r') as mercy:
#      favour = mercy.read()
#      a = ast.literal_eval(favour)
#      print(type(a))

#f1 = open('mary.text', mode = 'r')
# #f1.write('i am cing')
# f2 = f1.read()
# print(f2)
# # f1 = open('john.text', mode ='w')
# f1.write('iam coming')
# f2 = f1.read()
# # f4 = open('john.text', mode='r')
# print(f2)
#customer_details ={"name":"name", "school":"eva"}
# with open('bank_app.text', mode= 'w')as stella:
#                  for key, value in customer_details.items():
#                     stella.write('%s:%s\n' %(key, value))
# my_dict={'name':10, 'amount':20, 'class':50}
# for key, value in my_dict.items():
#              print('%s:%s\n' % (key, value))
