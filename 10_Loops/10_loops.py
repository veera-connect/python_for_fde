# Python examples extracted from 10_loops.md
# Run one section at a time in VS Code using the cell play buttons.
# Some examples require packages or services described in the lesson.

# %%
# Example 1: While Loop
# syntax
while condition:
    code goes here

# %%
# Example 2: While Loop
count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4

# %%
# Example 3: While Loop
# syntax
while condition:
    code goes here
else:
    code goes here

# %%
# Example 4: While Loop
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

# %%
# Example 5: Break and Continue - Part 1
# syntax
while condition:
    code goes here
    if another_condition:
        break

# %%
# Example 6: Break and Continue - Part 1
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

# %%
# Example 7: Break and Continue - Part 1
# syntax
while condition:
    code goes here
    if another_condition:
        continue

# %%
# Example 8: Break and Continue - Part 1
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1

# %%
# Example 9: For Loop
# syntax
for iterator in lst:
    code goes here

# %%
# Example 10: For Loop
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5

# %%
# Example 11: For Loop
# syntax
for iterator in string:
    code goes here

# %%
# Example 12: For Loop
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])

# %%
# Example 13: For Loop
# syntax
for iterator in tpl:
    code goes here

# %%
# Example 14: For Loop
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# %%
# Example 15: For Loop
# syntax
for iterator in dct:
    code goes here

# %%
# Example 16: For Loop
person = {
    'first_name':'veera',
    'last_name':'narni',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

# %%
# Example 17: For Loop
# syntax
for iterator in st:
    code goes here

# %%
# Example 18: For Loop
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

# %%
# Example 19: Break and Continue - Part 2
# syntax
for iterator in sequence:
    code goes here
    if condition:
        break

# %%
# Example 20: Break and Continue - Part 2
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

# %%
# Example 21: Break and Continue - Part 2
# syntax
for iterator in sequence:
    code goes here
    if condition:
        continue

# %%
# Example 22: Break and Continue - Part 2
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

# %%
# Example 23: The Range Function
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# for backward from start to end 
lst = list(range(11,0,-2))
print(lst) # [11,9,7,5,3,1]

# %%
# Example 24: The Range Function
# syntax
for iterator in range(start, end, step):

# %%
# Example 25: The Range Function
for number in range(11):
    print(number)   # prints 0 to 10, not including 11

# %%
# Example 26: Nested For Loop
# syntax
for x in y:
    for t in x:
        print(t)

# %%
# Example 27: Nested For Loop
person = {
    'first_name': 'veera',
    'last_name': 'narni',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# %%
# Example 28: For Else
# syntax
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')

# %%
# Example 29: For Else
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)

# %%
# Example 30: Pass
for number in range(6):
    pass
