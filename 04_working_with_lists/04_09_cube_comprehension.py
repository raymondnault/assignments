'''

Raymond Nault
Chapter 4: Working with Lists

'''

# this loop will print cubes of numbers from 1 to 10, but only in one line of code using a list comprehension

list_of_cubes = [value**3 for value in range(1, 11)]
print(list_of_cubes)