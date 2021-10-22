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

# a=+1
# while(a<=10):
   
#     print(a)
#     a=1
"""12) write a python program to print from m to n even number"""
"""method 1"""
# m,n=[int(i)for i in input("enter start value,enter end value").split(',')]
# x=m
# if x%2!=0:x=m+1
# while(x<=n):
#   print(x)
#   x+=2

"""method 2""" 
# m=int(input("enter starting number:"));n=int(input("enter ending number:"))
# for i in range(m,n,2):
#   print(i)

"""method 3""" 
# m=int(input("enter starting number:"));n=int(input("enter ending number:"))
# while(m<=n):
#   print(m)
#   m+=2

"""13) write a python program to display 100 to 110"""
"""method 1"""
# for i in range(100,111):
#   print(i)

"""method 2"""
# a=range(100,111)
# for i in a:
#   print(i)

"""method 2"""
# m=int(input("enter m value:"))
# n=int(input("enter n value:"))
# while(m<=n):
#   print(m)
#   m+=1


"""14)write a program to display even numbers between 100 to 110"""
"""method 1"""
# for i in range(100,111,2):
#   print(i)

"""method 2"""
# m=int(input("first number:"))
# n=int(input("last number:"))
# for i in range(m,n,2):
#   print(m)
#   m+=2

"""15)write a python program to display letters in given string"""
"""method 1"""
n="python"
# for i in n:
#   print(i)
"""method 2"""
# n="python"
# for i in n[::1]:
#   print(i)
"""method 3"""
# n="python"
# for i in n[::2]:
#   print(i)

"""16)write a python program for sum of listed numbers"""
"""method 1"""
# l=[5,10,15,20,25,30]
# sum=0
# for i in l:

#   sum+=1
# print("no.of elements present inside the list is=",sum)

"""method 2"""
# import math
# a=[10,20,30]
# print(a[0]+a[1]+a[2])
# print(sum(a))

"""17)write a python program multiplication table"""
# n=int(input("multiplication of which table:"))
# for i in range(1,11):
#   print(n,"x",i,"=",n*i)

"""18)write a program for check element present in the list or not"""
# n=[1,4,7,9,11,45,66,98,23,42]
# f=int(input("which element you want to find?"))
# for i in n:
#   if f in n:
#     print("the value is found")
#     break
#   elif f not in n:
#     print("the value not found")
#     break

"""19) write a python program for break loop"""
# n=0
# while(n<10):
#   n+=1
#   if n==7:
#     pass
#   print(n)

"""20) Not to display with continue"""
"""type_1"""
# n=0
# while n<10:
#   n+=1
#   if n>=6:
#     continue
#   print(n)

"""type_2"""
# n=0
# while n<10:
#   n+=1
#   if n<5:
#     continue
#   print(n)

"""type_3"""
# n=0
# while n<10:
#   n+=1
#   if n>5:
#     continue
#   print(n)


"""type_4"""
# n=0
# while n<10:
#   n+=1
#   if n>=5:
#     continue
#   print(n)


"""21)retrive_only_negative"""
"""1st_type"""
# n=[2,4,6,-4,-3,-1,0,7]
# n.sort()
# for i in n:
#   if(i<0):
#     print(i)
"""2nd_type"""
# n=[2,4,6,-4,-7,-9]
# for i in n:
#   if(i>0):
#     print(i)
#   else:
#     pass









