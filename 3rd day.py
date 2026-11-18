# Revision - Day 3 : 18, nov, 2026

# Lesson 1 : Operation with string 
greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting)) 
# Multiline String
multiline_string = """I am in computer science.
I like coding and see the result"""
print(multiline_string)

# Escape sequence
print('I hope every one enjoying the python challenge.\nDo you ?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('This is a back slash  symbol (\\)') # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')

# String Concatenation
first_name = 'Bino'
last_name = 'SUMU'
space = ' '
full_name = last_name  +  space + first_name
print(full_name) # SUMU Bino

# Checking length of a string using len() builtin function
print(len(first_name))  # 4
print(len(first_name) > len(last_name)) # False
print(len(full_name)) # 9

# Unpacking characters 
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t 
print(d) # h
print(e) # o
print(f) # n

# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n
# If we want to start from right end we can use negative indexing. -1 is the last index
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

# Slicing
shape = 'Polygone'
first_three = shape[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pol
middle = shape[3:6] # starts at three index and up to 3 but not include 6
print(middle) # ygo
# Another way
last_four = shape[-4:]
print(last_four)   # gone
last_three = shape[5:]
print(last_three)   # one

# Skipping character while splitting Python strings
language = 'polygone'
pyn = language[0:7:3] # from zero to seven, display all the letters when skipping 3 times
print(pyn) # pyn

