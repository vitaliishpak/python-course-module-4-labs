"""
Refactor given program code:
    foo = [1, 2, 3, 4, 5]
    odd_foo = []
    def isOdd(x):
        return x % 2 == 1
    for f in foo:
        if isOdd(f):
            odd_foo.append(f)
    print (odd_foo)
- Use list comprehension for this task
- Use filter with lambda function for this task
- Solutions should have only one line of code
"""

foo = list([ i for i in range(1,6)])
print(foo)

foo_odd = list(filter(lambda x:x%2==1, list(range(1,6))))
print(foo_odd)
