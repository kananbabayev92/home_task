"""
Note. Add the following list at the top of your code. You will use this list
during the homework in certain tasks:
fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]


Also print the list's modification versions to see the difference.

- List Methods -
A. Make up a formula with built-in python 'len' method that finds helps 
to get the last element from the 'fruits' list.

fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]
print("This have", len(fruits), "fruits")
print("The a", fruits[6], "last fruit")
_____________________________________________________________________________________-
B. Add any two fruits to the 'fruits' list.

fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]
fruits.append("mango")
fruits.append("avocado")
print(fruits)
_____________________________________________________________________________________-
C. Remove third fruit so you can assign it to a variable.

fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]
fruits.remove("Orange")
print(fruits)
_____________________________________________________________________________________-
D. Add a fruit to the 'fruits' list twice, and then print the amount of 
this fruit
in the 'fruits' list.

fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]
twice = fruits*2
print(len(twice))

_____________________________________________________________________________________-

E. Find the index of 'Grape' object in the 'fruits' list.

fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]
index_fruit = fruits.index("Grape")
print(index_fruit)


_____________________________________________________________________________________-
F. Add 'Avocado' to the 'fruits' list at position four. 

fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]
fruits.insert(3, "avocado")
print(fruits)
_____________________________________________________________________________________-
G. Remove third fruit without getting the removed fruit.
fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]
index_fruit = fruits.pop(2)
print(index_fruit)
print(fruits)

_____________________________________________________________________________________-

H. Remove a fruit at position one.
fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]
index_fruit = fruits.pop(0)
print(index_fruit)
print(fruits)


_____________________________________________________________________________________-
I. Add 'Blackberry' to the end of the 'fruits' list. Remove it using 'pop' 
method
by finding its positive index.
fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]
fruits.append("Blackberry")
print(fruits)
blackbery_index = fruits.index("Blackberry")
print(blackbery_index)
remove_blackbery = fruits.pop(7)
print("After remove", fruits)

_____________________________________________________________________________________-
J. Reverse the 'fruits' list with two different methods. Each time print 
the reversed
list.
fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]
print(fruits[::-1])
_____________________________________________________________________________________-
K. Sort alphabetically the 'fruits' list. Print the sorted version of the 
list.
fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]
fruits.sort()
print(fruits)

_____________________________________________________________________________________-
L. Suppose you have the following list:

new_fruits = ["Papaya", "Lime", "Lemon", "Peach"]
fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]
new_list = fruits + new_fruits
print(new_list)

Extend the 'fruits' list with the new list.

_____________________________________________________________________________________-
M. Make a copy of the 'fruits' list. Remove the last three fruits. Print 
both of the
lists ('fruits' and the modified copied version).

fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]
del fruits[-3: ]
new_fruits = ["Papaya", "Lime", "Lemon", "Peach"]
fruits.extend(new_fruits)
print(fruits)


_____________________________________________________________________________________-
N. Create a variable named 'occurrence'. Make it equal True if the 
'Papaya' is in the
'fruits' list, otherwise False.

fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry", "Papaya", "Lime", "Lemon", "Peach"]
occurrence = fruits.count("Papaya")
papaya_is_fruit = "Papaya" in fruits
print(papaya_is_fruit)
_____________________________________________________________________________________-

O. Clear the 'fruits' list.

fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry", "Papaya", "Lime", "Lemon", "Peach"]
fruits.clear()
print(fruits)


_____________________________________________________________________________________-

- Variables -
A. Suppose you have the following variables:
x = 60
y = 70

You need to swap these variables values in one line of code.
x, y = y, x

print(x, y)

- ChatGPT's homework (List Methods) -
1. Append and Extend:
a. Write a Python program that creates an empty list and then appends 
the following elements to it: 10, 20, 30, 40, and 50. Print the list 
after each append operation.
b. Create a second list containing elements [60, 70, 80]. Extend the 
first list using this second list and print the updated list.

empty_list = []
numb_list = 10, 20, 30, 40,50
empty_list.extend(numb_list)
more_numb = [60, 70, 80]
empty_list.extend(more_numb)
print(empty_list)
______________________________________________________________________________

2. Insert and Remove:
a. Write a Python program that creates a list containing the following 

elements: 'apple', 'banana', 'orange', 'grape', 'apple', 'kiwi'.
b. Use the 'insert' method to add 'pear' between 'banana' and 'orange' 
in the list. Print the updated list.
c. Use the 'remove' method to remove the first occurrence of 'apple' from 
the list. Print the updated list.
fruits = ["Apple", "Banana", "Orange", "Grape", "Apple", "Kiwi"]
fruits.insert(2, "pear")
fruits.pop(0)
print(fruits)

_________________________________________________________________________________


3. Count and Index:
a. Create a list containing the following elements: 2, 4, 6, 8, 4, 10, 4, 
12, 14.
b. Use the 'count' method to find how many times the color 4 appears in the 
list and print the count.
c. Use the 'index' method to find the index of the first occurrence of 4 in 
the list and print the index.

color = 2, 4, 6, 8, 4, 10, 4, 12, 14
count_color = color.count(4)
index_numb = color.index(4)
print(count_color)
print(index_numb)


_________________________________________________________________________________

4. Sort and Reverse:
a. Create a list containing the following integers in random order: 45, 23, 
78, 12, 98, 56.
b. Use the 'sort' method to sort the list in ascending order and print the 
sorted list.
c. Use the 'reverse' method to reverse the sorted list and print the reversed 
list.
color = [45, 23, 78, 12, 98, 56]
color.sort()
print(color)
print(color[::-1])

___________________________________________________________________________________________

5. Slice and Concatenate:
a. Create a list containing the following elements: 'red', 'blue', 'green', 
'yellow', 'orange', 'purple'.
b. Use slicing to extract a new list that contains only the first three 
colors. Print the new list.
c. Use slicing again to extract a new list that contains the last three 
colors. Print the new list.
d. Concatenate the two sliced lists and print the final combined list.

color_1 = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
del color[:3:1]
print(color)
color_2 = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
del color[3::1]
print(color)
______________________________________________________________________

color_1 = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
del color_1[:3:1]
print(color_1)
color_2 = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
del color_2[3::1]
print(color_2)
print("Concatenate two list: ", color_2 + color_1)
"""