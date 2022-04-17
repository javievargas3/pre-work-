

def hello_name(user_name):
    print("hello "+ user_name + "!")



#Write a python function, 
#first_odds that prints the odd numbers from 1-100 and returns nothing 

def first_odds():
    for i in range (0, 101):
        if (i % 2 == 1):
            print (i)


 #Please write a Python function, 
 # max_num_in_list to return the max number of a given list. 
 # The first line of the code has been defined as below. 

def max_num_in_list(a_list):
     max = 0
     for i in a_list:
         if (i > max):
             max = i 
     return max 

#Write a function to return if the given year is a leap year.
# A leap year is divisible by 4, but not divisible by 100 unless 
# it is also divisible by 400. 
# The return should be boolean Type (true/false). 
def is_leap_year(a_year):
    if (a_year % 4 == 0):
        if (a_year % 100 != 0):
           return True 
        elif (a_year % 400 == 0):
            return True 
    else:
        return False 


#Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers,
#  but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. 

def is_consecutive(a_list):
    b = True
    for i in range(len(a_list) - 1):
        if (a_list[i + 1] != a_list[i] + 1):
            b = False 
    return b 
