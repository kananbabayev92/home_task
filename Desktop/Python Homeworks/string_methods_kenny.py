P"""
- Strings -
A. Create a variable called 'long_sentence'. Make it equal a sentence
minimum. Print 'long_sentence's length.

long_sentence = "I love Python. Pyhton best programing language") 
print(len(long_sentence))

B. Replace Print function's 'end' parameter from default '\n' to '\t'.
Write 2 Print functions with it.
print("hello", end="\n")
print("world")


C. Change Print function's 'end' parameter, so that it links values with
stars. Example:
Today*is*a*good*day!

print("Today", end=" ")
print("is", end=" ")
print("a", end=" ")
print("good", end=" ")
print("day", end=" ")

D. Write 3 different Print functions with according string ("He", "is", "cool.")
in such way so you can see this on your console (you can use any method):
He is cool.

a = ["He", "is ", "cool."]  |   print("He", end=" ")        |   print("he\tis\tcool.")
b, c, d = a                 |   print("is", end=" ")        |
print(b, c, d)              |   print("cool.", end=" ")     |



E. The same task as previous (D), but now make it look like:
He#is#cool.
print("He", end="#")
print("is", end="#")
print("cool.")

F. Create a variable named 'color'. Give it a string 'Python' value.
color = "Python"

G. Create a variable named 'item'. Give it a string 'Developer' value.
item = "Developer

H. Use all methods you know about string-formattings and Print function
to concatenate these two variables, so you can see 'Python Developer' on your
console (terminal).
print(color, item)

I. Replace Print function's 'end' parameter from default value to '...'.
Write 3 Print functions with it.
print("He", end="...")
print("is", end="...")
print("cool.")

J. Suppose you have the following variable:
word = "Hello. I am Taylor."
Using slicing method:
1. Create a variable called 'prefix'. Make it equal to 'Hello.' part of 'word' variable. 
2. Create a variable called 'middle_part'. Make it equal to ' I am ' part of 'word' variable.
3. Create a variable called 'name'. Make it equal to 'Taylor.' part of 'word' variable.
prefix = "hello"
middle_part = "I am"
namme = "Taylor"

Create a variable named 'recreated_word' or 'result' and use all previous variables 
(prefix, middle_part, name) to recreate the 'word' phrase.
recreated_word = prefix + middle_part + name
print(recreated_word)

K. Suppose you have the following value:
"abababababa"
Using slicing method, get all 'a' characters from the value and assign it to a
variable, then print that variable.
value = "abababababa"
a = value[::2]
print(a)


L. Create a formula that finds the last index of a string.
word = "Python"
print(word[-1])

M. What is the difference between 1 and "1"? Are they equal values, why?
int = 1
str = "1"

N. Using all your Python knowledge, find the amount of words the following sentence:
"The mission of the Python Software Foundation is to promote, protect, and advance 
the Python programming language, and to support and facilitate the growth of a 
diverse and international community of Python programmers."
"""
""" a = """The mission of the Python Software Foundation is to promote, protect, and advance 
the Python programming language, and to support and facilitate the growth of a 
diverse and international community of Python programmers."""
a.split()
print(len(a.split()))
 """

"""
- String Methods -
A. Use all these string methods and test it in your code:
1. title        a = "elsen" , print(a.title())
2. capitalize   a = "elsen" , print(a.capitalize())
3. count        a = "elsen" , print(a.count())
4. endswith     a = "elsen cool" print(a.endswith("cool"))
5. find         a = "elsen cool" print(a.find("cool"))
6. index        a = "elsen cool" print(a.index("cool"))
7. isalpha      a = "elsen65" print(a.isalpha())
8. isdigit      a = 45 , print(a.isdigit())
9. islower      a = "samir" , print(a.islower())
10. isupper     a = "SAMIR" , print(a.isupper())
11. lower       a = "SAMIR" , print(a.lower())
12. upper       a = "samir" , print(a.upper())
13. replace     a = "somir"  b = a.replace["o", "a"]  , print(b)
14. split       a = "samir"  b = a.split() print(b)
15. strip       a = "  samir  "  b = a.strip() print(b)
16. startswith  a = "Hi Samir"  b = a.startswith("Hi")
17. join      

list = ("I","love Python")
list_join = "+".join(list)
print(list_join)


B. Combine several string methods at once. ----------------------

C. Create any string-valued variable. First, call the 'lower' method on it,
then call 'islower' method. What value will it always give you and why?  true . islower check lower letters
string_value = "Python best!"
lower_string = string_value.lower()
print(lower_string.islower()) 

D. Suppose you have the following variable:
my_value = "Obviously, today is a hot day."
Replace all 'o' characters with 0 (zeros). 

my_value = "Obviously, today is a hot day."
value = my_value.replace("o", "0")
print(value)



E. Count how many times the word 'likes' occured in the following string:
"Sammy likes to swim in the ocean, likes to spin up servers, and likes to smile."

a = "Sammy likes to swim in the ocean, likes to spin up servers, and likes to smile."
print(a.count("likes"))


______________________________________________________________________________________--


- String Formattings -
A. Create a variable 'name' and assign your name to it.
Create a variable 'age' and assign your age to it.
Using the f-string method, create a formatted string that displays your name 
and age in the following format:
"My name is [name] and I am [age] years old."
name = "kanan"
age = 32
print(f"My name is [name] and I am [age] years old.")

B. Create a variable item and assign a string representing an item name.
Create a variable quantity and assign an integer representing the quantity of the item.
Create a formatted string using the old-style % formatting that displays the item 
name and quantity in the following format:
"I want to buy %d units of %s."

print(""I want to buy %d units of %s." %) 
price = 35_000
product = "car"

print("I want to buy %d units of %s." % (price, product))


C. Make your best and create a hard task by your own using string formattings. 


- Chat GPT's Homework -
A. Use the len() function to find the length of the following strings:

1. "programming"    print(len("programming))

2. "python is fun" print(len(.split("python is fun")))

3. "12345" a ="12345" a.split() print(len(a))

B. Convert the following string to uppercase string:
"hello world" 
 a = "hello world"
print(a.upper())

C. Check if the string "python" is present in the following sentence:
"I enjoy programming in Python."
a = "I enjoy programming in Python."
print(a.count(Python))

D. Given the string "programming", access the following elements using positive and negative indexing:



1. The first character   
var = "programming"     
print(var[0])   print(var[-11])   

2. The last character
print(var[10]) print(var[-1])

3. The third character
print(var[2]) print(var[-9])

4. The second-to-last character
 print(var[1:: 1])  print(var[-10:: 1 ])

E. Using string slicing, extract the word "is" from the string:
"Python is a versatile programming language."


sentence = "Python is a versatile programming language."
slice_obj = sentence.split()
slice_obj.remove("is")
result = " ".join(slice_obj)
print(result)



F. Retrieve the substring "quick brown" from the following sentence:
"The quick brown fox jumps over the lazy dog."

sentence = "The quick brown fox jumps over the lazy dog."
list_a = sentence.split()
list_a.remove("quick")
list_a.remove("brown")
final = " ".join(list_a)
print(final)


G. Reverse the following string using slicing:
"redivider"
a = "redivider"
b = a[::-1]

H. Write a program that capitalizes the first letter of each word in the following sentence:
"welcome to the world of programming"

a = "welcome to the world of programming"
print(a.capitalize())

- Interview Questions -
A. Reverse any string using slicing method.  [::-1]
B. Print the whole string using slicing method, not knowing the length of a string. ?


__------------------------------------------------------------------------------------------
- Comments -
A. One-line comment in any random three places of your code, if it's appropriate.
B. Multi-line comment anywhere in your code, if it's appropriate.




____________________________________________________________
Quiz:
A. What does len('Hello ') return?
    a) 4
    b) 5
    c) 6 correct
    d) 'Hello'
    e) "Hello"

B. What is the output of the following code snippet:

    sphere = "Web Development" * 2 + "" * 6
    length = len(sphere)
    print(length)

    a) 15
    b) 20
    c) 25
    d) 30   #correct

C. Which of the operator can be used in Strings?
    a) +   # correct
    b) *
    c) Both of the above 
    d) None of the above

D. What is the output of the following code snippet:
                      4  3    2    5      1   
    comment = "I like your b l u e  p a n t s"
               012345678910111213141516171819
    pattern = comment[19:4:-3]
    print(pattern, len(pattern))

    a) "n lry", 5 correct
    b) "n lry", 4
    c) "n ly", 4
    d) "p ly", 4
    e) "p l ", 4

E. Is the following variable named correctly, why?

    myVariable = "Python is best!"

    a) yes, follows the rules of naming a variable, pythonic code        #   correct ( need use snake case)
    b) no, doesn't follow the rules of naming a variable, non-pythonic code
    c) it depends on the code editor you type
    d) it's not a code written in Python
"""