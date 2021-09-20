"""arithmatic operaters"""

# a=float(input("enter the value of a:"))
# b=float(input("enter the value of b:"))
# print(f"the value of {a}+{b} is {a+b}")#the value of 23.0+23.0 is 46.0
# print(f"the value of {a}-{b} is {a-b}")#the value of 23.0-23.0 is 0.0
# print(f"the value of {a}*{b} is {a*b}")#the value of 23.0*23.0 is 529.0
# print(f"the value of {a}/{b} is {a/b}")#the value of 23.0/23.0 is 1.0

# print(f"the value of {a}%{b} is {a%b}")#the value of 23.0%23.0 is 0.0
# print(f"the value of {a}**{b} is {a**b}")#the value of 23.0**23.0 is 2.088046799984791e+31



"""floor division"""
# c=4//2
# print(c)#2
# d=4//2.0
# print(d)#2.0
# e=5/2
# print(e)#2.5
# f=4.0//2


"""assignment operator"""
# a=12
# print(a)#12
# b=13
# print(b)#13
# a=a+b
# print(a)#25
# a=a+a
# print(a)#50

# a=10
# a+=5
# print(a)#15
# a-=2
# print(a)#13
# a*=4
# print(a)#52
# a/=2
# print(a)#26.0
# a**=2
# print(a)#676.0

# p=int(input("enter the value of p:"))
# print(f"the value of p  is {p}")#the value of p  is 22

# p+=2
# print(f"the value of p after p+=2 is {p}")the value of p after p+=2 is 24

# p-=2
# print("the value of p after p-=2 is {}".format(p))the value of p after p-=2 is 22

# p*=2
# print("the value of p after p*=2 is {}".format(p))the value of p after p*=2 is 44
# p/=2
# print("the value of p after p/=2 is {}".format(p))the value of p after p/=2 is 22.0
# p**=2
# print("the value of p after p**=2 is {}".format(p))the value of p after p**=2 is 484.0


"""Relational/comparition operator"""

# a=int(input("enter the value of a:"))
# b=int(input("enter the value of b:"))
# print(f"the value of {a}<{b}is{a<b}")#the value of 2<3isTrue
# print(f"the value of {a}>{b}is{a>b}")#the value of 2>3isFalse
# print(f"the value of {a}<={b}is{a<=b}"#)the value of 2<=3isTrue
# print(f"the value of {a}>={b}is{a>=b}")#the value of 2>=3isFalse
# print(f"the value of {a}=={b}is{a==b}")#the value of 2==3isFalse
# print(f"the value of {a}!={b}is{a!=b}")#the value of 2!=3isTrue

      
# a=int(input("enter the value of a:"))
# b=int(input("enter the value of b:"))
# print("the value of %d<%d=%d"%(a,b,a<b))             #the value of 4<5=1
# print("the value of a=%d,b=%d a>b=%d"%(a,b,a<b))     #the value of a=4,b=5 a>b=1
# print("the value of a=%d,b=%d a>=b=%d"%(a,b,a>=b))   #the value of a=4,b=5 a>=b=0
# print("the value of a=%d,b=%d a<=b=%d"%(a,b,a<=b))   #the value of a=4,b=5 a<=b=1
# print("the value of a=%d,b=%d a>b=%d"%(a,b,a>b))     #the value of a=4,b=5 a>b=0 
# print("the value of a=%d,b=%d a==b=%d"%(a,b,a==b))   #the value of a=4,b=5 a==b=0
# print("the value of a=%d,b=%d a!=b=%d"%(a,b,a!=b))   #the value of a=4,b=5 a!=b=1


# """logical operators"""
# a=int(input("enter the value of a:"))
# b=int(input("enter the value of b:"))
# print(f"the value of {a<b} and {a>b} is{a and b}")       #the value of True and False is6
# print(f"the value of {a<b} or {a>b} is{a or b}")         #the value of True or False is5
# print(f"the value of {a<=b} or {a>=b} is{a or b}")       #the value of True or False is5
# print(f"the value of {a!=b} or {a==b} is{a or b}")       #the value of True or False is5
# print(f"the value of {a<b} after not is {not a<b}")      #the value of True after not is False
# print(f"the value of {a==b} after not is {not a==b}")    #the value of False after not is True
# print(f"the value of {a!=b} after not is {not a!=b}")    #the value of True after not is False

"""bitwise operator"""
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
print("the value of {} & {} is {}".format(a,b,a&b))           #the value of 5 & 6 is 4
print("the value of {} | {} is {}".format(a,b,a|b))           #the value of 5 | 6 is 7
print("the value of ~{} is {}".format(a,~a))                  #the value of ~5 is -6 
print("the value of ~{} is {}".format(c,~c))                  #the value of ~7 is -8  

"""  identity operator  """
a=4;b=[5];c=6;d=a;e=5;f=[5]
print(f"the value of {a} is {b}={a is b}")                        #the value of 4 is [5]=False
print(f"the value of {a} is {c}={a is c}")                        #the value of 4 is 6=False 
print(f"the value of {a} is {d}={a is d}")                        #the value of 4 is 4=True
print(f"the value of {a} is {e}={a is e}")                        #the value of 4 is 5=False   
print(f"the value of {b} is {f}={b is f}")                        #the value of [5] is [5]=False 
print(f"the value of {a} is not {b}=",a is not b)                 #the value of 4 is not [5]= True 
print(f"the value of {a} is not {c}=",a is not c)                 #the value of 4 is not 6= True  
print(f"the value of {a} is not {d}=",a is not d)                 #the value of 4 is not 4= False  
print(f"the value of {a} is not {e}=",a is not e)                 #the value of 4 is not 5= True  
print(f"the value of {b} is not {f}=",b is not f)                 #the value of [5] is not [5]= True


"""member ship operator"""
n=[1,2.3,'python']
print(n[0],type(n[0]))                                                 #1 <class 'int'>
print(n,type(n))                                                       #[1, 2.3, 'python'] <class 'list'>
print(n[1],type(n[1]))                                                 #2.3 <class 'float'>
print(n[2],type(n[2]))                                                 #python <class 'str'>
print(f"the value of {n[0]} is n is {n[0] in n}")                      #the value of 1 is n is True
print(f"the value of {n[1]} is n is {n[1] in n}")                      #the value of 2.3 is n is True 
print(f"the value of {n[2]} is n is {n[2] in n}")                      #the value of python is n is True  
print(f"the value of {'pytho'} not in n is{'pytho'}")                  #the value of pytho not in n ispytho 
print(f"the value of {'python'} not in n is{n[2] not in n}")           #the value of python not in n isFalse
print(1 not in n )                                                     #False
print(5 not in n)                                                      #True
print(4.5 not in n)                                                    #True
print('pytho'not in n)                                                 #True
print('python'not in n)                                                #False
