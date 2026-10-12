# Python examples extracted from 19_file_handling.md
# Run one section at a time in VS Code using the cell play buttons.
# Some examples require packages or services described in the lesson.

# %%
# Example 1: File Handling
# Syntax
open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update

# %%
# Example 2: Opening Files for Reading
f = open('./sample_files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./sample_files/reading_file_example.txt' mode='r' encoding='UTF-8'>

# %%
# Example 3: Opening Files for Reading
f = open('./sample_files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()

# %%
# Example 4: output
f = open('./sample_files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()

# %%
# Example 5: output
f = open('./sample_files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()

# %%
# Example 6: output
f = open('./sample_files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()

# %%
# Example 7: output
f = open('./sample_files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()

# %%
# Example 8: output
with open('./sample_files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)

# %%
# Example 9: Opening Files for Writing and Updating
with open('./sample_files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')

# %%
# Example 10: Opening Files for Writing and Updating
with open('./sample_files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')

# %%
# Example 11: Deleting Files
import os
os.remove('./sample_files/example.txt')

# %%
# Example 12: Deleting Files
import os
if os.path.exists('./sample_files/example.txt'):
    os.remove('./sample_files/example.txt')
else:
    print('The file does not exist')

# %%
# Example 13: File with json Extension
# dictionary
person_dct= {
    "name":"veera",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'veera', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"veera",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''

# %%
# Example 14: Changing JSON to Dictionary
import json
# JSON
person_json = '''{
    "name": "veera",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

# %%
# Example 15: Changing Dictionary to JSON
import json
# python dictionary
person = {
    "name": "veera",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)

# %%
# Example 16: Saving as JSON File
import json
# python dictionary
person = {
    "name": "veera",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./sample_files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)

# %%
# Example 17: File with csv Extension
import csv
with open('./sample_files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # we use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')

# %%
# Example 18: File with xlsx Extension
import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)

# %%
# Example 19: File with xml Extension
import xml.etree.ElementTree as ET
tree = ET.parse('./sample_files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)

# %%
# Example 20: Exercises: Level 2
# Your output should look like this
    print(find_most_common_words('sample.txt', 10))
    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and'),
    (4, 'a'),
    (4, 'in'),
    (3, 'that'),
    (2, 'have'),
    (2, 'I')]

    # Your output should look like this
    print(find_most_common_words('sample.txt', 5))

    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and')]
