"""
Note. All tasks should be written as in the following example (you can
use variable naming method or adding a comment after the expression):
# A
expression = True and False or True
step_one = (True and False) or (True)
step_two = (False) or (True)
step_three = True
print(step_three == expression)

At the end, your program should only print 'True's, so that will mean
you have accomplished and simplified all expressions correctly.

- Booleans -
Simplify these expressions:
A. True or False and True  # step one = True or False, step two = True

B. False and False or False  #  step one = False and False, step two = False 

C. (True or False) and True # step_one = True and True step_two = true

D. True or (True or False and True) and True # step_one = True or True and True,  step_two = True

E. False or False and False and not False  # step_one = False or False and True, two_step = False

F. (True or True or False) and True  # step_one = True and True, step_two = True

G. False or (True and False)  # step_one = False

H. False and False and False and False and False or True and False   #  step_one = False or true and false, step_two = False 

I. True or False or True # True

J. False or (not False)  #True

K. not True or not False # step_one = False or True, step_two = True

L. False and not False or not False  # True

M. True or not False and True or not not True    # step_one = True or True or True , step_two = True

N. not not not False  # True

O. not N (previous task N's value) # true (true) print(true)

P. True or False and not True or (not True and False) and not True or False 
#  true or       false         or           False                  or False  # True     


Q. True or not False or not True or True # True

R. False and (not True or False or (False or not True and True or False)) and True # False

S. False and not not not True and (False or True or not False) and True or False
# False and True and True and True or False 
        False             and True or False
            False or False 
                False

T. not (True or False) or not False or (True and False or False) # False
U. (True or not not False) and (True or (True or (False)))  # step_one = True and True, step_two = True

V. False and False or (not False and (not False)) 
      False  or (True and True)
            False or True
                True

W. (not True or not False) and (not True or (not False)) # True


X. False or False and not True or not False and (not True and False) # False
 

Y. True and True and True and True and not True and True and True or False 
# True and True and True and True and False or False
    True and True and True and False or False
                False or False
                    False
      

Z. False and False and (True or not False and (True or False and True)) or not True and False and (not False or not True) 
        # False    and            (True or True)                        or   False  and               (True or False)
        # False    and            True                                or   False  and               True
        # False    and            True                                or   False
        # False    and            True
        # False

"""