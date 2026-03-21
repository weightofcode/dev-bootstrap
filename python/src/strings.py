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
name = 'Harald, Konrad '
print(name, "original string")
u = name.upper()
print(u, "upper")
l = name.lower()
print(l, "lower")
s = name.strip() # remove whitespace
print(s, "strip")
r = name.replace('a', 'u')
print(r, "replace")
sp = name.split(",")
print(sp, "split")
first = name.split(",")[0]
print(first, "split(',')[0]")
