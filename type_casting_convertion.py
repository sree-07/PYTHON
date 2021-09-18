"""int--->float,string"""
# a=7
# print(a,type(a))     #7 <class 'int'>
# b=float(a)
# print(b,type(b))    #7.0 <class 'float'>
# c=str(b)
# print(c,type(c))    #7.0 <class 'str'> 
 # x=10
# print("the value of x is",x)      #the value of x is 10
# print("the value of x is %d"%x)   #the value of x is 10
# z=str(x)
# print("the value of z is"+z)      #the value of z is10



"""float---->int,string"""
# a=12.5
# print(a,type(a))                    #12.5 <class 'float'>
# b=int(a)
# print(b,type(b))                    #12 <class 'int'> 
# c=str(b)
# print(c,type(c))                    #12 <class 'str'> 




"""string--->int,float"""
m="python"
print(m,type(m))        #python <class 'str'>
# n=int(m)
# print(n,type(n))      #ValueError: invalid literal for int() with base 10: 'python'
# o=float(m)
# print(o,type(o))        #ValueError: could not convert string to float: 'python'

# x="125"
# print(x,type(x))          #125 <class 'str'>
# y=int(x)
# print(x,type(y))          #125 <class 'int'> 
# z=float(x)
# print(z,type(z))          #125.0 <class 'float'>


