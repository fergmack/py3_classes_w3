# Return a value. For these, you will write return value tests.
# Modify the contents of some mutable object, like a list or dictionary. For these you will write side effect tests.
# Print something or write something to a file. Tests of whether a function generates the right printed output are beyond the scope of this testing framework; you won’t write these tests.

# return value test
def square(x):
    return x*x

assert square(3) == 9
assert square(-4) == 16
assert square(0) == 0 

# side effect test
# You can think of it like writing a small exam for your code – we would not give you an exam without knowing the answers ourselves.
def update_counts(letters, counts_d):
    for c in letters:
        if c in counts_d:
            counts_d[c] = counts_d[c] + 1
        else: 
            counts_d[c] = 1


counts = {'a': 3, 'b': 2}
update_counts("aaab", counts)
# 3 more occurrences of a, so 6 in all
assert counts['a'] == 6
# 1 more occurrence of b, so 3 in all
assert counts['b'] == 3


