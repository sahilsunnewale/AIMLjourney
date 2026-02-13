# # # #ans1 = int(5+10) #casting
# # #  ans2 = 10.20 #conversopm
# # # # # # # print(ans1 ,type(ans1))
# # # # # # # print(ans2 ,type(ans2))

# # # # # # # # Name=input("enter your name:")
# # # # # # # # Age=int(input("enter your age:"))
# # # # # # # # print("your name is ",Name,"and your age is",Age);

# # # # # # # a=int(input("enter the number:"))
# # # # # # # b=int(input("enter the number:"))
# # # # # # # sum=a+b,a*b,a-b,a/b
# # # # # # # print(sum)   
# # # # # # age=int(input("enter your age"))
# # # # # # if age <13:
# # # # # #     print(child)
# # # # # # elif (age >=13 and age < 18):
# # # # # #     print("teenager")
# # # # # # else:
# # # # # #     print("adult")
# # # # # s=int(input("ENter a no here:"))
# # # # # if(s%2==0):
# # # # #     print("even")
# # # # # else:
# # # # #     ("odd")
# # # # n=int(input("NUMBER ENTER KARO BE"))
# # # # for n in range(5):
# # # #     for i in range(1):
# # # #         i=1
# # # # while(i<=10):
# # # #     print(n*i)
# # # #     i+=1


# # # i=1
# # # while(i<=10):
# # #     if(i%10==0):
# # #         break
# # #     print(i)
# # #     i+=1
# # # print("outside ayaa")

# # # def new(a,b):
# # #     s=a+b
# # #     return s
# # # ans=new(3,6)
# # # print(ans)
# # #for user input
# # def new(a,b):
# #     s=a+b
# #     return s
# # x=int(input("enter a number x"))
# # y=int(input("enter a number y"))
# # ans=new(x,y)
# # print("Answer =",ans)

# def calc_factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#         return fact
# n=int(input("enter no,s:"))

# print(calc_factorial(n))
# def ML(n):
#     n = str(n)        # convert number to string
#     for digit in n:   # go through each digit
#         print(digit)

# num = int(input("Enter a number: "))
# ML(num)()
#oddsbers
# i=0
# while(i<10):
#     i+=1
#     if(i % 2==0):
#         continue;
#     print(i)
# def arrival():
#     return "new collection"
# message=arrival();
# print(message)
#stringd s are immutable we not chsngr the vslue of strings by index operston

# s = "madam"

# rev = ""
# for i in range(len(s) - 1, -1, -1):
#     rev = rev + s[i]

# if s == rev:
#     print("Palindrome string")
# else:
#     print("Not a palindrome")
    
#     s = "I love python"
# count = 1

# for ch in s:
#     if ch == " ":
#         count += 1

# print("Number of words:", count)


#lists are mutable means we can change the particular value with index assignning 
# new=[99,48,78,'as',89]
# print(new[3])
#lists methods
# nums=[50,32,1,40]
# nums.append(30)
# print(nums)
# nums.insert(2,30)
# print(nums)
# nums.sort()
# print(nums)
# nums.reverse()
# print(nums)

# lit=[39,40,20,30,44]
# x=30
# count=0
# for val in lit:
#     if (val==x):
#         print(f"{x}value of x is founs{idx}")
#         break
#     idx=+1
#find largets no in list
# num=int(input("enter the no of list"))
# list=[]
# for i in range(num):
#     num=
# largest=[0]
# for i in []:
#     if i > largest:
#         largest = i
#         print("largets no list",largest)

# n = int(input("Enter number of elements: "))

# lst = []

# for i in range(n):
#     num = int(input("Enter number: "))
#     lst.append(num)

# largest = lst[0]

# for i in lst:
#     if i > largest:
#         largest = i

# print("Largest number in list =", largest)
# list1=[]
# list2=[]
# n1=int(input("enter the value of list:"))
# for i in range(n1):
#     num=int(input("enter the number"))
#     list1.append(num)
# n2=int(input("enter the value of list 2:"))
# for i in range(n2):
#     num=int(input("enter the number"))
#     list2.append(num)
            
# merged=list1+list2
# merged.sort()
# print("merged list of combine list new one",merged)

# new = {
#      "name": "sahil sunnewale",
      



# }

# print(new.keys())
#sets of python 
# s={1,2,3,3,3,4,4,209.0,} #here in set duplicates are avoided and they written in singles on /op and they are muatbles
# s.add(4)
# print(s)
# s.remove(2)
# print(s)
# s={2,3,2,4,5,}
# a={2,2,4,7,8}
# # print(s.union (a))#union set of two set
# print(s.intersection(a))#
#add unique value through set in listss
# listhai = [
#     ("sahil", "engineer"),
#     ("arshad", "salesman"),
#     ("moin", "bussiness man"),
#    ( "amir", "engineer"),
#    ( "newalice","salesman"),
# ]#now above this are all tuples in listhai name dictonary so we are making a new set for uniques values of profesion ok
#for accesing we are applying a for looop ]
# courses_set = set()
# for tup in listhai:
# #     print(tup[0])# tup at inddex is name
#    courses_set.add(tup[1])#tup for indesx 1 profession #and then we add cpuser st in all uniques
# print("your professions ",courses_set)
#now for which studet is in enrolled bussiness man
# for name,course in listhai:
#     if(course == "bussiness man"):
        
#         print(name)
# n = int(input("Enter number of elements: "))

# t = ()
# for i in range(n):
#     num = int(input("Enter number: "))
#     t = t + (num,)

# even = ()
# odd = ()

# for i in t:
#     if i % 2 == 0:
#         even = even + (i,)
#     else:
#         odd = odd + (i,)

# print("Original tuple:", t)
# # print("Even numbers tuple:", even)
# # print("Odd numbers tuple:", odd)
# # s = input("Enter a string: ")

# # unique_chars = set(s)

# # print("Unique characters are:")
# # for ch in unique_chars:
# #     print(ch, end=" ")

# # print("\nCount of unique characters:", len(unique_chars))


# def add (a, b):
#     return a + b
# print(add(5, 4))

# def square(n):
#     return n*n
# print(square(4))
# def subtract(a,b):
#     return a-b
# print(subtract(4 ,3))


# def even_odd(n):
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"
# print(even_odd(6))
# def even_odd():
#     n=int(input("enter the number here:")) 
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"
# print(even_odd())
# def count_vowels(s):
#     count=0
#     for ch in s:
#         if ch in "aieouaAEIOU":
#             count+=1
#             return count 
# print(count_vowels("sahil"))

# def digits(n):
#     count=0

#     for ch in n:
#         if n== (0,n):
#             count+=1
        
#             return n;
# print(digits("ad45"))


# 

# class Product:

#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def get_info(self):
#         print(f"price of {self.name}is rs.{self.price}")

    
# p1=Product("mobile",10_000)
# p2=Product("laptop",45_00)
# p1.get_info()
    

#oops concept encapsulations
# class Bankaccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance

# newacc1=Bankaccount("sahils",40000)
# print(newacc1.name,newacc1.balance)
        
#now this are public for private we can us in python _underscore for this private and protected and we can also 
#acces the private prtoedvted key in python BUT NOT IN JAVA AND C C++ WE  CAN ACCCES SUISNG __ UNDERSCPDE PRINT OBJECT
# class Bankaccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self._balance=balance #now this is protected

# newacc1=Bankaccount("moin",40000)
# print(newacc1.name,newacc1._balance)#accesble protected by this _
#now for privaate key acces we use special fun in pyhton is getter snd setter
# class schoolnew:
#     def __init__(self,name,marks):
#         self.name=name
#         self.__marks=marks#private by __
#         #now this private key is acces by only fun using gett and sett
#         def get_marks(self):
#             return self.__marks
# scoresem1=schoolnew("arshad",80.0)
# print(scoresem1.name,scoresem1.get_marks)
#now we are doing inherit means we are learning inheritance now 
# class Sunnewale:
#         start_time="10am"
#         end_time="6pm"
#         def change_time(self,new_end_time):
#                 self.end_time = new_end_time
# class teacher(Sunnewale):
#         def __init__(self,subject):
#                 self.subject=subject
# class kids(Sunnewale):
#         def __init__(self,member):#this is constructor see
#                 self.member=member

# bache=kids("Sahil ayaan")   
# print(bache.member)             
                
        
# t1 = teacher("Math")
# t1.change_time("5pm")
# print(t1.subject,t1.start_time,t1.end_time)
# class A:
#     def show(self):
#         print("This is parent")

# class B(A):
#     def display(self):
#         print("This is child")

# obj = B()
# obj.show()
# obj.display()
#MUTLIPLE INHEERIANCE
# class Teacher:
#     def __init__(self,salary):
#         self.salary=salary
# class student:
#     def __init__(self,gpa):
#         self.gpa=gpa
# class TA(Teacher,student):
#     def __init__(self,salary,gpa,name):
#         super().__init__(salary) 
#         student.__init__(self,gpa)
#         self.name=name
# new1=TA(10_000,9.4,"sahil")
# print(new1.name,new1.gpa,new1.salary)
# class bankaccount:
#     def __init__(self,accountno, name,balance):
#         self.accountno=accountno
#         self.name=name
#         self.balance=balance
#         def deposit(self,amount):
            
            
        
# f =open("new.txt","w")
# data =f.readline()
# print(data)
# f.close()
# f.write("this our new texxt which is repalce by new twxt in write fun,\n this isnnenxt line.")
# f.write("ne")
# ("new.txt","r+")as f:
    # content=f.write("new filw foe read write"\n "this our secounf line")
# f= open("new.txt","r+")
# f.write("python file operations\n")
# f.write("new line of python")
# f.close()
# data= True
# line = 1
# word="school"
# with open("new.txt","r")as f:
#     while data:
#         data=f.readline()
#         if(word in data):
#             print (f"{word} found word at line{line}")
#             break
#   
#       line+=1

# try:
#     x=int(input("enter the no x:"))
#     ans=10/x

#     # print(f"ans=",{ans})
# except ZeroDivisionError:
#     print(f"cant be exuxte")
# else:

#     print(f"ans={ans}")
# finally:
#     print("end f program") 
# example of dictonary

# def airportsystem():

#      flightnumber=int=[]
#      cost=[5000,3000,2000]
#      flighthours=[10,12,1,2,3]
#      return 0;






 

# yourflight={"flghtnumber":flightnumber,"cost":cost,"hours":flighthours
            

# }
# print(yourflight)
# def airportsystem():
#     flightnumber = []
#     n = int(input("How many flights? "))

# for i in range(n):
#     fn = int(input("Enter flight number: "))
    


#     cost = [5000, 3000, 2000]
#     flighthours = [10, 12, 3]

#     for i in range(len(flightnumber)):
#         print(f"Flight No: {flightnumber[i]}, Cost: {cost[i]}, Hours: {flighthours[i]}")

def main():
    airportsystem()

main()

flightnumber = []

n = int(input("How many flights? "))

for i in range(n):
    fn = int(input("Enter flight number: "))
    flightnumber.append(fn)

print("Flights:", flightnumber)

