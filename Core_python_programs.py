"""1) write a python program to display name,id&salary by taking input from the user it should print my name,is xyz,id is 12345, &salary is 100K"""
# emp_name=input("enter your name:")
# emp_id=input("enter your id:")
# emp_sal=input("enter your salary:")
# print(f"my name is {emp_name},id is {emp_id} and salary is{emp_sal}")
# print("my name is {},id is {} and salary is{}".format(emp_name,emp_id,emp_sal))






"""2)sum & avg of three numbers"""
"""method 1"""
# a=int(input("enter the 1st value:"))
# b=int(input("enter the 2nd value:"))
# c=int(input("enter the 3rd value:"))
# sum=a+b+c
# avg=(a+b+c)/3
# print(sum)
# print(avg)

"""method 2"""
# a,b,c=int(input("enter the 1st value:" )),int(input("enter the 2nd value:" )),int(input("enter the 3rd value:" ))
# sum=a+b+c
# avg=(a+b+c)/3
# print(sum)
# print(avg)

"""method 3"""
# a,b,c=[int(i) for i in input("enter the numbers:").split(',')]
# sum=a+b+c
# avg=(a+b+c)/3
# print("the sum is%d,the average is%d"%(sum,avg))





"""3)area of circle"""
"""method 1"""
# rad=float(input("enter the circle radius:"))
# area_of_circle=3.14*rad**2
# print(area_of_circle)
"""method 2"""
# import math
# r=float(input("enter the radius:"))
# area_of_circle=math.pi*r**2
# print(area_of_circle)





"""4)To print starting character of string """
# s=input("enter any string:")
# print("the entered character is:"+s[0])
# print("the entered character is:",s[0])




"""5)write a python program to join multiple strings together"""
# a,b,c=input("enter the three strings:").split(',')
# print(a+b+c)
# print(a+"  "+b+"  "+"  "+c)






"""6)write a python program to print cube of a given number """
"""method 1"""
# n=int(input("enter required cube number:"))
# print(n**2)
# print(n**3)
"""method 2"""
# n=int(input("enter any number:"))
# for i in range(1,n):
#     print(i**3)
"""method 3"""
# import math
# a=int(input("enter your number:"))
# print(math.pow(a,5))




"""7)write a python program to take multiple strings from the user and the sort them"""
# str=[]
# n=int(input("how many strings?"))
# for i in range(n):
#     s=input("enter a string")
#     str.append(s)
# str.sort()
# # print(str)
# # print(*str)
# for i in str:
#     print(i)

"""8)write a python program for evaluate a number"""
# num=eval(input("enter any numberr"))
# print(num,type(num))
# print("num=%d"%num)


"""9)write a python program for given number is even or odd"""
"""method 1"""
# n=int(input("enter any number"))
# if n%2==0:
#     print("it is an even number")
# else:
#     print("it is an odd number")

"""method 2"""
# for i in range(0,n,2):
#     print(i,end=" ")
    
# for i in range(1,n,2):
#     print(i)
"""method 3"""
# a=int(input("enter first number:"))
# b=int(input("enter last number:"))
# while(a<=b):
#     print(a)
#     a+=2


"""10)write a python program to print given number is even or odd,
  suppose the user enters the number is zero,
  then you should print you have entered zero number"""

# n=int(input("enter any number"))
# if n==0:
#     print("you entered zero number")
# elif n%2==0:
#     print("given number is even number")
# else:
#     print("given number is odd number")



"""11)to print 1 to 10 number"""
# for i in range( 1,11):
#     print(i)

while(a<=10):
    a=1
    print(a)
    a+=1








