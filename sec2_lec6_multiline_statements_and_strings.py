# Implicit Line Continuation

# Lists
a = [1, 2, 3]

a = [1, 2, 
        3, 4, 5]

print(a)

# tuples
a = (1 #comment
    ,2 #comment
    ,3)

print(a)

# dictionary
a = {'key1': 1 #value for key 1
    ,'key2': 2 #value for key 2
    }

print(a)


# functions
def my_func(a,  #this is used to indicate
            b,  #comment
            c):
    print(a,b,c)

my_func(10, #comment
        20, #comment
        30  #comment
        )


# Explicit line continuation ("\")
a = 10
b = 20
c = 30

if a > 5 \
    and b > 10 \
        and c > 20:
    print("yes")

# multi line strings
a = '''this is a string'''
print(a)

#prints over two lines
a = '''this 
is a string'''

print(a)

a = 'this\nis a string'
print(a)


