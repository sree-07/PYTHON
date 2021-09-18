""" ways to assign valid variables"""
# a=1
# B=2
# _c=3
# _1=4
# c_a=5
# v_1=6
# _=7
# x_y3=8
# c_c_1=9
# t1=10
# print(a)                #1
# print(B)                #2
# print(_c)               #3
# print(_1)               #4
# print(c_a)              #5
# print(v_1)              #6
# print(_)                #7
# print(x_y3)             #8
# print(c_c_1)            #9
# print(t1)               #10
"""  ways to assign variables  """
'''  1st way  '''
# a=1
# b=2
# c=3
# d=4
# e=5
# print(a)                                    #1
# print(b)                                    #2
# print(c)                                    #3
# print(d)                                    #4
# print(e)                                    #5
# print(a),print(b),print(c),print(d),print(e)
# print(a);print(b);print(c);print(d);print(e)
# print(a,b,c,d,e)                            #1 2 3 4 5



'''2nd way'''

#  a=1,b=2,c=3,d=4,e=5            #SyntaxError: cannot assign to literal
# a=1;b=2;c=3;d=4;e=5
# print(a),print(b),print(c),print(d),print(e)
# print(a,b,c,d,e)                 #1 2 3 4 5
# print(a,b,c,d,e,f)               #NameError: name 'f' is not defined

'''3rd way'''
# a,b,c,d,e=1,2,3,4,
# print(a,b,c,d,e)   #ValueError: not enough values to unpack (expected 5, got 4)
# a,b,c,d=1,2,3,4
# print(a,b,c,d,)      #1 2 3 4


'''4th way'''
a=b=2;c=d=3
print(a,b,c,d)