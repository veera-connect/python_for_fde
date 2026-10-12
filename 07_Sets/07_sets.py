# Python examples extracted from 07_sets.md
# Run one section at a time in VS Code using the cell play buttons.
# Some examples require packages or services described in the lesson.

# %%
# Example 1: Creating a Set
# syntax
st = set()

# %%
# Example 2: Creating a Set
# syntax
st = {'item1', 'item2', 'item3', 'item4'}

# %%
# Example 3: Creating a Set
# syntax
fruits = {'banana', 'orange', 'mango', 'lemon'}

# %%
# Example 4: Getting Set's Length
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
len(st)

# %%
# Example 5: Getting Set's Length
fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits)

# %%
# Example 6: Checking an Item
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True

# %%
# Example 7: Checking an Item
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True

# %%
# Example 8: Adding Items to a Set
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')

# %%
# Example 9: Adding Items to a Set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')

# %%
# Example 10: Adding Items to a Set
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])

# %%
# Example 11: Adding Items to a Set
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)

# %%
# Example 12: Removing Items from a Set
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')

# %%
# Example 13: Removing Items from a Set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set

# %%
# Example 14: Removing Items from a Set
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()

# %%
# Example 15: Clearing Items in a Set
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()

# %%
# Example 16: Clearing Items in a Set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()

# %%
# Example 17: Deleting a Set
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del st

# %%
# Example 18: Deleting a Set
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

# %%
# Example 19: Converting List to Set
# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered

# %%
# Example 20: Converting List to Set
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}

# %%
# Example 21: Joining Sets
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2) #st3 = st1 | st2

# %%
# Example 22: Joining Sets
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
# or using this : print(fruits | vegetables)

# %%
# Example 23: Joining Sets
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1

# %%
# Example 24: Joining Sets
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

# %%
# Example 25: Finding Intersection Items
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
# or using thia : st1 & st2

# %%
# Example 26: Finding Intersection Items
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}
# python & dragon

# %%
# Example 27: Checking Subset and Super Set
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True

# %%
# Example 28: Checking Subset and Super Set
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False

# %%
# Example 29: Checking the Difference Between Two Sets
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set() : st2 - st1
st1.difference(st2) # {'item1', 'item4'} => st1\st2  : st2 - st1

# %%
# Example 30: Checking the Difference Between Two Sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
# python - dragon
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
# dragon - python

# %%
# Example 31: Finding Symmetric Difference Between Two Sets
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)âˆª(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'} : st2 ^ st1

# %%
# Example 32: Finding Symmetric Difference Between Two Sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
# python ^ dragon

# %%
# Example 33: Joining Sets
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False

# %%
# Example 34: Joining Sets
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}

# %%
# Example 35: ðŸ’» Exercises: Day 7
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
