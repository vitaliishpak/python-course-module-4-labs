"""
Create variable with numbers list from 0 to 9
"""
list_1 = [element for element in range(10)]

"""
Create variable with numbers list from 0 to 9 and step 2
"""
list_2 = [element for element in range(0, 10, 2)]

"""
Create function that find intersection between two list variable
"""
def lists_intersection(l_1, l_2):
    return list(set(l_1) & set(l_2))

"""
Create third list initialized with function defined above
"""
list_intersection = lists_intersection(list_1, list_2)

"""
Call function
"""
print(list_intersection)
