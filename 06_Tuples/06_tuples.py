# Python examples extracted from 06_tuples.md
# Run one section at a time in VS Code using the cell play buttons.
# Some examples require packages or services described in the lesson.

# %%
# Example 1: Tuple length
# syntax
tpl = ('item1', 'item2', 'item3')
len(tpl)

# %%
# Example 2: Changing Tuples to Lists
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)

# %%
# Example 3: Changing Tuples to Lists
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')

# %%
# Example 4: Checking an Item in a Tuple
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True

# %%
# Example 5: Checking an Item in a Tuple
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment

# %%
# Example 6: Joining Tuples
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2

# %%
# Example 7: Joining Tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables

# %%
# Example 8: Deleting Tuples
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1

# %%
# Example 9: Deleting Tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
