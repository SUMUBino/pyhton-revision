# Day 2 - Revision : Difference between retrun and print() in a function
#17/11/2026



# when we use return

def square(num):
    print ("Here we used return")
    return (num*num)

x = square(4) # Here the "x" equals to "16", then we can use it later in the program

# example :
z = x + 10
print (z) #this will display 26

#---------------------------------------------------------------------------
print(" ---------------------------------------------------")


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

