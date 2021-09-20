"""$$$    datatypes(17)    $$$"""
"""int,float,string,none,bool,list,set,dictionary,string"""
    
"""int datatype"""
# n=2;m=3;o=5
# print(n,type(n))
# print(m,type(m))
# print(o,type(o))

"""convert int-->float"""
# a=12
# print(a)
# print(int(a))
# print(float(a))

"""float datatype"""
# p=2.3;q=3.4;r=5.6
# print(p,type(p))
# print(q,type(q))
# print(r,type(r))

"""convert float-->int"""
# b=2.2
# print(b)
# print(float(b))
# print(int(b))

"""string datatype"""

# a="hello"
# print(a)          #hello
# print(a,type(a))  #hello <class 'str'>

'''convert str-->int,float'''
# n="python"
# m=int(n)
# o=float(n)
# print(n)
# print(m)            #ValueError: invalid literal for int() with base 10: 'pyhton'
# print(o)              #ValueError: could not convert string to float: 'python'


# s="hello"
# print(s)                   #hello
# print(s[0])                #h
# print("%c"%s[0])           #h
# print("%c"%s[1])           #e
# print("%c"%s[2])           #l
# print("%c"%s[3])           #l
# print("%c"%s[4])           #o
# # print("%c"%s[5])          #IndexError: string index out of range
# print("%c"%s[-1])          #o
# print("%c"%s[-2])          #l
# print("%c"%s[-3])          #l
# print("%c"%s[-4])          #e
# print("%c"%s[-5])          #h

"""None datatype"""
# b=None
# print(b,type(b))        #None <class 'NoneType'>

"""boolean datatype"""
# a=True
# print(a,type(a))              #True <class 'bool'>
# b=False
# print(b,type(b))              #False <class 'bool'>
# print(3<5)                     #True
# print(3>5                      #False


"""List datatype"""
# a=[]
# print(a,type(a))                  #[] <class 'list'>

# p=["sri",23,1.0,None,True]
# print(p,type(p))                      #['sri', 23, 1.0, None, True] <class 'list'>
# print(p[0],type(p[0]))                #sri <class 'str'>
# print(p[1],type(p[1]))                #23 <class 'int'>
# print(p[2],type(p[2]))                #1.0 <class 'float'>
# print(p[3],type(p[3]))                #None <class 'NoneType'>
# print(p[4],type(p[4]))                #True <class 'bool'>
# print(p[5],type(p[5]))                #IndexError: list index out of range

# r=[4,3.1,"python"]
# r[0]="H"
# r[2]="programming"
# print(r)                    #['H', 3.1, 'programming']


"""  Tuple datatype  """
# a=(1.1,2,'hello',)
# print(a,type(a))            #(1.1, 2, 'hello') <class 'tuple'>
# print(a[-1])                #hello

# m=('apple',"moto","onle+","nokia","mi","xiomi","vivo","oppo")
# print(m)                      #('apple', 'moto', 'onle+', 'nokia', 'mi', 'xiomi', 'vivo', 'oppo')

# n="hello","python"
# print(n,type(n))         #('hello', 'python') <class 'tuple'>
# print(n[0])              # hello


""" set datatype"""
# a={}
# print(a,type(a))           #{} <class 'dict'>
# b={1,2,3}
# print(b,type(b))           #{1, 2, 3} <class 'set'>
# c={3,5.5,"hi",("hey",9)} 
# print(c,type(c))           #{('hey', 9), 3, 'hi', 5.5} <class 'set'>
# n={1,2,3}
# print(n[1])                  #TypeError: 'set' object is not subscriptable


# d={1,3,5}
# print(d,type(d))         #{1, 3, 5} <class 'set'>
# k=frozenset(d)
# print(k)                 #frozenset({1, 3, 5})
# print(k,type(k))         #frozenset({1, 3, 5}) <class 'frozenset'>
# print(k[1])               #TypeError: 'frozenset' object is not subscriptable

"""    dictionary datatype   """
# book={1:"python",2:"html",3:"css",4:"javascript"}
# print(book)                    #{1: 'python', 2: 'html', 3: 'css', 4: 'javascript'}
# print(book,type(book))         #{1: 'python', 2: 'html', 3: 'css', 4: 'javascript'} <class 'dict'>
# print(book[3])                 #css


a={1:"",2:"python",3:5,4:3.3,5:[1,1],6:(3,4),7:{1,2},8:"yes"}
# print(a[1],type(a[1]))                 # <class 'str'>
# print(a[2],type(a[2]))                 #python <class 'str'>  
# print(a[3],type(a[3]))                 #5 <class 'int'>  
# print(a[4],type(a[4]))                 #3.3 <class 'float'>
# print(a[5],type(a[5]))                 #[1, 1] <class 'list'>
# print(a[6],type(a[6]))                 #(3, 4) <class 'tuple'>
# print(a[7],type(a[7]))                 #{1, 2} <class 'set'> 
# print(a[8],type(a[8]))                 #yes <class 'str'>

# print(a,type(a))           #{1: '', 2: 'python', 3: 5, 4: 3.3, 5: [1, 1], 6: (3, 4), 7: {1, 2}, 8: 'yes'} <class 'dict'>
# print(a.keys())            #dict_keys([1, 2, 3, 4, 5, 6, 7, 8])
# print(a.values())          #dict_values(['', 'python', 5, 3.3, [1, 1], (3, 4), {1, 2}, 'yes'])
# print(a.items())           #dict_items([(1, ''), (2, 'python'), (3, 5), (4, 3.3), (5, [1, 1]), (6, (3, 4)), (7, {1, 2}), (8, 'yes')])

# t=range(5)
# print(t,type(t))             #range(0, 5) <class 'range'>

# z=b"hello"
# print(z,type(z))              #b'hello' <class 'bytes'>
# d=bytearray(b"hello")
# print(d)                     #bytearray(b'hello')

""" string datatype"""
# a="hello python programming"
# print(a,type(a))                #hello python programming <class 'str'>
# print(len("python programing"))   #17
a="python"
# print(a[0])         #p
# print("python"[0])    #p
# print("python"[1])    #y 
# print("python"[2])    #t
# print("python"[3])    #h
# print("python"[4])    #o
# print("python"[5])    #n
# print("python"[6])    #IndexError: string index out of range
# print("python"[-1])    #n
# print("python"[-2])    #o
# print("python"[-3])    #h
# print("python"[-4])    #t
# print("python"[-5])    #y
# print("python"[-6])    #p
# print("python"[-7])    #IndexError: string index out of range

w="python"
# print(w[:])              #python
# print(w[0:])             #python
# print(w[0:6])            #python
# print(w[-6:6])           #python
# print(w[0:1])              #p
# print(w[0:2])              #py
# print(w[0:3])              #pyt
# print(w[0:4])              #pyth
# print(w[0:5])              #pytho
# print(w[0:6])              #python
# print(w[0:7])              #python
# print(w[0:8])             #python
# print(w[0:0])              #empty line

print(w[0:-1])
print(w[0:-2])
print(w[0:-3])
print(w[0:-4])
print(w[0:-5])
print(w[0:-6])
