# Day 2 - Revision : 17/11/2026


# Lesson 1: Difference between retrun and print() in a function
# when we use return


def square(num):
    print ("Here we used return")
    return (num*num)

x = square(4) # Here the "x" equals to "16", then we can use it later in the program

# example :
z = x + 10
print (z) #this will display 26

print(" --------------------------------")


# when we use print

def square(num):
    print ("Here we used print")
    print (num*num) 

# the fuction just display the calculation but don't return a result that we could use later

x = square(4)   # Here the function will display the print functions,  such : Here we used print and 16 
                # But "x" equals to "None" and we can't use it later in the program

# example :
z = x + 10
print (z) #this will make an error

#_________________________________________________________________

# Lesson 2 :  Arithmetic Operations in Python reminder
# Integers

print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print ('Division: ', 4 / 2)                         # Division in python gives floating number
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 // 2)   # gives without the floating number or without the remaining
print('Modulus: ', 3 % 2)                           # Gives the remainder
print ('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)                     # it means 3 * 3

# Floating numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)



# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex number: ',(1 + 1j) * (1-1j))

result = (1 + 1j) * (1 - 1j)
print(result)
print(type(result))
print(result.real)
print(result.imag)

# boolean
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Boolean comparison
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Another way comparison 
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('I in Bino', 'I' in 'Bino')         # False - there is no uppercase I
print('B in Bino', 'B' in 'Bino')         # True - B found in the string
print('coding' in 'coding for all')       # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')            # True
print('4 is 2 ** 2:', 4 is 2 ** 2)        # True

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False