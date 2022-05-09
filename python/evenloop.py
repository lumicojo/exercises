#Write a function that takes an integer, num, as an argument. 
# The function should return a list of every even number from 1 to num.
#Break Down Problem
#will need to go up from 1 to ... ? (whatever passed in)

#will need to check each number

#collect evens so they can be returned


#Pseudocode
#Let’s write down the steps we’ll take

# Make a function, takes in num

# Make starting number variable, i

# Loop until i is equal to num

# For each value of i, check if its even

# If it is, add to a list

# Return the list
# Ah! also need to make an empty list to collect even numbers
#Translate to Python
#Skeleton function

def get_evens_up_to(num):
    print(num)

get_evens_up_to(10)  # Call the function
#get while loop

def get_evens_up_to(num):

    i = 1

    while i != num:

        print(i)
        i = i + 1

get_evens_up_to(10)  # Call the function

#Check for even-ness

def get_evens_up_to(num):

    i = 1

    while i != num:

        if i % 2 == 0:
            print(i, "is even!")
        else:
            print(i, "is NOT even")

        i = i + 1

get_evens_up_to(10)  # Call the function
def get_evens_up_to(num):

    i = 1
    evens = []

    while i != num:

        if i % 2 == 0:
            evens.append(i)
        # else:
        #    print(i, "is NOT even")

        i = i + 1

    # print(evens)
    return evens

the_evens = get_evens_up_to(10)  # Call the function
print(the_evens)
#Consider Special Cases
#What special cases are there to consider?

#What if num is less than 1? 
# What should the function return?

#Should the output list include num also?

#Refactoring: What other functions do we know that can do this?

