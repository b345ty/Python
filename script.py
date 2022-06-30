#!/bin/python3
#Variables And Methods
print ("Variables And Methods")

quote = "Badgers do not care."
print (quote.upper()) # Uppercase
print (quote.lower()) # Lowercase
print (quote.title()) # Title case

print (len(quote)) # Number of chracters in quote.

name = "Sipho" # String "Sipho"
age = 50       # Integer (50)
gpl = 3.7      # Float   (3.7)

print (name)
print (age)
print (gpl)

print (int(age)) # Output 50
print (float(3.9)) # Output 3

print ("My name is " + name + " and my age is " + str(age) + " years old.") # Cannot concaternagte a integer, add str() to age variable.

age += 1 

print ("I am a year older " + str(age) + " years today.")


birthday  = 1
age += birthday
print (age)

#Print New Line
print ("Print New Line")
print ('\n')

#Functions
print ("Here is an example of a function:")
def who_am_i(): # This is a function
    name = "Sipho" # String "Sipho"
    age = 50       # Integer (50)
    gpl = 3.7      # Float   (3.7)
    print ("My name is " + name + " and my age is " + str(age) + " years old.") 
who_am_i()

print ("Multiply Function")
def multiply(x,y):
        return x * y

multiply(7,7) # Only calculation!
print(multiply(7,7))


print ("Square Roor Function:")
def square_root(x):
        print(x ** .5)
        
square_root(64)

print ("New Line Function:")
def nl():
        print('\n')
        
nl()

#BOOLEAN EXPRESSIONS (True or False)
print ("Boolean expressions:")

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1, bool2, bool3, bool4)
print(type(bool1))

bool5 = "True"
print (type(bool5))

nl()

#Relational and Boolean Operators
print ("Relational and Boolean Operators")
greater_than = 7 > 5

less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_not = not True #False

nl()

#CONDITIONAL STATEMENTS
print ("Conditional Statements:")
def drink(money):
        if money >= 2:
                return "You've got yourself a drink!"
        else:
                return "No drink for you!"

print (drink(3))
print (drink(1))

def alcohol(age,money):
        if (age >= 21) and (money >= 5):
                return "We're getting a drink!"
        elif (age >= 21) and (money < 5):
                return "Come back with more money."
        elif (age < 21) and (money >= 5):
                return "Nice try, kid!"
        else:
                return "You're too poor and too young!"

print (alcohol(21,5))
print (alcohol(21,4))
print (alcohol(20,5))
print (alcohol(20,4))

