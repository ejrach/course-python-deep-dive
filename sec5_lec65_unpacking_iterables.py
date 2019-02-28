# define a tuple
a = (1, 2, 3)

print(type(a))
print(a)

#unpack into a tuple (don't need the parenthesis)
a, b, c = [1, 'a', 3.14]

print(a)
print(b)
print(c)

# another way to unpack
a, b = 10, 20

print(a)
print(b)

#swapping variables
a, b = 10, 20
print(a, b)

a,b = b,a
print(a, b)

# using for loop to unpack
for e in 'XYZ':
    print(e)

# is the same as
a, b, c = 'XYZ'
print(a, b, c)

# unpacks dictionary key's only
d = {'a':1, 'b':2, 'c':3, 'd':4}
for e in d:
    print (e)

# unpacks key and value
for e in d.items():
    a, b = e
    print ("key={0}, value={1}".format(a,b))



