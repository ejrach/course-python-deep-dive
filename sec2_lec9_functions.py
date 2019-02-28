from math import sqrt

# list
s = [1, 2, 3]
print(len(s))


print(sqrt(4))

# define the function
def func_1():
    print("running func_1")

# invoke the function
func_1()

# function parameters don't need a type
def func_2(a, b):
    return a * b

# multiplies 2 and 3
print(func_2(2,3))

# multiplies 'a' 3 times
print(func_2('a',3))

# multiplies list 3 times
print(func_2([1,2],3))