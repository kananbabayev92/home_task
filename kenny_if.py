"""
Instructions: Write Python code for each of the following tasks. 
Make sure to use if statements appropriately to achieve the desired outcomes. 
If appropriate, comment your code to explain each step.

- If Statements -
A. Create any variable with Boolean value. Print 'My variable evaluates to True'
if this variable is 'True', otherwise print 'My variable evaluates to False'.

x = 10
if x > 5:
    print("My variable evaluates to True")
else:
    print("My variable evaluates to False)



B. Create a variable named 'temperature'. Make it equal to any degree. Check: 
1. If temperature is under 10 degrees, print 'It\'s cold outside, take a scarf.'.
2. If temperature is in interval from 10 to 24 degrees (both included), print 
'It\'s a nice weather. Let\'s go for a walk.'.
3. If temperature is above 24 degrees, print 'It\'s quite hot, I need an AC.'.

temperature = 15

if temperature < 10:
    print("It's cold outside, take a scarf.")
elif 10 <= temperature <= 24:
    print("It's a nice weather. Let's go for a walk.")
else:
    print("It's quite hot, I need an AC.")


C. Create a variable named 'age'. Make it equal your age. Check:
1. If it's under 18, print 'I am not eligible for voting :('
2.If you are 18 or older, print 'I am eligible for voting!'

my_age = 32

if my_age < 18:
    print("I am not eligible for voting :(")
else:
    print("I am eligible for voting!")


D. Create variables 'a' and 'b'. Make them equal 15 and 20 correspondingly.
Check if their sum gives less than 40, print their sum and add 'It\'s less than 40.'.
Otherwise, print their sum and add 'It makes 40 or more than 40.'. 

a = 15
b = 20

if a + b < 40:
    print(f"{a + b} It's less than 40.")
else:
    print(f"{a + b} It makes 40 or more than 40.")





E. Create a list with 4 students (make it contain their names). Check if the 
length of that list is less than 5, add new student to that list.

students = ["Leyla", "Kanan", "Veli", "Intiqam"]

if len(students) < 5:
    students.append("Asim")
print(students)


F. Create four variables (a, b, c, d) with numeric (int & float) values. 
Write the logical expression to check if 'a' is greater than 'b' and 'c' is greater
than 'd'.
a = 10      
b = 20.5  
c = 30    
d = 40.75

if a > b and c > d:
    print(f"{a} is greater than {b} and {c} is greater than {d}.")
else:
    print(f"{b} is greater than {a} and {d} is greater than {c}.")


G. Write a program to check whether a number accepted from user is divisible by 2
and 3 both. 

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is divisible by 2.")
elif number % 3 == 0:
    print("The number is divisible by 3.")
else:
    print("The number is not divisible by 2 and 3.")


H. Write a program that finds the largest number out of three numbers accepted from user. 

 
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))


    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3

    print(f"The largest number is {largest}")

I. Write a program that gets any input from user. It should print 'Lower job!' if all
characters in user's input are lowercase, otherwise print 'Upper job!'. 
input_user = input(">>").strip()

if input_user == input_user.upper():
    print(f"{input_user}, upper word")
elif input_user == input_user.capitalize():
    print(f"{input_user}, capitalize word")
else:
    print(f"{input_user}, lower word")




J. Write a program to check whether a number entered by user is three digit number or not. 

number = input("Enter a number: ")

if len(number) == 3 and number.isdigit():
    print("The number is a three-digit number.")
else:
    print("The number is not a three-digit number.")


K. Accept the temperature in degree Celcis of water and check whether it's boiling or
not (boiling point of water is 100 degree Celcius). 

temperature = float(input("Enter the temperature in Celsius: "))

if temperature >= 100:
    print("The water is boiling.")
else:
    print("The water is not boiling.")


    
L. Accept the IQ of 3 people and display the highest one. 
iq1 = int(input("Enter the IQ of the first person: "))
    iq2 = int(input("Enter the IQ of the second person: "))
    iq3 = int(input("Enter the IQ of the third person: "))

    if iq1 >= iq2 and iq1 >= iq3:
        highest_iq = iq1
    elif iq2 >= iq1 and iq2 >= iq3:
        highest_iq = iq2
    else:
        highest_iq = iq3

    print(f"The highest IQ is {highest_iq}")


M. Write a program to check whether a character accepted from user is vowel or not. 
char = input("Enter a character: ").lower()
vowel_char = "aeiou"

    if char in vowel_char:
        print("The character is a vowel.")
    else:
        print("The character is not a vowel.")


N. Accept the following from the user and calculate the percentage of class attendance: 
1. Total number of class days
2. Total number of days for absence


O. Accept the percentage from the user and display the grade according to the following 
criterias: 
1. Below 25 - D
2. 25 to 45 - C
3. 45 to 50 - B
4. 50 to 60 - B+
5. 60 to 80 - A
6. Above 80 - A+

ercentage_user = float(input("Add percentage: "))

if percentage_user < 25:
    grade = "D"
elif  25 <= percentage_user <= 45:
    grade = "C"
elif  45 <= percentage_user <= 50:
    grade = "B"
elif  50 <= percentage_user <= 60:
    grade = "B+"
elif  60 <= percentage_user <= 80:
    grade = "A"
elif  percentage_user > 80:
    grade = "A+"

print(grade)
-------------------------------------------------------------------------------------------------------------------------




- Dictionary Methods -
A. Create a nested dictionary. Get any inner value using multiple key-indexing. 

nested_dict = {
    "person": {
        "name": "Kanan",
        "detail": {
            "age": 30,
            "address": {
                "city": "Baku",
                "zipcode": "1089"
            }
        }
    }
}

city = nested_dict["person"]["detail"]["address"]["city"]
print(f"The city is: {city}")



B. Create a dictionary with your personal data (name, surname, age, family status,
gender). Ask user for any key in your dictionary. Print the value of the given
key from the dictionary. Try to ask all keys. 


personal_data = {
    "name": "Kanan",
    "surname": "Babayev
    "age": 32,
    "family_status": "Single",
    "gender": "Male"
}

key = input("Enter a key (name, surname, age, family_status, gender): ").strip().lower()
if key in personal_data:
    print(f"The value for '{key}' is: {personal_data[key]}")
else:
    print(f"Key '{key}' not found in personal data.")



C. Create a dictionary with stock data of clothes (cloth name + amount). Let 
the user choose any of keys and add some count to it. 

clothes = {
    "shirt": 10,
    "pants": 5,
    "jacket": 2,
    "socks": 20
}
new_clothes = input("Add new clothes: ").strip().lower()
count_clothes = int(input("Add new clothes: "))
clothes[new_clothes] = count_clothes
print(clothes)


D. Copy any dictionary from previous tasks. Print it. 

copy_clothes = clothes.copy()

print(copy_clothes)

E. Clear the dictionary from Task D. Print the length of this dictionary.

clothes.clear()
print(len(clothes))

F. Create an empty dictionary. Let the user add data to it (key & value). Choose
any topic (books, cars, info, items, grades...) and let the user fill it with
minimum 4 key-value pairs. 
data = {}
for _ in range(4):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value
print(data)


G. You have the following dictionary: 
car = {
    "brand": "Chevrolet",
    "model": "Camaro",
    "year": 2017
}
not_found_message = "Value not found"

year = car.get("year", not_found_message)
color = car.get("color", not_found_message)

print(f"Year: {year}")
print(f"Color: {color}")

Create a 'not_found_message' variable. Make it equal appropriate "not found" message.
Try to get 'year's and 'color's values from the 'car'. Set the default value to 
our "not found" message.     



H. Print the first 6 keys from the following dictionary (hint: you should use 
'list()' method to convert dict_keys to list and indexing to get the appropriate

countries_capitals = {
    "USA": "Washington, D.C.",
    "Canada": "Ottawa",
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "Australia": "Canberra",
    "Brazil": "Brasília",
    "India": "New Delhi",
    "South Africa": "Pretoria",
}

first_six_dict = list(countries_capitals.keys())
print(first_six_dict[:6])


I. You have the following dictionary:
programming_languages = {
    "Python": {
        "designed_by": "Guido van Rossum",
        "first_appeared": 1991,
        "paradigm": "Multi-paradigm",
        "typing": "Dynamic",
        "popularity": "High"
    },
    "JavaScript": {
        "designed_by": "Brendan Eich",
        "first_appeared": 1995,
        "paradigm": "Multi-paradigm",
        "typing": "Dynamic",
        "popularity": "Very High"
    },
    "Java": {
        "designed_by": "James Gosling",
        "first_appeared": 1995,
        "paradigm": "Object-oriented",
        "typing": "Static",
        "popularity": "High"
    },
    "C++": {
        "designed_by": "Bjarne Stroustrup",
        "first_appeared": 1985,
        "paradigm": "Multi-paradigm",
        "typing": "Static",
        "popularity": "Moderate"
    }
}

Using in f-strings print the year Python was appeared value.


python = programming_languages["Python"]
print(f"Python first appeared in {python["first_appeared"]}")

J. You have the following code snippet:
tasks = {
    "Alice": ["Buy groceries", "Finish report", "Call the doctor"],
    "Bob": ["Walk the dog", "Pay bills", "Read a chapter"]
}

selected_person = "Alice"
new_task = "Go to the gym"

up_task = tasks["Alice"].append("Go to the gym")

print(tasks)

Add the new task to the selected person's tasks. Print the tasks & length of tasks 
before and after edition.





K. There is a dictionary method that helps to create a dictionary with a collection
of keys and apply a default value to that key. Using that method create a dictionary
with all values equal to the '[0, 4, 8, 12, 16, 20]' list and keys should only be
the numbers from 0 to 4, so your dictionary should look like: 
digits = [1, 2, 3, 4, 5]

my_dict = {
    0: [0, 4, 8, 12, 16, 20],
    1: [0, 4, 8, 12, 16, 20],
    2: [0, 4, 8, 12, 16, 20],
    3: [0, 4, 8, 12, 16, 20],
    4: [0, 4, 8, 12, 16, 20],
}

You should use list comprehension in this task. 

Then you should print some portion from the list values of a dictionary. The
portion size depends on a key you are using to index the list. 



L. Print all items, values, keys from 'programming_languages' dictionary.

programming_languages = {
    "Python": {
        "designed_by": "Guido van Rossum",
        "first_appeared": 1991,
        "paradigm": "Multi-paradigm",
        "typing": "Dynamic",
        "popularity": "High"
    },
    "JavaScript": {
        "designed_by": "Brendan Eich",
        "first_appeared": 1995,
        "paradigm": "Multi-paradigm",
        "typing": "Dynamic",
        "popularity": "Very High"
    },
    "Java": {
        "designed_by": "James Gosling",
        "first_appeared": 1995,
        "paradigm": "Object-oriented",
        "typing": "Static",
        "popularity": "High"
    },
    "C++": {
        "designed_by": "Bjarne Stroustrup",
        "first_appeared": 1985,
        "paradigm": "Multi-paradigm",
        "typing": "Static",
        "popularity": "Moderate"
    }
}
print("Values:", programming_languages.values())
print("Keys:", programming_languages.keys())


M. Remove 'Java' from 'programming_languages' dictionary & get its value. Print it. 
java_remove = programming_languages.pop("Java")

print(programming_languages)
print("Java:", java_remove)


N. Remove the last item from the following dictionary and print it:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car.popitem()
print(car)


O. Expand 'programming_languages' dictionary with the following data:
language_to_add = {
    "PHP": {
        "designed_by": "Rasmus Lerdorf",
        "first_appeared": 1995,
        "paradigm": "Server-side scripting",
        "typing": "Dynamic",
        "popularity": "Moderate"
    }
}
programming_languages.update(language_to_add)
print(programming_languages)





P. Use 'setdefault' method on any dictionary. 
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car.setdefault("color", "red")
print(car)


Q. Which Data Types can be represented as values of any dictionary?
R. In the following example: 
data = {
    "Python3.x": {
        "Wep Development", "Machine Learning", "Penetration Testing", "Game Development"
    }
} 
edit_error = data.get("Python2.x", "Key not found")
print(edit_error)

It's giving an error if you try to get 'Python2.x' in this way:
data["Python2.x"]
Edit this code so it doesn't return an error.



-----------------------------------------------------------------------------------------------------------



- Chat GPT's Homework -
Task 1.
Create an empty dictionary called student_info.
Add the following key-value pairs to the dictionary: 
"name": "John Doe"
"age": 20
"major": "Computer Science"
student_info = {
    "name": "John Doe",
    "age": 20,
    "major": "Computer Science"
}


Task 2.
Print the value associated with the key "name" from the student_info dictionary.
Change the value of the "age" key to 21. 
Add a new key-value pair: "gender": "Male".  

student_info["age"] = 21
print(student_info["name"])

student_info["gender"] = "Male"

Task 3.
Create a new dictionary called grades with the following data: 
"math": 85
"english": 92
"history": 78
Use the update method to add the key-value pairs from the grades dictionary into the student_info dictionary.
grades = {
    "math": 85,
    "english": 92,
    "history": 78
}
student_info.update(grades)

Task 4.
Remove the "history" key from the grades dictionary using the pop method, and print the value that was removed. 

removed_value = grades.pop("history")
print(removed_value)

Remove the "major" key from the student_info dictionary using the del statement. 
del student_info["major"]
print(student_info)

Task 5: Basic If-Else Statements
Write a Python program that does the following: 
Takes an integer input from the user.
Checks if the input is greater than 10.
If it is, prints "The number is greater than 10."
If it's not, prints "The number is not greater than 10."

number = int(input("Enter an integer: "))
if number > 10:
    print("The number is greater than 10.")
else:
    print("The number is not greater than 10.")


Task 6: Multiple Conditions
Write a Python program that: 
Takes two integer inputs from the user.
Checks if both numbers are even (divisible by 2).
If both are even, prints "Both numbers are even."
If at least one is not even, prints "At least one number is not even."

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even.")
else:
    print("At least one number is not even.")

Task 7: Grade Calculator
Write a Python program that: 
Takes a numerical score as input from the user (0 to 100).
Uses if-elif-else statements to determine the corresponding letter grade based on the following scale:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59
Prints the calculated letter grade.

score = int(input("Enter your score (0-100): "))

if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 89:
    grade = 'B'
elif 70 <= score < 79:
    grade = 'C'
elif 60 <= score < 69:
    grade = 'D'
else:
    grade = 'F'

print(f"Your grade is: {grade}")



Task 8: Leap Year Checker
Write a Python program that:
Takes a year as input from the user.
Checks if the year is a leap year or not.
A leap year is divisible by 4, but not divisible by 100 unless it's also divisible by 400.
Prints "Leap year" or "Not a leap year" accordingly.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")




Task 9: Temperature Converter
Write a Python program that: 
Takes a temperature in Celsius as input from the user.
Converts it to Fahrenheit using the formula: Fahrenheit = (Celsius * 9/5) + 32.
Prints the temperature in Fahrenheit.

temp = float(input("Enter a temperature: "))
Fahrenheit = (Celsius * 9/5) + 325
print(fahrenheit)

Task 10: Number Comparison
Write a Python program that: 
Takes three integer inputs from the user.
Determines and prints the largest of the three numbers using if-else statements.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is {largest}")



Task 11: Positive or Negative
Write a Python program that:
Takes an integer as input from the user.
Checks if the number is positive, negative, or zero.
Prints "Positive," "Negative," or "Zero" accordingly.

number = int(input("Enter number: "))

if number > 0:
    print("It's number Positive")
else:
    print("it's number Negative")



Task 12: Eligibility Checker
Write a Python program that: 
Takes the age and citizenship status (True for U.S. citizen, False for non-U.S. citizen) as input from the user.
Checks if the person is eligible to vote in the U.S. based on the following conditions:
Must be at least 18 years old.
Must be a U.S. citizen.
Prints "You are eligible to vote" or "You are not eligible to vote" accordingly.


age = int(input("How old are you? >> ").strip().lower())
citizien_status= input("Are you U.S. citizen? yes or no? >> ").strip().lower()

if age >= 18 and citizien_status == "yes":
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")



Task 13: Password Strength Checker
Write a Python program that:
Takes a password as input from the user.
Checks the strength of the password based on the following criteria:
At least 8 characters long.
Contains both uppercase and lowercase letters.
Contains at least one digit (0-9).
Prints "Strong password" or "Weak password" accordingly.

import string
enter_pass = input("Enter password for check: ").strip().replace(" ","") 
digits = range(0, 10)
letters = string.ascii_letters
if len(enter_pass) >= 8 and (char in letters for char in enter_pass): 
    print("Password is valid")
else:
    print("Password is invalid")
print(enter_pass) 




Task 14: Rock-Paper-Scissors Game

Implements a simple text-based rock-paper-scissors game.
Takes the player's choice as input (rock, paper, or scissors).
Generates a random choice for the computer.
Determines the winner based on the game rules.
Prints the result of the game (win, lose, or tie) and the computer's choice. 

import random
choices = ["rock", "paper", "scissors"]

player_choice = input("Enter your choice (rock, paper, or scissors): ").lower().split()
computer_choice = random.choice(choices)
player_choice = " ".join(player_choice)

if player_choice == computer_choice:
    result = "It's a tie!"
elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "paper" and computer_choice == "rock") or \
     (player_choice == "scissors" and computer_choice == "paper"):
    result = "You win!"
else:
    result = "You lose!"

print(f"Player choice: {player_choice}")
print(f"Computer choice: {computer_choice}")
print(result)



- Comments -
A. One-line comment in any random three places of your code, if it's appropriate.
B. Multi-line comment anywhere in your code, if it's appropriate.

______________________________________________________________________________________________________

Quiz. (If-Statements)
1. What is the keyword used to define an 'if' statement in Python?
    a) if #correct
    b) case
    c) switch
    d) when

2. How do you write an if statement in Python?
    a) if condition: #correct
    b) if (condition)
    c) if {condition}
    d) if [condition]

3. In Python, what is the symbol for 'not equal to' in an if statement?
    a) ==
    b) != #correct
    c) <=
    d) >=

4. In Python, what is the purpose of the 'elif' statement?
    a) It is used for error handling.
    b) It is executed if the 'if' condition is True.
    c) It is executed if the 'if' condition is False. #correct
    d) It is executed if the 'if' condition is True, and no 'else' condition is present.

5. What will be the output of the following Python code?
    if 10 > 5:
        print("10 is greater than 5")
    else:
        print("This will not be printed")

    a) 10 is greater than 5 #correct
    b) This will not be printed
    c) SyntaxError
    d) 5 is greater than 10

6. What is the output of the following Python code?
    x = 15
    if x < 10:
        print("x is less than 10")
    elif x < 20:
        print("x is less than 20 but greater than or equal to 10")
    else:
        print("x is 20 or greater")

    a) x is less than 10
    b) x is less than 20 but greater than or equal to 10 #correct
    c) x is 20 or greater
    d) x is 15

7. What is the primary purpose of an 'if' statement in Python?
    a) To execute a specific block of code based on a condition. #correct
    b) To create loops in a program.
    c) To define a function.
    d) To print output to the console.

8. When is an 'else' statement used in conjunction with an 'if' statement?  
    a) To execute the code block if the 'if' condition is True.
    b) To execute the code block if none of the 'if' or 'elif' conditions are True. #correct
    c) To execute the code block regardless of the 'if' condition.
    d) To define a loop within the 'if' statement.

9. Consider the following Python code. What will be printed if the variable 'num' is greater than or equal to 20?
    num = 25
    limit = 20

    if num >= limit:
        print("The number is greater than or equal to the limit")
    else:
        print("The number is less than the limit")

    a) The number is greater than or equal to the limit #correct
    b) The number is less than the limit
    c) The number is exactly the limit
    d) There is a syntax error in the code

10. Given the Python code snippet:
    num = 15

    if num > 10:
        print("num is greater than 10")

    What will be the output if this code is executed?

    a) num is greater than 10 #coorect
    b) num is less than 10
    c) num is 10
    d) num is equal to 15

11. Given the Python code snippet:
    x = 15

    if x > 10 and x < 20:
        print("x is greater than 10 and less than 20")
    else:
        print("x is either less than or equal to 10 or greater than or equal to 20")

    What will be the output if this code is executed?
    a) x is greater than 10 and less than 20 #correct
    b) x is either less than or equal to 10 or greater than or equal to 20
    c) x is 10
    d) x is 20

12. Given the Python code snippet:
    y = 5

    if y < 0 or y > 10:
        print("y is less than 0 or greater than 10")
    else:
        print("y is between 0 and 10 (inclusive)")

    What will be the output if this code is executed?
    a) y is less than 0 or greater than 10 #correct
    b) y is between 0 and 10 (inclusive)
    c) y is 0
    d) y is 10

13. Given the Python code snippet:
    x = 8

    if x < 10:
        print("Code block 1: x is less than 10")
    elif x < 15:
        print("Code block 2: x is less than 15")
    elif x < 20:
        print("Code block 3: x is less than 20")
    else:
        print("Code block 4: x is 20 or greater")

    What will be the output if this code is executed when x is 8?
    a) Code block 1: x is less than 10 #correct
    b) Code block 2: x is less than 15
    c) Code block 3: x is less than 20
    d) Code block 4: x is 20 or greater

14. Given the Python code snippet:
    y = 25

    if y < 10:
        print("Code block 1: y is less than 10")
    elif y < 15:
        print("Code block 2: y is less than 15")
    elif y < 20:
        print("Code block 3: y is less than 20")
    else:
        print("Code block 4: y is 20 or greater")

    What will be the output if this code is executed when y is 25?
    a) Code block 1: y is less than 10
    b) Code block 2: y is less than 15
    c) Code block 3: y is less than 20
    d) Code block 4: y is 20 or greater #correct



    _____________________________________________________________________________________________________      
Quiz. (Dictionaries)
1. Which of the following are true of Python dictionaries: 
    a) Dictionaries are mutable #true
    b) Items are accessed by their position in a dictionary
    c) A dictionary can contain any object type except another dictionary
    d) Dictionaries can be nested to any depth #correct
    e) Dictionaries are accessed by key #correct
    f) All the keys in a dictionary must be of the same type

2. Consider this dictionary: 
    d = {'foo': 100, 'bar': 200, 'baz': 300}
    What is the result of this statement: 
    d['bar':'baz']

    a) (200, 300)
    b) [200, 300] #correct
    c) 200 300
    d) It raises an exception 

3. Suppose x is defined as follows:
    x = [
        'a',
        'b',
        {
            'foo': 1,
            'bar':
            {
                'x': 10,
                'y': 20,
                'z': 30
            },
            'baz': 3
        },
        'c',
        'd'
    ]

What is the expression involving x that accesses the value 30? 

4. Select the correct ways to get the value of marks key.
    student = {
    "name": "Emma",
    "class": 9,
    "marks": 75
    }

    a) m = student.get(2)
    b) m = student.get('marks') #
    c) m = student[2])
    d) m = student['marks'])

5. Dictionary keys must be immutable:
    a) True #
    b) False

6. Select the all correct way to remove the key marks from a dictionary: 
    student = { 
        "name": "Emma",
        "class": 9,
        "marks": 75
    }

    a) student.pop("marks")#
    b) del student["marks"] #
    c) student.remove("marks")
    d) student.popitem("marks") 

7. What is the output of the following dictionary operation:
    dict1 = {"name": "Mike", "salary": 8000}
    temp = dict1.get("age")
    print(temp)

    a) KeyError: 'age' 
    b) None #correct

8. Items are accessed by their position in a dictionary and all the keys in a 
dictionary must be of the same type: 
    a) True
    b) False

9. Select all correct ways to copy a dictionary in Python: 
    a) dict2 = dict1.copy() # correct
    b) dict2 = dict(dict1) #correct
    c) dict2 = dict1

10. Please select all correct ways to empty the following dictionary:
    student = { 
        "name": "Emma", 
        "class": 9, 
        "marks": 75 
    }
    a) del student
    b) del student[0:2]
    c) student.clear() #correct

11. What is the output of the following: 
    sample_dict = dict([
        ('first', 1),
        ('second', 2),
        ('third', 3)
    ])
    print(sampleDict) # burda error var

    a) [ ('first', 100), ('second', 200), ('third', 300) ]
    b) Options: SyntaxError: invalid syntax #coorrect
    c) {'first': 1, 'second': 2, 'third': 3} #correct

12. Select the correct way to access the value of a history subject: 
    sample_dict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }

    a) sample_dict['class']['student']['marks']['history'] #correct
    b) sample_dict['class']['student']['marks'][1]
    c) sample_dict['class'][0]['marks']['history']

13. Select the correct way to print Emma's age: 
    student = {
        1: {'name': 'Emma', 'age': '27', 'sex': 'Female'},
        2: {'name': 'Mike', 'age': '22', 'sex': 'Male'}
    }

    a) student[0][1]
    b) student[1]["age"] #correct
    c) student[0]["age"]

14. What is the output of the following dictionary operation:
    dict1 = {"name": "Mike", "salary": 8000}
    temp = dict1.pop("age")
    print(temp)

    a) KeyError: 'age' #correct
    b) None

15. What is the output of the following code:
    dict1 = {"key1": 1, "key2": 2}
    dict2 = {"key2": 2, "key1": 1}
    print(dict1 == dict2)

    a) True correct
    b) False

16. Select correct ways to create an empty dictionary:
    a) sample_dict = { } 
    b) sample_dict = dict() # correct
    c) sample_dict = dict{}
"""