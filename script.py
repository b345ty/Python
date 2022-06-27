#!/bin/python3
#Variables And Methods

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

print ('\n')
#Functions
print ("Here is an example of a function:")
def who_am_i(): # This is a function
    name = "Sipho" # String "Sipho"
    age = 50       # Integer (50)
    gpl = 3.7      # Float   (3.7)
    print ("My name is " + name + " and my age is " + str(age) + " years old.") 
who_am_i()


