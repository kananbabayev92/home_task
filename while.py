import sys
import os

list_num = []
for num in range(10):
    number = int(input("add number:"))
    if number < 0:
        print("You add negative number")
        sys.exit()
        break
    list_num.append(number)
print(sum(list_num))
print(os.getcwd())