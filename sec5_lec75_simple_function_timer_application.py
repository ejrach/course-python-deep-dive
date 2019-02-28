# Want to time how long a function takes to run
# Be able to time this
# Want to be generic so it could work with any function and any parameters

import time

# pass the function, and positional arguments and keyword arguments
def time_it(fn, *args, rep = 1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (end - start)/rep


print(time_it(print, 1, 2, 3, sep=' - ', end=' ***\n', rep = 5))

# calculate n, starting at the power of 1, or whatever is defined
# by start. The *  indicates we are not allowing any more positional arguments
def computer_powers_1(n, *, start=1, end):
    # using a for loop
    results = []
    for i in range(start, end):
        results.append(n**i)
    return results

def computer_powers_2(n, *, start=1, end):
    # using a list comprehension
    return [n**i for i in range(start, end)]

def computer_powers_3(n, *, start=1, end):
    # using generator expressions
    return (n**i for i in range(start, end))

# print the list of 2 to the power of 1 through 4 (5 is non inclusive)
print(computer_powers_1(2, end=5))
print(computer_powers_2(2, end=5))
print(list(computer_powers_3(2, end=5)))


print(time_it(computer_powers_1, 2, start=0, end=20000, rep=5))
print(time_it(computer_powers_2, 2, start=0, end=20000, rep=5))
print(time_it(computer_powers_3, 2, start=0, end=20000, rep=5))
