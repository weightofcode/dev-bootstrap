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

