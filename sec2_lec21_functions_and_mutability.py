

# immutable object
def process(s):
    print("initial s memory address # = {0}".format(id(s)))
    s = s + 'world'
    print("final s memory address # = {0}".format(id(s)))

my_var = 'hello'
print('my_var # = {0}'.format(id(my_var)))

process(my_var)
print(id(my_var))

print(10 * "=")

# mutable object - here, the result address doesn't change
def modify_list(lst):
    print("initial lst memory address # = {0}".format(id(lst)))
    lst.append(100)     #modifying the object state
    print("final lst memory address # = {0}".format(id(lst)))

my_list = [1,2,3]
print(id(my_list))

modify_list(my_list)