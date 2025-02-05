"""
Note. You should use indexing, negative indexing, slicing method,
mathematical operations and other techniques to accomplish tasks.

- Lists -
A. Create a list containing minimum seven different colors.
color = ["green", "red", "blue", "black", "orange", "gray", "yellow" ]

B. Create a list containing minimum five different countries.
countries = ["Spain", "Italy", "Finland", "Azerbaijan", "USa"]

C. Create a list containing three string values and two integer values.
str_int = ["apple", "orange", "cherry", 35, 9]

D. Create a list containing all continents of the world.
continents = ["Asia", "Africa", "North America", "South America", "Antarctica, Europe"]

E. Create a list containing minimum four car brands.
my_brand_car = ["BMW", "lamborgini", "Pagani", "Audi"]

F. Create a list containing four different data types of Python.
data_type =["string", "Float", "integar", "boolen"]
G. Create a list containing only negative even numbers from -2 to -12.
negative_numb = [-2, -4, -6, -8, -10, -12]
H. Create a list containing only positive even numbers from 0 to 12.
number = [2, 4, 6, 8, 10, 12]
I. Combine lists from Task G and H.
combine = negative_numb + number
J. Create a list containing minimum six students' names. Print the first
student's name.
students = ["kanan", "Nadir", "Ilham", "mahir", "veli", "islam" ]
print(students[0])

K. Create a list containing three different integers. Print the integer
at position two.
number = [2, 4, 6, 8]
print(number[1])

L. Print the last element of Task D's list.
print(continents[-1])

M. Print the last 2 elements of Task A's list. You can use slicing
method only once. Separately printing those elements will not be accepted.
print(color[-2:-1: -1])

N. Given the following list:
Create a new list containing the triple value of that list.
three = [3, 3, 3]
a, b, c = three



O. Create any nested list. Print any value from the inner list and the whole
inner list.
nested_list = [1, 2, 3]

P. Change the value of the color at position six of the list from Task A.
print(color[5])
Q. From Task B's list print all countries except the first two.
print(countries[1::1])
R. Create two new lists containing the double value of the list from Task F 
using 2 different mathematical operations (methods).
new_list = ["phone","number", "charge"]
new_list_2 = ["Kevin", "Karen", "Jim"]
result = new_list+new_list2

S. From the following list change the value of the last element to "Bob":
friends = "Kevin, Karen, Jim, Carry"
new = friends.replace("Carry", "Bob")
print(new)


T. Create an empty list.
empty = [" "]

- Interview Question -
A. Reverse a list with slicing method.
new_list = ["phone","number", "charge"]
print(new_list[::-1])


Bonus:
A. Print the whole list from previous tasks using the slicing method.
new_list = ["phone","number", "charge"]
print(new_list[:-1])

B. Print the length of any list from previous tasks.
friends = "Kevin, Karen, Jim, Carry"
print(len(friends))
"""