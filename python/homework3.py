#1
#What is the purpose of functions?
#A sequence statement that belong together and organize the program.

####2
#What is the difference between print and return?
     #print function = print out in one line of text.
     #return function = give back the value.

#### 3    
# What is the difference between defining a function and calling a function? 
#def = name,  ( colling): = value

#### 4

# B

#### 5 

# A

### ###Function



###Count to 3

def count_to_three():
    """Counts to three and returns nothing."""
    # num = 1 
    # while num <= 3:
    #     print(num)
    #     num += 1 
        # num = num + 1
        
    # nums = [1, 2 ,3]
    # for num in nums:
    #     print(num)
        
    for i in range(4):
        print(i)

####Greater than 10

 #
mylist = [1, 5, 23, 89, 11, 84, 5]
def find_greater_than_10(nums):
    """" function takes one argument: a list of integers and returns a list containing any integers from the argument list that are greater than 10."""

    nums_greater_than_10 = []

    for num in nums:
        if num > 10:
            nums_greater_than_10.append(num)
    # nums_greater_than_10.sort()
    return nums_greater_than_10

# print(find_greater_than_10([1, 5, 23, 89, 11, 84, 5]))

 
###Funy sentence


def get_funny_sentence(name, place):

    funny_sentence = f"Yesterday, {name} sipped tea at a beautiful yet boring bungalow in {place}."

    return funny_sentence

name = "Brighticorn"
place = "SF"

# print(get_funny_sentence(name, place))
# print(get_funny_sentence(name, place))




def get_funny_sentence(name, place):

    funny_sentence = f"Yesterday, {name} sipped tea at a beautiful yet boring bungalow in {place}."

    return funny_sentence

name = "Brighticorn"
place = "SF"

# print(get_funny_sentence(name, place))
# print(get_funny_sentence(name, place))

def find_common_words(words1, words2):
    """ Function takes in two lists of words and returns a list of the words common to both original lists"""

    common_words = []

    for word in words1:
        if word in words2:
            common_words.append(word)
    return common_words
# return multiples

# print(find_common_words(['hello', 'adios', 'goodbye'], ['goodbye', 'hello', 'please']))


#Write a function that takes in 3 integers as arguments and returns a list of numbers from 1 to 100 (inclusive), containing only integers that are evenly divisible by at least one of the integers.

#For example, given 50, 30, and 29, return [29, 30, 50, 58, 60, 87, 90, 100].

def find_divisible_nums(num1, num2, num3):
    """ function takes in 3 integers as arguments and returns a list of numbers from 1 to 100, containing only integers that are evenly divisible by at least one of the intgers"""

    multiples = []

    # num = 1 

    # while num <= 100:
    #     if (num % num1 == 0) or (num % num2 == 0) or (num % num3 == 0):
    #         multiples.append(num)

    #     num += 1

 #Write a function that takes in 3 integers as arguments and returns a list of numbers from 1 to 100 (inclusive), containing only integers that are evenly divisible by at least one of the integers.

#For example, given 50, 30, and 29, return [29, 30, 50, 58, 60, 87, 90, 100].
  
  
    # return multiples

    #alternate solution:
    for n in range(1, 101):
        if (n % num1 == 0) or (n % num2 == 0) or (n % num3 == 0):
            multiples.append(n)
    return multiples

#[29, 30, 50, 58, 60, 87, 90, 100]     

print(find_divisible_nums(50, 30, 29))


#TUPLETS  DICTIONARY


