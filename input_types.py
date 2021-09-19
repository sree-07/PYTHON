# n=input("enter your name---")
# print("my name is"+n)            #my name issrikanth 
# print("my name is",n)            #my name is srikanth
# p=int(input("enter your number"))
# print("my contact nuber is",p)   #my contact nuber is 950593030
# h=float(input("enter your height"))
# print("my height is",h)          #my height is 4.0 


""" ways to print the input types"""

# '''1st way'''
# name=input("enter your name:")
# age=int(input("enter your age:"))
# height=float(input("enter your height:"))
# print(name,age,height)                          #ss 23 6.0
# print(age,name,height)                          #23 ss 6.0
# print(height,name,age)                          #6.0 ss 23


# '''2nd way'''
# name=input("enter your name:")
# age=int(input("enter your age:"))
# height=float(input("enter your height:"))
# print("your name is",name,"your age is ",age,"your height is",height)#your name is srikanth your age is  23 your height is 6.0



"""3rd way"""
# print("enter your name is"+name,"your age is",age,"your height is",height)#enter your name issrikanth your age is 23 your height is 6.0

"""4th way"""
# print("enter your name is"+"  "+name,"your age is",age,"your height is",height)#enter your name is  srikanth your age is 23 your height is 6.0

"""5th way"""
# name=input("enter your name")
# age=input("enter your age")
# height=input("enter your height")
# # name="srikanth";age=23;height=6.0
# print("my name is %s" "my age is%d" "my height is%f" %(name,age,height))


"""6th way"""
# name="srikanth";age=23;height=6
# print("my name is {} and my age is {} and my height is {}".format(name,age,height))#my name is srikanth and my age is 23 and my height is 6


"""7th way"""
# name="srikanth";age=23;height=6
# print("my name is {2} and my age is {1} and my height is {0}".format(name,age,height))#my name is 6 and my age is 23 and my height is srikanth

"""8th way"""
# name=input("enter your name")
# age=input("enter your age")
# height=input("enter your height")
# print(f"my name is {name} and my age is {age} and my height is {height}")#my name is srikanth and my age is 23 and my height is 6

