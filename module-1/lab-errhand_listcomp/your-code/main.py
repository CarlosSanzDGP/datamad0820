#Example: 

eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)

#Insert here the module/library import statements 

import math 

import os, sys

import random


#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results

square = [n**2 for n in range(1,21)]


#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results

power_of_two = [2**n for n in range(1,51)]


#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results

sqrt = [1/n for n in range(1,100)] 
#este primero te lo dejo para que lo veas. Que no me he dado cuenta de la cagada hasta el ultimisimo momento de repaso.

sqrt = [math.sqrt(n) for n in range(1,100)] 

#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results

my_list = [n for n in range(-10, 1)]

print(my_list)

#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results

odds = [n for n in range(1,101) if n%2!=0]


#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results

divisible_by_seven = [n for n in range(1,1001) if n%7==0]



#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience

teststring = 'Find all of the words in a string that are monosyllabic'
non_vowels = [l for l in teststring if l not in "aeiou"]

print("".join(non_vowels))

#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results

capital_letters = [l for l in 'The Quick Brown Fox Jumped Over The Lazy Dog' if l.isupper()==True]
print(capital_letters)

#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.

consonants = [c for c in 'The Quick Brown Fox Jumped Over The Lazy Dog' if c not in "aeiou AEIOU"]
print(consonants)


#10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.

#dejo las dos maneras para acordarme de donde lo he sacado
#solo saco los de module 1 pq si no se hace demasiado larga
path = "../.."
dirs = os.listdir( path )
for file in dirs:
   print (file)

files = [file for file in os.listdir("../..")]
files

#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results

#lo he hecho de dos maneras pq son muy diferentes y la segunda es mejor pero la primera tbn me gusta
list1= (random.choices(range(0,100), k=10))
list2= (random.choices(range(0,100), k=10))
list3= (random.choices(range(0,100), k=10))
list4= (random.choices(range(0,100), k=10))
random_lists = [list1, list2,list3, list4]
[print(e) for e in random_lists]


random_lists = [random.sample(range(1,101),k=10) for e in range(4)]
print (random_lists)


#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]

flat_list = [item for sublist in list_of_lists for item in sublist]
print(flat_list)


#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]

# las lista de floats en una sola lista
floats = [float(n) for sublist in list_of_lists for n in sublist]
print(floats)

# LLevo un buen rato intentando hacer una lista de listas con los numeros convertidos, es decir, trabajar con los numero pero 
# no aplanar la lista. Se puede hacer una a una pero no veo como hacerlo rapido. Alguna idea?


#14. Handle the exception thrown by the code below by using try and except blocks. 


for i in ['a','b','c']:
    try:
        print (i**2)
    except:
        print(f'{i} is not a number')


#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use.

x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print('We can not divide by 0, it does not have any sense')
print ('All done')


#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 


abc=[10,20,20]
try:
    print(abc[3])
except IndexError:
    print ("pero no ves que solo tiene tres elementos y le pides el cuarto?")
    

#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 

a=2
b='a'

try:
    x=int(a)/int(b)
    print(x)
except ZeroDivisionError:
    print ('try not to divide by 0')
except ValueError:
    print('Come on lad, this is not a number!')



#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 
 
try:
    f = open('testfile','r')
    f.write('Test write this')
except FileNotFoundError:
    print ("you sure there that file exists?")
    





#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int

try:
    fp = open('myfile.txt')
    line = f.readline()
    i = int(s.strip())
except FileNotFoundError:
    print ("Check the name you wrote. This file does not exist")
except:
    print ("the file exists but there is something wrong")




#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')


try:
    linux_interaction()
except:
    print('This funcion only works in a Linux')
    
# me gustaria saber que hace esta funcion pq la verdad es que no entiendo que pasa. solo he puesto un bloque de try except pero # pero  no se que esta ocurriendo.    



# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.

def squared_int():
    num= input ("Dame un numero cualquiera: ")
    try:
        x = int(num)
        if x%5 == 0: 
             print ("por el culo te la hinco")
        else:    
            print (f'el cuadrado de {num} es {x**2}. La verdad es que lo podias haber hecho de cabeza')
    except:
        print ("en serio no puedes escribir un numero?")
        
### Ojo, falta el while true de este ejercicio. a ver si mas adelante soy capaz de retomarlo. 
        
        

# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 




# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python

Total_Marks = int(input("Enter Total Marks Scored: ")) 
Num_of_Sections = int(input("Enter Num of Sections: "))


