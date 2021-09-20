"""Number system"""

# a=5;b=4.6
# print(a,type(a))                                        #5 <class 'int'>
# print(b,type(b))                                        #4.6 <class 'float'>
# print(isinstance,(a,int))                               #<built-in function isinstance> (5, <class 'int'>)
# print(isinstance(a,int))                                #True
# print(isinstance(a,float))                              #False
# print(isinstance(a,bool))                               #False
# print(isinstance(b,float))                              #True



"""complex"""

# c=2j
# print(c)                         # 2j

# d=1+5j
# print(d,type(d))(1+5j)           # <class 'complex'>
# print(isinstance(d,complex))     # True

# e=0+0j
# print(e)        #0j

# f=(1-5j)
# print(f)        #(1-5j)
# g=(0-5j)
# print(g)        #-5j

# h=(0+(-3j))
# print(h)        #-3j

# j='0.1'+'0.2'
# print(j)          #0.10.2
# k=str(j)
# print(k)          #0.10.2
# n=float(2.2)+float(2.2)
# print(n)          #4.4
# print(4)             #4  
# print("4")           #4
# print('4')           #4
# print(+4)            #4
# print(+0.1)          #4
# print(+2+3j)         #(2+3j)
# print(-2+3j)         #(-2+3j)
# print(3j)            #3j



"""  decimal  """

# import decimal
# v=decimal(0.1)+decimal(0.1)
# print(v)


# from decimal import Decimal as D
# v=D('0.1')+D('0.1')
# print(v)                           #0.2

# a=2.5
# from fractions import Fraction as F
# print(F(a),type(F(a)))               #5/2 <class 'fractions.Fraction'>
 

"""binary"""

# a=bin(5)
# print(a,type(a))          #0b101 <class 'str'>

# x=0b101
# print(x,type(x))            #5 <class 'int'>

# n=0B101
# print(n,type(n))               #5 <class 'int'>


"""octal"""

# d=oct(19)
# print(d,type(d))           #0o23 <class 'str'>
# e=0o23 
# print(e,type(e))           #19 <class 'int'> 
# f=0O23
# print(f,type(f))           #19 <class 'int'>


"""hexa decimal"""

# g=hex(24)
# print(g,type(g))                       #0x18 <class 'str'>
# h=0x18
# print(h,type(h))                       #24 <class 'int'> 
# i=0X18
# print(i,type(i))                        #24 <class 'int'> 


"""  fractions  """

# from fractions import Fraction as F
# print(F,type(F))                 #<class 'fractions.Fraction'> <class 'abc.ABCMeta'>
# print(F('2.5'))                  #5/2
# print(F("2.5"))                  #5/2
# y=F(4.5)
# print(y,type(y))                 #9/2 <class 'fractions.Fraction'>
# print(F(5.0))                    #5
# v=F(5,15)
# print(v)                         #1/3



# print(1e0)                   #1.0
# print(4e0)                   #4.0
# print(4e1)                   #40.0
# print(4e2)                   #400.0
# print(12e2)                   #1200.0
# print(1.2e0)                   #1.2
# print(1.2e1)                   #12.0
# print(1.2e2)                   #120.0
# print(1.2e3)                   #1200.0
# print(1.2e4)                   #12000.0



# print(4*5)                     #20
# print(4**5)                    #1024
# print(4.5**5)                  #1845.28125    


# import math as M
# print(M.exp(3))             #20.085536923187668
# e=M.exp(1)
# print(e,type(e))            #2.718281828459045 <class 'float'>


"""int datatype"""
# n=2;m=3;o=5
# print(n,type(n))
# print(m,type(m))
# print(o,type(o))
"""float type"""
# p=2.3;q=3.4;r=5.6
# print(p,type(p))
# print(q,type(q))
# print(r,type(r))
"""string type"""

# a="hello"
# print(a)          #hello
# print(a,type(a))  #hello <class 'str'>
# n="python"
# m=int(n)
# o=float(n)
# print(n)
# print(m)            #ValueError: invalid literal for int() with base 10: 'pyhton'
# print(o)              #ValueError: could not convert string to float: 'python'


"""convert int-->float"""
# a=12
# print(a)
# print(int(a))
# print(float(a))
"""convert float-->int"""
# b=2.2
# print(b)
# print(float(b))
# print(int(b))


"""format"""
# k=1.1+2.2
# print('%f'%k)            #3.300000
# print('%1f'%k)           #3.300000
# print('%2f'%k)           #3.300000
# print('%3f'%k)           #3.300000
# print('%4f'%k)           #3.300000
# print('%1.f'%k)          #3
# print('%2.f'%k)          # 3
# print('%3.f'%k)          #  3
# print('%4.f'%k)          #   3
# print('%.1f'%k)          #3.3
# print('%.2f'%k)          #3.30
# print('%.3f'%k)          #3.300
# print('%.4f'%k)          #3.3000

# p=7
# print("%d"%p)              #7
# print(p)                   #7
# print("%f"%p)              #7.000000