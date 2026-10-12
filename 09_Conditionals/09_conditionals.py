# Python examples extracted from 09_conditionals.md
# Run one section at a time in VS Code using the cell play buttons.
# Some examples require packages or services described in the lesson.

# %%
# Example 1: If Condition
# syntax
if condition:
    this part of code runs for truthy conditions

# %%
# Example 2: If Condition
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number

# %%
# Example 3: If Else
# syntax
if condition:
    this part of code runs for truthy conditions
else:
     this part of code runs for false conditions

# %%
# Example 4: If Else
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

# %%
# Example 5: If Elif Else
# syntax
if condition:
    code
elif condition:
    code
else:
    code

# %%
# Example 6: If Elif Else
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

# %%
# Example 7: Short Hand
# syntax
code if condition else code

# %%
# Example 8: Short Hand
a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed

# %%
# Example 9: Nested Conditions
# syntax
if condition:
    code
    if condition:
    code

# %%
# Example 10: Nested Conditions
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

# %%
# Example 11: If Condition and Logical Operators
# syntax
if condition and condition:
    code

# %%
# Example 12: If Condition and Logical Operators
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

# %%
# Example 13: If and Or Logical Operators
# syntax
if condition or condition:
    code

# %%
# Example 14: If and Or Logical Operators
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')

# %%
# Example 15: Exercises: Level 3
person={
    'first_name': 'veera',
    'last_name': 'narni',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

# %%
# Example 16: Exercises: Level 3
veera narni lives in Finland. He is married.
