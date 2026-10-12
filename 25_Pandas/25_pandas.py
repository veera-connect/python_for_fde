# Python examples extracted from 25_pandas.md
# Run one section at a time in VS Code using the cell play buttons.
# Some examples require packages or services described in the lesson.

# %%
# Example 1: Installing Pandas
pip install conda
conda install pandas

# %%
# Example 2: Installing Pandas
pip install conda
pip install pandas

# %%
# Example 3: Installing Pandas
import pandas as pd

names = pd.Series(['veera', 'David', 'John', 'Sara', 'Eyob'])
print(names)

# %%
# Example 4: Installing Pandas
countries = pd.Series(['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland'])
print(countries)

# %%
# Example 5: Installing Pandas
cities = pd.Series(['Helsinki', 'Stockholm', 'Oslo', 'Copenhagen', 'Reykjavik'])
print(cities)

# %%
# Example 6: Installing Pandas
data = [
    ['veera', 'Finland', 'Helsinki'],
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names', 'Country', 'City'])
print(df)

# %%
# Example 7: Installing Pandas
df = pd.read_csv('weight-height.csv')
print(df.head())

# %%
# Example 8: Importing Pandas
import pandas as pd # importing pandas as pd
import numpy  as np # importing numpy as np

# %%
# Example 9: Creating Pandas Series with Default Index
nums = [1, 2, 3, 4,5]
s = pd.Series(nums)
print(s)

# %%
# Example 10: Creating  Pandas Series with custom index
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)

# %%
# Example 11: Creating  Pandas Series with custom index
fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)

# %%
# Example 12: Creating Pandas Series from a Dictionary
dct = {'name':'veera','country':'Finland','city':'Helsinki'}

# %%
# Example 13: Creating Pandas Series from a Dictionary
s = pd.Series(dct)
print(s)

# %%
# Example 14: Creating a Constant Pandas Series
s = pd.Series(10, index = [1, 2, 3])
print(s)

# %%
# Example 15: Creating a  Pandas Series Using Linspace
s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
print(s)

# %%
# Example 16: Creating DataFrames from List of Lists
data = [
    ['veera', 'Finland', 'Helsink'],
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)

# %%
# Example 17: Creating DataFrame Using Dictionary
data = {'Name': ['veera', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)

# %%
# Example 18: Creating DataFrames from a List of Dictionaries
data = [
    {'Name': 'veera', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)

# %%
# Example 19: Reading CSV File Using Pandas
import pandas as pd

df = pd.read_csv('weight-height.csv')
print(df)

# %%
# Example 20: Data Exploration
print(df.head()) # give five rows we can increase the number of rows by passing argument to the head() method

# %%
# Example 21: Data Exploration
print(df.tail()) # tails give the last five rows, we can increase the rows by passing argument to tail method

# %%
# Example 22: Data Exploration
print(df.shape) # as you can see 10000 rows and three columns

# %%
# Example 23: Data Exploration
print(df.columns)

# %%
# Example 24: Data Exploration
heights = df['Height'] # this is now a series

# %%
# Example 25: Data Exploration
print(heights)

# %%
# Example 26: Data Exploration
weights = df['Weight'] # this is now a series

# %%
# Example 27: Data Exploration
print(weights)

# %%
# Example 28: Data Exploration
print(len(heights) == len(weights))

# %%
# Example 29: Data Exploration
print(heights.describe()) # give statistical information about height data

# %%
# Example 30: Data Exploration
print(weights.describe())

# %%
# Example 31: Data Exploration
print(df.describe())  # describe can also give statistical information from a dataFrame

# %%
# Example 32: Data Exploration
print(df.info())

# %%
# Example 33: Creating a DataFrame
import pandas as pd
import numpy as np
data = [
    {"Name": "veera", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
print(df)

# %%
# Example 34: Adding a New Column
weights = [74, 78, 69]
df['Weight'] = weights
df

# %%
# Example 35: Adding a New Column
heights = [173, 175, 169]
df['Height'] = heights
print(df)

# %%
# Example 36: Modifying column values
df['Height'] = df['Height'] * 0.01
df

# %%
# Example 37: Modifying column values
# Using functions makes our code clean, but you can calculate the bmi without one
def calculate_bmi ():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi

bmi = calculate_bmi()

# %%
# Example 38: Modifying column values
df['BMI'] = bmi
df

# %%
# Example 39: Formatting DataFrame columns
df['BMI'] = round(df['BMI'], 1)
print(df)

# %%
# Example 40: Formatting DataFrame columns
birth_year = ['1769', '1985', '1990']
current_year = pd.Series(2020, index=[0, 1,2])
df['Birth Year'] = birth_year
df['Current Year'] = current_year
df

# %%
# Example 41: Checking data types of Column values
print(df.Weight.dtype)

# %%
# Example 42: Checking data types of Column values
df['Birth Year'].dtype # it gives string object , we should change this to number

# %%
# Example 43: Checking data types of Column values
df['Birth Year'] = df['Birth Year'].astype('int')
print(df['Birth Year'].dtype) # let's check the data type now

# %%
# Example 44: Checking data types of Column values
df['Current Year'] = df['Current Year'].astype('int')
print(df['Current Year'].dtype)

# %%
# Example 45: Checking data types of Column values
ages = df['Current Year'] - df['Birth Year']
print(ages)

# %%
# Example 46: Checking data types of Column values
df['Ages'] = ages
print(df)

# %%
# Example 47: Checking data types of Column values
mean = (35 + 30)/ 2
print('Mean: ',mean)	#it is good to add some description to the output, so we know what is what

# %%
# Example 48: Boolean Indexing
print(df[df['Ages'] > 120])

# %%
# Example 49: Boolean Indexing
print(df[df['Ages'] < 120])
