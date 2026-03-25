"""
# Casting concept
num = 3
num = int(num)
num1 = str(num)
num2 = float(num)
print(type(num), type(num1), type(num2))

a, b, c = "hi", 4, 3.5
print(type(a), type(b), type(c))
print(a,b,c)

d = e = f = "hi"
print(d,e,f)

m = n = []
m.append(1) # unintended side effect
print("n:", n)

# Unpacking concept
shopping_cart = ['salt', 'pepper', 'sugar'] 
a, b, c = shopping_cart
print(a,b,c)

a, b, c = "hi", 4, 3.5 
print(a,b,c)
print(a,b-c)

# global keyword
x = 5
def myfunc():
    x = 3
    print(x)
myfunc()
print(x)
print('--------------')
x = 5
def myfunc():
    global x
    x = 3
    print(x)
myfunc()
print(x)

print('###############################################')

x = 3j
print(x)
print(type(x))

h = ['a', 'b', 'c'] # list
print(h[1])
j = ('a', 'b', 'c') # tuple - immutable
print(j[1])
k = {'a', 'b', 'c'} # set
print(k)
fk = ({'a', 'b', 'c'}) # frozen set - immutable
print(fk)
l = {'age':5, 'likes':'icecream'} # dict
sl = dict(age=5, likes='icecream')
print(l)
print(sl)

# always use this syntax:
# x = constructor((value))
# when declaring these 'array' types
# even for set or list

ba = bytearray(22)
print(ba)
ba = memoryview(bytes(22))
print(ba)

r = range(5,12)
print(r)

import random
print(random.randrange(-2, 14))
"""


print('###############################################')

# a = """
# this is a multi-line string
# really, it is a string
# """
# print(a)
# 
# b = '''
# this is also a multi-line string
# with single quotes
# '''
# print(b)
# 
# # loop strings (arrays of chars)
# c = "hello"
# print(c[2])
# print(c)
# for i in c:
#     return(i)
# 
# # str length
# print('length of c:', len(c))

# check str
x = "hello world"
print('hi in x:', 'hi' in x)

t = str(4+5+10)
m = str(1)
n = str(2)
if m in t:
    print('m=1 in t:', bool(m))
if n not in t:
    print('n=2 not in t:', bool(n))

# --------- SLICE ----------------
x = "greetings"
i = (x[3:6])
j = x[:len(x)]
print("i:", i, "len(i):", len(i))
print("j:", j, "len(j):", len(j))

# --------- MODIFY ----------------

name = '"Harald Konrad "'
u = name.upper()
print(u)
l = name.lower()
print(l)
s = name.strip() # remove whitespace
print(s)
r = name.replace('a', 'u')
print(r)

# --------- FORMAT ----------------
age = 45
txt = f"age is {age}"
print(txt)
price = 59
# placeholder can include MODIFIER or Python code
txt1 = f"price is {price:.2f} $" 
print(txt1)
txt2 = f"price is twice expensive {59 * 2} " 
print(txt2)
