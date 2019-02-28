
# the *c is an optional, variable parameter
def func1(a, b, *c):
    print(a)
    print(b)
    print(c)

func1(10, 20)

# the 1, 2, 3 are printed as a tuple
func1(10, 20, 1, 2, 3)

# function to create average number of parameters passed to it
def avg(*args):
    count = len(args)
    total = sum(args)

    # use short circuited 'and', or use if/else
    # returns total/count (avg) if count is non-zero and total/count is non-zero
    # otherwise returns count = 0
    #return count and total/count

    if count == 0:
        return 0
    else:
        return total/count
    
print(avg(2, 2, 4, 4))


# another way to define avg function. Here we are forcing the
# function to be called with at least one argument
def avg1(a, *args):
    count = len(args) + 1
    total = sum(args) + a
    return total/count

print(avg1(2, 2, 4, 4))

# passing a list to function
def func2(a, b, c):
    print(a)
    print(b)
    print(c)

l = [1, 2, 3]

# pack the list
func2(*l)








