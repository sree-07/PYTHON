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


# a={1:"",2:"python",3:5,4:3.3,5:[1,1],6:(3,4),7:{1,2},8:"yes"}
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
# print(w[0:8])              #python
# print(w[0:0])              #empty line

# print(w[0:-1])              #pytho
# print(w[0:-2])              #pyth
# print(w[0:-3])              #pyt
# print(w[0:-4])              #py
# print(w[0:-5])              #p
# print(w[0:-6])              #empty line



"""string methods(47)"""
"""'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',\
'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', \
'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 
'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix',\
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', \
'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'"""
                                                                                                                                                                                                                                                                                                                                                                                                              
# a="String methods"
# print(a.capitalize())                    #Stringmethods
# print(a.casefold())                      #stringmethods 
# print(a.swapcase())                        #sTRINGMETHODS
# print(a.title())                         #Stringmethods
# print(a.istitle())                       #True
# print(a.upper())                         #STRINGMETHODS 
# print(a.isupper())                       #False
# print(a.lower())                         #stringmethods 
# print(a.islower())                       #False
# print(a.center())                      #TypeError: center expected at least 1 argument, got 0
# print(a.center(10))                    #Stringmethods
# print(a.center(20))                    #     Stringmethods
# print(a.center(30))                    #          Stringmethods
# print(a.center(40))                    #                Stringmethods
# print(a.center(50))                    #                     Stringmethods





# print(a.count())                         #TypeError: count() takes at least 1 argument (0 given)
# print(a.count('a'))                       #0
# print(a.count('s'))                       #1
# print(a.count('r'))                       #1
# print(a.isspace())#false
# print(a.startswith("S"))#True
# print(a.startswith(" "))#false
# print(a.endswith(""))#true
# print(a.endswith("s"))#true
# print(a.endswith('m'))#false
# x="          string        "
# y="          string    *    "
# z="      *    string        "
# # print(x.strip())#string
# print(y.strip())#string    * 
# print(z.strip())#*    string
# print(x.lstrip())#string 
# print(y.lstrip())#string    *  
# print(z.lstrip())#*    string 
# print(x.rstrip())#           string
# print(y.rstrip())#           string    *
# print(z.rstrip())#      *    string 
# n="happy dusshera"
# a=print(n.encode())   #b'happy dusshera'
# n=b'happy dessra'
# print(n.decode())      #happy dusshra  
# g="happy diwali"
# print(g.index('d'))      #6





# print(g.rindex('i'))     #11
# r="hello google"
# print(len(r))               #12j
# print(r.find('g'))
# print(r.rfind('o'))         #12
# k="happy new year"
# print(k.replace("new","old"))   #happy old year
# print(k.replace("new",str(5)))  #happy 5 year 
# print(k.replace('e','a',1))     #happy naw year 
# print(k.replace('e','a',2))     #happy naw yaar  

# a="ipl14"
# print(a.isalnum())#True
# b="ipl "
# print(b.isalnum())  #False
# c="core python"
# print(c.isalpha())     #False
# d="corepython"
# print(d.isalpha())     #True
# print(d.isascii())     #True
  
# a={'x':1,'y':4,'z':6}
# print('{}{}{}'.format(*a))  #xyz
# print('{x}{y}{z}'.format(**a))  #146
# print('{x}{y}{z}'.format(**a))  #146
# print('{x}{y}{z}'.format_map(a))  #146




# x="hello\tworld"
# print(x.expandtabs())                    #hello   world
# print(x.expandtabs(10))                  #hello     world
# print(x.expandtabs(20))                  #hello               world
# y="h\te\tl\tl\to"
# print(y.expandtabs(5))                   #h    e    l    l    o
# print(y.expandtabs(10))                  #h         e         l         l         o
# print(y.expandtabs(15))                  #h              e              l              l              o
# print(y.expandtabs(20))                  #h                   e                   l                   l                   o
# print(y.expandtabs(25))                  #h                        e                        l                        l                        o
# q="2021"
# print(q.zfill(1))                          #2021
# print(q.zfill(2))                          #2021
# print(q.zfill(3))                          #2021
# print(q.zfill(4))                          #2021
# print(q.zfill(5))                          #02021
# print(q.zfill(10))                         #0000002021   
# i="\b"
# j="\n"
# g=""
# k=" "
# print(i.isprintable())#False
# print(j.isprintable())#False
# print(g.isprintable())#True
# print(k.isprintable())#True

# p="2"
# print(p.isdecimal())#True
# l="3e"
# print(l.isdecimal())#False
# w= "hello"
# print(w.ljust(30),"is my favorite fruit.")#hello                          is my favorite fruit.

"""  set methods (17) """
a=['add', 'clear', 'copy', 'difference', 'difference_update', 
'discard', 'intersection', 'intersection_update', 'isdisjoint', \
'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',\
 'symmetric_difference_update', 'union', 'update']

# print(len(a))
# a={1,2,3,4,5};b="python",3,5,7
# a.add(b)
# print(a)             #{1, 2, 3, 4, 5, ('python', 3, 5, 7)}

# b={1,2,3}
# b.clear()
# print(b)             #set()

# a={3,4,5,6}
# x=a.copy()
# print(a)         # {3, 4, 5, 6}

# a={1,2,3,4,5,6};b={3,5,7}
# print(a.difference(b))                      #{1, 2, 4, 6}
# print(b.difference(a))                      #{7}
# print(a-b)                                  #{1, 2, 4, 6}  
# print(b-a)                                  #{7}
# a.difference_update(b)
# b.difference_update(a)
# print(a)                                      #{1, 2, 4, 6}
# print(b)                                      #{7}

# x={11,22,33,44,55,66}
# x.discard(2)
# print(x)                                       #{33, 66, 22, 55, 11, 44}
# x.discard(33)
# print(x)                                       #{66, 22, 55, 11, 44}

# a={1,2,3,4,5};b={3,4,5,6,7};c={5,6,7,};d={3,5,7}
# print(a.union(b))                       #{1, 2, 3, 4, 5, 6, 7}
# print(a.intersection(b))                #{3, 4, 5}
# print(a.union(c))                       #{1, 2, 3, 4, 5, 6, 7}
# print(a.intersection(c))                #{5}
# # print(b.union(d))                       #{3, 4, 5, 6, 7}   
# print(b.intersection(d))                 #{3, 5, 7}
# # print(c.union(d))                       #{3, 5, 6, 7}
# print(c.intersection(d))                #{5, 7}
# print(a.intersection(b))                #{3, 4, 5}
# a.intersection_update(b)
# print(a)                                 #{3, 4, 5}


# x={12,23,34,22,66,};y={56,67,78};z={12,77,90,87,88}
# print("are a and b disjoint?",x.isdisjoint(y) )           #are a and b disjoint? True
# print("are a and b disjoint?",y.isdisjoint(a) )           #are a and b disjoint? True 
# print("are a and b disjoint?",x.isdisjoint(z) )           #are a and b disjoint? False
# print("are a and b disjoint?",y.isdisjoint(z) )           #are a and b disjoint? True 

# x={1,2,3,4,5,6,7};y={2,4,5,3,6,7};z={3,6,7}
# print(y.issubset(x))   #True
# print(y.issubset(z))   #False
# print(x.issubset(z))   #False
# print(y.issuperset(x))   #False
# print(y.issuperset(z))   #True
# print(x.issuperset(z))   #True


# c={6,5,8,14}
# c.pop()
# print(c)                    #{5, 6, 14}


# x={1,2,3,4,5,6,7}
# x.remove(3)
# print(x)           #{1, 2, 4, 5, 6, 7}

# a={1,2,3,4,5};b={3,4,5,6,7};c={5,6,7,8};d={3,5,7,9}
# a.update(b)
# b.update(c)
# c.update(d)
# print(a)      #{1, 2, 3, 4, 5, 6, 7}
# print(b)      #{3, 4, 5, 6, 7, 8}
# print(c)      #{3, 5, 6, 7, 8, 9}

# print(a.symmetric_difference(b))   #{1, 2, 6, 7}
# print(a)                           #{1, 2, 3, 4, 5} 
# a.symmetric_difference_update(b)
# print(a)                           #{1, 2, 6, 7} 



""" list datatype(11)"""
"""['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort' """
# print(len(a))
n=[1,2.2,"python",[11,22],(1,1),]
# print(n,type(n))              #[1, 2.2, 'python', [11, 22], (1, 1)] <class 'list'>
# print(n[0],type(n[0]))          #1 <class 'int'>
# print(n[1],type(n[1]))          #2.2 <class 'float'> 
# print(n[2],type(n[2]))          #python <class 'str'>
# print(n[3],type(n[3]))          #[11, 22] <class 'list'>
# print(n[4],type(n[4]))          #(1, 1) <class 'tuple'> 

n=[1,2.2,"python",[11,22],(1,1),]
# n.append("hello")
# print(n)             #[1, 2.2, 'python', [11, 22], (1, 1), 'hello']
# n.clear()
# print(n)     #[]
# m=n.copy()
# print(m)              #[1, 2.2, 'python', [11, 22], (1, 1)]
# print(n.count(5))#0
# print(n.count(1))#1

# m=[11,22,33,"web"]
# n.extend(m)
# m.extend(n)
# print(n)             #[1, 2.2, 'python', [11, 22], (1, 1), 11, 22, 33, 'web']
# print(m)             #[11, 22, 33, 'web', 1, 2.2, 'python', [11, 22], (1, 1), 11, 22, 33, 'web']

# m=[11,22,33,"web"]
# print(m.index())#TypeError: index expected at least 1 argument, got 0
# print(m.index(22))#1
# print(m.index("web"))#3
# m.insert(1,"55")#[11, '55', 22, 33, 'web']
# m.insert(4,"development")
# print(m)    #[11, 22, 33, 'web', 'development']

# m.pop()
# print(m)          #[11, 22, 33]
# m.pop(1)
# print(m) #[11, 33]

# m.remove("web")
# print(m)    #[11, 22, 33]

# n=[5,7,3,5,1]
# n.sort()
# print(n) #[1, 3, 5, 5, 7]
# n.sort(reverse=True)
# print(n)  #[7, 5, 5, 3, 1]
# n.sort(reverse=False)
# print(n)  #[1, 3, 5, 5, 7]  

# k=["se","tf","hg","ii"]
# k.sort()
# print(k)     #['hg', 'ii', 'se', 'tf']



"""   tuple methods(2)"""

"""'count', 'index'"""
# print(dir(tuple))
# a=(1,4,8,12,23,56,78,54,4,133,66,88,2,99)
# print(a.count(4))    #2
# print(a.index(54))   #7


""" dictionary methods(11)"""
""" 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 
'popitem', 'setdefault', 'update', 'values'"""
# print(dir(dict))
# h={1:1,2:"hello",3:2.2,4:(1,2),5:[2,2],6:{5,8}}
# print(h[1],type(h[1]))#1 <class 'int'>
# print(h[2],type(h[2]))#hello <class 'str'>
# print(h,type(h))#{1: 1, 2: 'hello', 3: 2.2, 4: (1, 2), 5: [2, 2], 6: {8, 5}} <class 'dict'
# print(h.keys())#dict_keys([1, 2, 3, 4, 5, 6])
# print(h.values())#dict_values([1, 'hello', 2.2, (1, 2), [2, 2], {8, 5}])
# print(h.items())#dict_items([(1, 1), (2, 'hello'), (3, 2.2), (4, (1, 2)), (5, [2, 2]), (6, {8, 5})])
# h.clear()
# print(h)             #{}

# a=[100,101,102,103,104,105,106]
# b=dict.fromkeys(a)
# print(b,type(b))      #{100: None, 101: None, 102: None, 103: None, 104: None, 105: None, 106: None} <class 'dict'>
# print(dict.fromkeys(a,"python"))   #{100: 'python', 101: 'python', 102: 'python', 103: 'python', 104: 'python', 105: 'python', 106: 'python'}

# h={1:1,2:"hello",3:2.2,4:(1,2),5:[2,2],6:{5,8}}
# print(h.get(2))      #hello
# print(h.get(10))       #None
# print(h[2])          #hello
# print(h[10])       #KeyError: 10
# h.pop(3)
# print(h)        #{1: 1, 2: 'hello', 4: (1, 2), 5: [2, 2], 6: {8, 5}}
# h.popitem()
# print(h)            #{1: 1, 2: 'hello', 3: 2.2, 4: (1, 2), 5: [2, 2]}


# h={1:1,2:"hello",3:2.2,4:(1,2),5:[2,2],6:{5,8}}
# h.update({7:"python"})
# print(h)          #{1: 1, 2: 'hello', 3: 2.2, 4: (1, 2), 5: [2, 2], 6: {8, 5}, 7: 'python'}
# h.setdefault(8,[11,22])
# print(h)          #{1: 1, 2: 'hello', 3: 2.2, 4: (1, 2), 5: [2, 2], 6: {8, 5}, 7: 'python'}




