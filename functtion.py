# def cal_sum(a,b):
#     sum=a+b
#     print(sum)
#     return sum
# cal_sum(5,10)
# cal_sum(20,45)
# cal_sum(4,8)
# def cal_avg(a,b,c):
#     sum=a+b+c
#     avg=(a+b+c)/3
#     print("the sum of this number is =")
#     print(avg)
#     return avg
# cal_avg(3,4,5)
# cal_avg(45,67,22)

# def even(n):
#     n=int(input("enter the number"))
#     if(n%2==0):
#         print("the numer iprint_lenths even")
#     else:
#         print("the number is not even because the num,ber that not be divided by 2")
        
# even(10)n
 
 
# cities=["delhi","amdhanpur"]
# heroes=["salamnkhan","ritikrosan"]
# print(heroes[0],end=" ")
# print(heroes[1],end=" ")
# def print_length(list):
#     print(len(list))
    
# # print_length(cities)  
# def print_list(list):
#     for item in list:
#         print(item,end=" ")  
# print_list(heroes)        
# n=5
# fact=1
# for i  in range(1,n+1):
    
#     fact*=i
#     print(fact)
# def cal_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact =fact*i
#         print(fact)
# cal_fact(6) 
# def convertor(usd_var):
    
#     inr_val=usd_var * 83
#     print(usd_var,"usd=",inr_val,"INR")
# convertor(1000)

# input=int(input("enter the number"))
# def check_even_or_odd(input):
#     if(input % 2==0):
#         print("the number is even")
#     else:
#         print("odd")
# check_even_or_odd(input)
# class Student:
#     def __init__(self,fullname,marks):
#         self.name= fullname
#         self.marks=marks
#         print(self)
#         print("adding new studdent a data bases")
    
     
    
# s1=Student("karan",45)
# print(s1.name, s1.marks)


# s2=Student("arjun",46)
# print(s2.name,s2.marks)
class Student:
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        print(self)
        print("Adding new student to the database")
    
s1 = Student("Karan", 45)
print(s1.name, s1.marks)

s2 = Student("Arjun", 46)
print(s2.name, s2.marks)
