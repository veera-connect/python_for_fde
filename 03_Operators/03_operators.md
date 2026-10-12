<div align="center">
  <h1> 30 Days Of Python: Day 3 - Operators</h1>

<sub>Author:
veera narni<br>
<small> Third Edition: September, 2026</small>
</sub>
</div>

[<< Day 2](../02_Variables_and_Builtin_Functions/02_variables_and_builtin_functions.md) | [Day 4 >>](../04_Strings/04_strings.md)


- [ðŸ“˜ Day 3](#-day-3)
  - [Boolean](#boolean)
  - [Operators](#operators)
    - [Assignment Operators](#assignment-operators)
    - [Arithmetic Operators:](#arithmetic-operators)
    - [Comparison Operators](#comparison-operators)
    - [Logical Operators](#logical-operators)
    - [Chained Comparison](#chained-comparison)
    - [Walrus Operator (:=)](#walrus-operator-)
    - [Bitwise Operators](#bitwise-operators)
  - [ðŸ’» Exercises - Day 3](#-exercises---day-3)

# ðŸ“˜ Day 3

## Boolean

A boolean data type represents one of the two values: _True_ or _False_. The use of these data types will be clear once we start using the comparison operator. The first letter **T** for True and **F** for False should be capital unlike JavaScript.
**Example: Boolean Values**

```py
print(True)
print(False)
```

## Operators

Python language supports several types of operators. In this section, we will focus on few of them.

### Assignment Operators

Assignment operators are used to assign values to variables. Let us take = as an example. Equal sign in mathematics shows that two values are equal, however in Python it means we are storing a value in a certain variable and we call it assignment or a assigning value to a variable. The table below shows the different types of python assignment operators.

| Operator | Name                      | Example   | Result (starting from x = 5) |
|----------|---------------------------|-----------|------------------------------|
| =        | Assign                    | `x = 5`   | `x` is `5`                   |
| +=       | Add and assign            | `x += 3`  | `x` becomes `8`              |
| -=       | Subtract and assign       | `x -= 3`  | `x` becomes `5`              |
| *=       | Multiply and assign       | `x *= 3`  | `x` becomes `15`             |
| /=       | Divide and assign         | `x /= 3`  | `x` becomes `5.0`            |
| //=      | Floor divide and assign   | `x //= 4` | `x` becomes `3`              |
| %=       | Modulus and assign        | `x %= 4`  | `x` becomes `3`              |
| **=      | Exponent and assign       | `x **= 2` | `x` becomes `9`              |

**Example: Assignment Operators**

```py
x = 5
print(x)        # 5

x += 3
print(x)        # 8

x -= 3
print(x)        # 5

x *= 3
print(x)        # 15

x /= 3
print(x)        # 5.0

x = 15
x //= 4
print(x)        # 3

x = 15
x %= 4
print(x)        # 3

x = 3
x **= 2
print(x)        # 9
```

Output:

```shell
5
8
5
15
5.0
3
3
9
```

### Arithmetic Operators:

- Addition(+): a + b
- Subtraction(-): a - b
- Multiplication(*): a * b
- Division(/): a / b
- Modulus(%): a % b
- Floor division(//): a // b
- Exponentiation(**): a ** b

| Operator | Name           | Example    | Result |
|----------|----------------|------------|--------|
| +        | Addition       | `1 + 2`    | `3`    |
| -        | Subtraction    | `2 - 1`    | `1`    |
| *        | Multiplication | `2 * 3`    | `6`    |
| /        | Division       | `4 / 2`    | `2.0`  |
| //       | Floor division | `7 // 2`   | `3`    |
| %        | Modulus        | `3 % 2`    | `1`    |
| **       | Exponentiation | `2 ** 3`   | `8`    |

**Example:Integers**

```py
# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 8 it means 2 * 2 * 2
```

**Example:Floats**

```py
# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)
```

**Example:Complex numbers**

```py
# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))
```

Let's declare a variable and assign a number data type. I am going to use single character variable but remember do not develop a habit of declaring such types of variables. Variable names should be all the time mnemonic.

**Example:**

```python
# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
print(total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)
```

**Example:**

```py
print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)
```

Let us start connecting the dots and start making use of what we already know to calculate (area, volume,density,  weight, perimeter, distance, force).

**Example:**

```py
# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adding unit to the weight

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3
print(density, 'Kg/m^3') # Adding unit to the density

```

### Comparison Operators

In programming we compare values, we use comparison operators to compare two values. We check if a value is greater or less or equal to other value. The following table shows Python comparison operators.

| Operator | Name                     | Example   | Result  |
|----------|--------------------------|-----------|---------|
| ==       | Equal                    | `3 == 2`  | `False` |
| !=       | Not equal                | `3 != 2`  | `True`  |
| >        | Greater than             | `3 > 2`   | `True`  |
| <        | Less than                | `3 < 2`   | `False` |
| >=       | Greater than or equal to | `3 >= 2`  | `True`  |
| <=       | Less than or equal to    | `2 <= 3`  | `True`  |

**Example: Comparison Operators**

```py
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
```

In addition to the above comparison operator Python uses:

- _is_: Returns true if both variables are the same object(x is y)
- _is not_: Returns true if both variables are not the same object(x is not y)
- _in_: Returns True if the queried list contains a certain item(x in y)
- _not in_: Returns True if the queried list doesn't have a certain item(x not in y)

**Membership operators (in, not in):**

| Operator | Example                      | Result  |
|----------|------------------------------|---------|
| in       | `'a' in 'an'`                | `True`  |
| in       | `1 in [1, 2, 3]`             | `True`  |
| not in   | `5 not in [1, 2, 3]`         | `True`  |

```py
print('A in veera', 'A' in 'veera')   # False - 'veera' has a lowercase v, no uppercase A
print('coding' in 'coding for all')   # True - the substring is found
print('a in an:', 'a' in 'an')        # True

nums = [1, 2, 3]
print('1 in nums:', 1 in nums)        # True
print('5 not in nums:', 5 not in nums)  # True
```

Output:

```shell
A in veera False
coding for all True
a in an: True
1 in nums: True
5 not in nums: True
```

**Identity operators (is, is not):** the `is` operator checks whether two variables point to the **same object** in memory, not whether their values are equal. Use `==` to compare values.

```py
a = [1, 2, 3]
b = a          # b points to the same list object as a
c = [1, 2, 3]  # c is a different object with the same values

print('b is a:', b is a)          # True - same object
print('c is a:', c is a)          # False - different objects
print('c is not a:', c is not a)  # True
print('c == a:', c == a)          # True - same values
```

Output:

```shell
b is a: True
c is a: False
c is not a: True
c == a: True
```

### Logical Operators

Unlike other programming languages python uses keywords _and_, _or_ and _not_ for logical operators. Logical operators are used to combine conditional statements:

| Operator | Description                                        | Example                  | Result  |
|----------|----------------------------------------------------|--------------------------|---------|
| and      | True if both statements are true                   | `3 > 2 and 4 > 3`        | `True`  |
| or       | True if at least one statement is true             | `3 < 2 or 4 > 3`         | `True`  |
| not      | Reverses the result, returns the opposite boolean  | `not 3 > 2`              | `False` |

```py
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

```

### Chained Comparison

Python lets you chain comparison operators, which reads like a mathematical expression.

```py
print(1 < 2 < 3)  # True - both 1 < 2 and 2 < 3 are true
print(5 > 3 > 1)  # True
print(1 < 2 > 3)  # False - 2 > 3 is false
```

Output:

```shell
True
True
False
```

### Walrus Operator (:=)

The walrus operator assigns a value to a variable as part of an expression.

```py
numbers = [1, 2, 3, 4, 5]
if (n := len(numbers)) > 3:
    print('List is long, length =', n)
```

Output:

```shell
List is long, length = 5
```

### Bitwise Operators

Bitwise operators work on the binary representation of integers.

| Operator | Name        | Example    | Result |
|----------|-------------|------------|--------|
| &        | AND         | `5 & 3`    | `1`    |
| \|       | OR          | `5 \| 3`   | `7`    |
| ^        | XOR         | `5 ^ 3`    | `6`    |
| ~        | NOT         | `~5`       | `-6`   |
| <<       | Left shift  | `5 << 1`   | `10`   |
| >>       | Right shift | `5 >> 1`   | `2`    |

```py
print(5 & 3)   # 1
print(5 | 3)   # 7
print(5 ^ 3)   # 6
print(~5)      # -6
print(5 << 1)  # 10
print(5 >> 1)  # 2
```

Output:

```shell
1
7
6
-6
10
2
```

ðŸŒ• You have boundless energy. You have just completed day 3 challenges and you are three steps ahead on your way to greatness. Now do some exercises for your brain and your muscles.

## ðŸ’» Exercises - Day 3

1. Declare your age as integer variable
2. Declare your height as a float variable
3. Declare a variable that store a complex number
4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

```py
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
```

5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

```py
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
```

6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
9. Slope is (m = y2-y1/x2-x1). Find the slope and [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) between point (2, 2) and point (6,10) 
10. Compare the slopes in tasks 8 and 9.
11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
13. Use _and_ operator to check if 'on' is found in both 'python' and 'dragon'
14. _I hope this course is not full of jargon_. Use _in_ operator to check if _jargon_ is in the sentence.
15. There is no 'on' in both dragon and python
16. Find the length of the text _python_ and convert the value to float and convert it to string
17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
19. Check if type of '10' is equal to type of 10
20. Check if int('9.8') is equal to 10
21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

```py
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
```

22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

```py
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
```

23. Write a Python script that displays the following table

```py
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
```

ðŸŽ‰ CONGRATULATIONS ! ðŸŽ‰

[<< Day 2](../02_Variables_and_Builtin_Functions/02_variables_and_builtin_functions.md) | [Day 4 >>](../04_Strings/04_strings.md)
