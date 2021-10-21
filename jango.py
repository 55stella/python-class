# class DangoStudent():
#   def __init__(self, name, laptop):
#       self.name = name
#       self.computer = laptop

# mystudent = DangoStudent("Ejiro","mackbook")
# print(mystudent.name)
# print(mystudent.computer)


# class BankApp():
#     def __init__(self, name, balance):
#         if not isinstance(balance,(int, float)):
#             raise TypeError(f'Epected int or float but got  {type(balance)}')
#         self.name = name
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance+=amount
#         return self.balance
#     def name_tolower(self):
#         self.name = self.name.lower()
#         return self.name
# customer1 = BankApp('Tunde', 105.90)
# print(customer1.name_tolower())
# print(customer1.deposit(1000))



# class vehicle():
#      def __init__(self,max_speed, mileage):
#            self.max_speed = max_speed #mileage = distance
#            self.mileage = mileage




#      def  accerleration (self, time):
#           acerlerate = self.mileage*2/time**2#accerleration = distance/time^2
#           return acerlerate 

# b= vehicle(100,20)
# c= b.accerleration(10)
# print(c)
# print(b.max_speed)
# print(b.mileage)

#inheritance
class Employer():
    def __init__(self, name,salary, disignation):
        self.name = name
        self.salary = salary
        self.designation = disignation

    @property
    def bonus(self):
        bo = self.salary*0.1
        return self.salary+bo

a = Employer('tosin', 99, 'Q/A')
a.bonus
print(a.bonus)
# def report(self):
#       return (f'Hi{self.name}.your take home salary is {self.bonus}')
    #     c = (f'Hi{self.name}.your take home salary is {self.bonus}')
    #     print(c)
#here we are changing the bonus() method to become a property.so we remove the method ()sign in by calling the propert decleration
class supervisors(Employer):
    def __init__(self, name,salary, disignation,branch):
        self.branch=  branch
        super().__init__(name, salary, disignation)
a = Employer('tosin', 10, 'Q/A')
a.bonus
st2 = supervisors("tunde", 100000, 'accountant','sabo')
print(st2.bonus)
print(a.bonus)



# #tango with jango


# class vehicle():
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self. mileage = mileage
#     def accerleration(self, time):
#         a = self.mileage *2/time**2
#         return a


# b = vehicle(10,30)
# c= b.accerleration(10)
# print(c)         