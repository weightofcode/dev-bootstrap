# # Casting concept
# num = 3
# num = int(num)
# num1 = str(num)
# num2 = float(num)
# print(type(num), type(num1), type(num2))
# 
# a, b, c = "hi", 4, 3.5
# print(type(a), type(b), type(c))
# print(a,b,c)
# 
# d = e = f = "hi"
# print(d,e,f)
# 
# m = n = []
# m.append(1) # unintended side effect
# print("n:", n)
# 
# # Unpacking concept
# shopping_cart = ['salt', 'pepper', 'sugar'] 
# a, b, c = shopping_cart
# print(a,b,c)
# 
# a, b, c = "hi", 4, 3.5 
# print(a,b,c)
# print(a,b-c)
# 
# # global keyword
# x = 5
# def myfunc():
#     x = 3
#     print(x)
# myfunc()
# print(x)
# print('--------------')
# x = 5
# def myfunc():
#     global x
#     x = 3
#     print(x)
# myfunc()
# print(x)

# print('###############################################')
# 
# x = 3j
# print(x)
# print(type(x))
# 
# h = ['a', 'b', 'c'] # list
# print(h[1])
# j = ('a', 'b', 'c') # tuple - immutable
# print(j[1])
# k = {'a', 'b', 'c'} # set
# print(k)
# fk = ({'a', 'b', 'c'}) # frozen set - immutable
# print(fk)
# l = {'age':5, 'likes':'icecream'} # dict
# sl = dict(age=5, likes='icecream')
# print(l)
# print(sl)
# 
# # always use this syntax:
# # x = constructor((value))
# # when declaring these 'array' types
# # even for set or list
# 
# ba = bytearray(22)
# print(ba)
# ba = memoryview(bytes(22))
# print(ba)
# 
# r = range(5,12)
# print(r)
# 
# import random
# print(random.randrange(-2, 14))


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
# x = "hello world"
# print('hi in x:', 'hi' in x)
# 
# t = str(4+5+10)
# m = str(1)
# n = str(2)
# if m in t:
#     print('m=1 in t:', bool(m))
# if n not in t:
#     print('n=2 not in t:', bool(n))
# 
# # --------- SLICE ----------------
# x = "greetings"
# i = (x[3:6])
# j = x[:len(x)]
# print("i:", i, "len(i):", len(i))
# print("j:", j, "len(j):", len(j))
# 
# # --------- MODIFY ----------------
# name = '"Harald Konrad "'
# u = name.upper()
# print(u)
# l = name.lower()
# print(l)
# s = name.strip() # remove whitespace
# print(s)
# r = name.replace('a', 'u')
# print(r)
# 
# # --------- FORMAT ----------------
# age = 45
# txt = f"age is {age}"
# print(txt)
# price = 59
# # placeholder can include MODIFIER or Python code
# txt1 = f"price is {price:.2f} $" 
# print(txt1)
# txt2 = f"price is twice expensive {59 * 2} " 
# print(txt2)
# 
# # --------- ESCAPE CHARACTER ----------------
# txt = "we are the \"music makers\"! yeah!"
# print(txt)
# txt = "we are\t the\t \"music makers\"!\t yeah!" # tab as \t
# print(txt)
# 
# # --------- BOOLEAN ----------------
# def somefunc():         # functions
#     return False
# print(somefunc())
# 
# class myclass():        # objects of a class
#     def __len(self):
#         return 0
# myobj = myclass()
# print("bool(myobj):", bool(myobj))
# 
# 
# 
# # --------- OPERATORS ----------------
# # WALRUS
# print("WALRUS")
# nums = [1,2,3,4]
# if (count := len(nums)) > 2:
#     print(f"nums[] has {count} elements")
# 
# x = 5
# print("x = 5 : 1 < x < 10:", 1 < x < 10)
# 
# # IDENTITY
# print("IDENTITY")
# a = ['apple', 'banana']
# b = ['apple', 'banana']
# c = a
# print(a is c) # true
# print(a is b) # false
# print(a == b) # true (comparing content)
# 
# # MEMBERSHIP
# print("MEMBERSHIP")
# fruit = ["apple", "cherry"]
# a = "cherry"
# p = "pineapple"
# print("a in fruit", a in fruit)
# print("p not in fruit", not p in fruit)
# 
# # BITWISE
# print("BITWISE")
# a = 41
# b = 55
# print("55 << 1:", b << 1)
# print("41 ^ 55:", a ^ b)
# c = 6
# print("~6:", ~c)


# PYTHON COLLECTIONS ------------------
## 1. LIST ----------------------------

# constructor = list((0x4,0xb,0x0)) # Constructor (notice the () instead of [])

# state_machine = [True, False, True]
# print("LIST:", state_machine)
# r = state_machine[1:2] # slicing always returns a list
# print(r)
# random_data = [True, "0x45", False, 14, (35-15), len(state_machine), "hi", False, (len(state_machine) * (False/True)), True]
# print("Random Data LIST:", random_data, "Type of random_data:", type(random_data))
# print("random_data[-3]:", random_data[-3])
# print("random_data[2:7]", random_data[2:7])
# print("random_data[4:]", random_data[4:])
# print("random_data[-3:]", random_data[-3:])
# print("random_data[-3:2]", random_data[-3:2]) # empty list (the same as [7:2], when it should be [2:7])
# 
# num = [1,2,3,4,5]
# print("num is:", num)
# num[1:3] = [21,56]                      # slice [i:j]
# print("num[1:3] = [21,56] is:", num)
# num.insert(4, 0x22)                     # insert(i, v)
# print("num is now:", num)
# num.append(5)                           # append(v)
# num.extend(state_machine)               # extend(other_list) - append other_list
# num.remove(5)                           # remove(v) - only the first occurence
# num.pop(1)                              # pop(i) - last item without specifying i
# num.clear()                             # clear() - removes all list items
# del num                                 # del list
# 
# digits = [1,2,3]
# print("for d in digits:")
# for d in digits:                    # item in list
#     print(d)
# print("for i in range(len(digits)):")
# for i in range(len(digits)):        # i in range(len(list))
#     print(digits[i])
# print("while i < len(digits):")
# i = 0
# while i < len(digits):              # while i < len(list)
#     print(digits[i])
#     i += 1

# list COMPREHENSION
# we can write explicit for loop to create new list
albums_in_store = ["nirvana", "blues", "rock", "jazz"]
albums_to_buy = []
for album in albums_in_store:
    if "j" in album:
        albums_to_buy.append(album)
        print(albums_to_buy)

# or we can re-write the loop in a more compact way
# only if condition *evaluates* to True
albums_in_store = ["nirvana", "blues", "rock", "jazz"]
albums_to_buy = [album for album in albums_in_store if "j" in album]
print(albums_to_buy)
do_not_buy_nirvana = [album for album in albums_in_store if album != "nirvana"]
print(do_not_buy_nirvana)

# condition is optional
buy_everything = [album for album in albums_in_store]
print(buy_everything)
new_numbers = [nums for nums in range(10) if nums < 5]
print(new_numbers)

# item = item in iteration OR the outcome
old_digits = [1, 2, 3, 4, 5]
replace_all_digits_with_9 = [9 for digit in old_digits]
print(replace_all_digits_with_9)

# in case of outcome, it can be an expression too!
# [(value_if_true if condition) else (value_if_false) (for item in iterable)]
# [(return value if condition true) else (value_if_false) (for item in iterable)]
replace_digits = [2 if digit != 5 else 3 for digit in old_digits]
print(replace_digits)

# sort (numeric & alphabetic)
old_digits = [3,2,4,1,5]
old_digits.sort()
print("[3,2,4,1,5].sort() :", old_digits)
# sort reverse=True (descending)
old_digits = [3,2,4,1,5]
old_digits.sort(reverse = True)
print("[3,2,4,1,5].sort(reverse=True) :", old_digits)
# sort with function as key
def myfunc(v):
    return abs(v - 50)
numms = [100,50,32,85,14]
numms.sort(key = myfunc)
print("[100,50,32,85,14] sort(key = func) :", numms)

# reverse
old_digits.reverse()
print("[3,2,4,1,5].reverse() :", old_digits)
nums = [1,2,3,4,5]
nums.reverse()
print("[1,2,3,4,5].reverse() :", nums)

# copy (makes a copy)
some_nums = [1,2,3,4]
sn_copy = some_nums.copy()
print("[1,2,3,4].copy()", sn_copy)

# list
sn_list = list(some_nums)
print("list([1,2,3,4])", sn_list)

# slice :
sn_list = some_nums[:]
print("[1,2,3,4][:]", sn_list)

