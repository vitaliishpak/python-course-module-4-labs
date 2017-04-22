##Laboratory Work 4.5

####Description:

Find Lab_4_5_generators.py attached.
1. Explain how does enumerate function works
2. Answer the questions
3. Create generator function that return item value index +1 and item value itself
4. Create list with numbers from 1 to 5
5. Write loop with printing own enumerate function values for number list

####Here is its solution code:

*solution_4_5.py*
```python
""" Create own enumerate function with count started from 1 bot from 0 """

"""
Explain how does enumerate function works
Answer the questions
"""


def enumerator(*args):
    return list(enumerate(list(args)))


"""
Create generator function that return item value index +1 and item value itself
"""


def next_item(*args, index: int):
    try:
        return args[index + 1]
    except IndexError:
        print('There is no item with index {i}!'.format(i=index))
        return args[len(args) - 1]


if __name__ == '__main__':
    l = ['a', 'b', 'c']
    print(enumerator(*l))
    print(next_item(*l, index=4))
    print(next_item(*l, index=0))

"""
Create list with numbers from 1 to 5
"""
nums = list(range(1, 6))

"""
Write loop with printing own enumerate function values for number list
"""
print(nums)
print(enumerator(*nums))
for t in enumerator(nums):
    print(t[1], end=' ')
print()

for t in list(enumerate(nums)):
    print(t[1], end=' ')
print()
```