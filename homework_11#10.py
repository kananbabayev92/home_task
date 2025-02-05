"""
- Lists -
A. Create an empty list and add 5 user-input integers to it.
empty_list = int(input("Add 5 number: ))

________________________________________________________________________________________________-
B. Take a list of integers as input and print the sum of all the elements in the list. 
a = input("add number:").split()
b = map(int, a)
c = sum(b)

print(c)
________________________________________________________________________________________________-
C. Ask the user for a sentence and store each word as an element in a list.

sentence = input("Enter a sentence: ")
word_list = sentence.split()
print(word_list)

________________________________________________________________________________________________-
D. Write a program that asks user for six countries. The program should create a list of
those countries and ask for three countries to delete from the list. Make the program
user-friendly, and print each time the content of a list to show the user which countries
are in a list.

countries = [input("Enter country 1: "), input("Enter country 2: "), input("Enter country 3: "),
input("Enter country 4: "), input("Enter country 5: "), input("Enter country 6: ")]

countries = list(countries)
print(f"\nYour list of countries: {countries}")
print(type(countries))
countries.remove(input("Enter the name of the country you want to remove:"))
print(countries)
countries.remove(input("Enter the name of the country you want to remove:"))
print(countries)
countries.remove(input("Enter the name of the country you want to remove:"))
print(countries)



________________________________________________________________________________________________-

E. Which list method makes any list look the same. The lists are the same if its content,
elements and all other properties are the same.
with copy()

fruits = ["Apple", "Banana", "Orange", "Grape", "Apple", "Kiwi"]
b = fruits.copy()
________________________________________________________________________________________________-
F. Create an empty list and print its length.
Write a function that accepts a list of names and returns the name with the longest length.

empty_list = []
print(len(empty_list))
________________________________________________________________________________________________-
G. Ask the user for a list of integers and find the second-largest number in the list.

number = list(map(int, input("add number with separete:").split(",")))
number.sort()
a = number.pop(-2)
print(number)
print(a)
________________________________________________________________________________________________-
H. Ask the user for a list of integers and find the mean value of that list. 
number = list(map(int, input("add number with separete:").split(",")))

a = sum(number)
print(number)
print(a)
________________________________________________________________________________________________-
I. Ask the user for a list of integers and find the third-smallest number in the list.

number = list(map(int, input("add number with separete:").split(",")))
number.sort()
a = number.pop(2)
print(number)
print(a)
________________________________________________________________________________________________-
J. Write a program that asks the user for three colors separated by spaces. The
program should print all those colors using comma (you should use string 'join' method). 
For example:
Your colors are red, blue, white.

user_color = list(map(str, input("add color  with separated by spaces: ").split()))
my_color = ["red", "blue", "white"]
my_color.extend(user_color)
print(type("my_color"))
print(my_color)
________________________________________________________________________________________________-
K. Write a program that asks the user for four capital cities separated by spaces. 
The program should print all those cities the following structure:

There are many capital cities in the world. For example, Baku, Moscow and Kyiv.

capital_cities = input("Add four capital cities separated by spaces: ").split()
print(capital_cities)
a, b, c, d = capital_cities
print(f"There are many capital cities in the world. For example, {a}, {b}, {c} and {d}.")

You should follow all instructions, and not make changes to the structure of final sentence.
________________________________________________________________________________________________-
L. Take a list of strings as input and sort it in alphabetical order.

words = input("Write words separated by spaces: ").split()
sorted_words = sorted(words)
print("Sorted words:", sorted_words)


________________________________________________________________________________________________-
M. Take a list of numeric values as input and sort it in descending order.

numbers = list(map(int, input("Enter numbers separated by spaces: ").split( )))
sorted_numbers = sorted(numbers, reverse=True)

print("Sorted numbers in descending order:", sorted_numbers)



________________________________________________________________________________________________-
N. Remove duplicates from a list entered by the user while preserving the original order. --------------------


________________________________________________________________________________________________-
O. Write a program that accepts two lists and concatenates them into a single list.

two_list = input("add fruits list:") +" "+ input("add vegetables list: ")
print(two_list)

The first list is a list of fruits, the second is a list of vegetables.


________________________________________________________________________________________________-
P. Write a program that prints 'True' if there is at least one item in a 'my_list' list.

my_list = list(map(str, input("Enter list items separated by spaces: ").split()))

print(bool(my_list))


________________________________________________________________________________________________-

- List Comprehension -
Suppose you have the following lists:
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ['p', 'y', 't', 'h', 'o', 'n']
times = [1, 2, 3, 4, 5]

combined_list = digits + letters + times
print(combined_list)
________________________________________________________________________________________________-
A. Create a list containing raised to power two values of 'digits' list. 
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
raised_digits = [digits**2 for digit in digits]
print(raised_digits)

________________________________________________________________________________________________-
B. Create a list containing capitalized version of letter values of 'letters' list.

letters = ['a', 'b', 'c', 'd', 'e']
capitalized_letters = [letter.upper() for letter in letters]
print(capitalized_letters)


________________________________________________________________________________________________-
C. Create a list containing the 'Comprehension' string value the amount of 'times'
list's length time.
times = [1, 2, 3]  
var = "Comprehension"
result = var * len(times)
print(result)

________________________________________________________________________________________________-
D. Create a list containing 5 random integers between -5 and 5. find the second-smallest 
number in the list. The program should print 'True' if that number is negative, and 'False'
otherwise.

number = (-4, -3, -2 , 0, 1, 2, 3, 4) # tuple
number = ("-4", "-3", "-2") #tuple
second_smal = sorted(number)
small = second_smal[1]
print(small)
print(type(number))


________________________________________________________________________________________________-
E. Create a list of 10 random numbers and find the maximum and minimum values.

random_number = (1, 2, 3, 5, 8, 10)
max_num = max(random_number)
min_num = min(random_number)

print(max_num)
print(min_num)

________________________________________________________________________________________________-
- Comments -
A. One-line comment, if it's appropriate.
B. Multi-line comment, if it's appropriate.
________________________________________________________________________________________________-





- Chat GPT's Homework -
A. Create a list of colors and write a function that duplicates each color in the 
list. For example, if the list contains "red," it should become ["red", "red"]. 
Print the modified list.  
color_list = "red", "blue"
new list = (color_list*2 for colors in color_list)

new_list = color_list*2



B. How many methods do you know to create an empty list in Python?   two  method  list = []  list_2 = list()

C. Which list method is used to add an element to the end of a list?
my_list.appened()

D. Write a Python code snippet to access the third element in a list named my_list. my_list.pop(2)

E. Which list method is used to remove the last element from a list? pop()

F. What list method is used to insert an element at a specific position?  insert()


G. Write Python code to reverse a list called my_list in-place. 
my_list.reverse()

H. How can you create a shallow copy of a list in Python? 
copy.copy()

I. Which list method is used to count the number of occurrences of a specific element in a list? 
count()


J. Write a Python code snippet to concatenate two lists, list1 and list2. 
two_list = input("add list 1:") +" "+ input("add  list 2: ")
print(two_list)


K. What list method can be used to sort a list in ascending order?  sort()


L. Write Python code to remove the first occurrence of an element 'x' from a list. 
x = ["banana", 'orange', 'grape',]
del x[0]



M. Explain the difference between append() and extend() methods when adding elements to a list. # with append can only value, with extend() can list

N. Which list method can be used to remove all elements from a list?  # clean()

P. What list method can be used to remove and return an element from a specific index in a list?        pop()
________________________________________________________________________________________________________



Quiz.
1. Which method is used to add an element to the end of a list in Python? 
    a) add()
    b) insert()
    c) extend()
    d) append() #correct 

2. What is the purpose of the insert() method for lists in Python? 

    a) Remove an element from a list.
    b) Add an element to the beginning of a list.
    c) Add an element at a specific index in the list.
    d) Replace an element at a specific index in the list. #correct

3. Which list method is used to remove and return the last element of a list? 
    a) pop() #correct
    b) remove()
    c) delete()
    d) discard()    

4. What does the extend() method do when used on a list in Python?
    a) Adds an element to the beginning of the list.
    b) Adds a new list as elements to the existing list. # correct
    c) Removes the last element from the list.
    d) Sorts the list in ascending order.

5. Which list method is used to reverse the order of elements in a list in Python?
    a) reverse() #correct
    b) flip() 
    c) backwards() 
    d) revert() 

6. What does the sort() method do when used on a list in Python?
    a) Reverses the order of elements in the list.
    b) Removes all elements from the list.
    c) Sorts the list in ascending order. # correct
    d) Sorts the list in descending order.

7. Which method is used to find the index of the first occurrence of an element in a list?
    a) index() #correct
    b) find()
    c) search()
    d) lookup()

8. What is the purpose of the pop() method when used on a list in Python?
    a) Adds an element to the end of the list.
    b) Removes and returns the last element of the list.
    c) Removes the first element of the list.
    d) Inserts an element at a specific index in the list. #correct

9. How can you count the number of occurrences of a specific element in a list?
    a) Use the count() method.    #correct
    b) Use the occurrences() method.
    c) Use the find_count() method.
    d) Use the search_count() method.

10. How can you check if a list is empty in Python?
    a) Use the empty() method. 
    b) Use the is_empty() method.
    c) Use the len() function and check if it's equal to zero. #correct
    d) Use the has_elements() method.

11. Which method is used to copy the elements of one list to another in Python?
    a) copy() # correct
    b) duplicate()
    c) clone()
    d) replicate()

12. How do you remove an element by index from a list in Python?
    a) Use the remove() method with the index as an argument.
    b) Use the pop() method with the index as an argument. #correct
    c) Use the delete() method with the index as an argument.
    d) Use the discard() method with the index as an argument.

13. What does the len() method do when applied to a list?
    a) Returns the maximum value in the list #correct
    b) Returns the minimum value in the list
    c) Returns the number of elements in the list
    d) Returns the sum of all elements in the list

14. Given the following list, what is the output of min(my_list)?
    my_list = [0, 2, 4, 1, 5]
    result = min(my_list)

    a) 0 #correct
    b) 1
    c) 4
    d) 5

15. Given the following list, what is the output of max(my_list)?
    my_list = [0, 2, 4, 1, 5]

    a) 0
    b) 1
    c) 4
    d) 5 #correct

16. Which list method can be used to find the number of occurrences 
of a specific element in a list?
    a) count() #corrent
    b) len()
    c) sum()
    d) max()

17. What is the output of the following code snippet?
    my_list = [1, 2, 3, 4, 5]
    my_list.reverse()
    print(my_list)

    a) [1, 2, 3, 4, 5]
    b) [5, 4, 3, 2, 1] # correct
    c) [1, 2, 3, 4]
    d) [5, 4, 3, 2]

18. What is the output of the following code snippet? 
    my_list = [1, 2, 3] 
    my_list.insert(1, 4) 
    print(my_list)

    a) [1, 2, 3] 
    b) [1, 4, 2, 3]  #correct
    c) [4, 1, 2, 3] 
    d) [1, 2, 4, 3] 

19. Which method is used to remove all elements from a list? 
    a) clear() #correct
    b) remove_all() 
    c) delete_all() 
    d) reset() 

20. What is the output of the following code snippet? 
    my_list = [1, 2, 3, 4, 5] 
    result = sum(my_list) 
    print(result)

    a) 15  #correct
    b) [1, 2, 3, 4, 5] 
    c) [5, 4, 3, 2, 1] 
    d) 10 

21. What is the output of the following code snippet? 
    my_list = [1, 2, 3, 4, 5] 
    result = my_list.index(3) 
    print(result)

    a) 0 
    b) 1 
    c) 2  #correct
    d) 3
"""