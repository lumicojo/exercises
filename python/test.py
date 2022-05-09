
# 1
#Given a list of integers, determine whether the sum of its elements is odd or even.

#Give your answer as a string matching "odd" or "even".

#If the input array is empty consider it as: [0] (array with a zero).
#Examples:
#Input: [0]
#Output: "even"

#Input: [0, 1, 4]
#Output: "odd"

#Input: [0, -1, -5]
#Output: "even"

#import codewars_test as test
#from solution import odd_or_even

#@test.describe("Fixed Tests")
#def fixed_tests():
    #@test.it('Basic Test Cases')
    #def basic_test_cases():
        #test.assert_equals(odd_or_even([0, 1, 2]), "odd")
        #test.assert_equals(odd_or_even([0, 1, 3]), "even")
        #test.assert_equals(odd_or_even([1023, 1, 2]), "even")




### 2

#Your task is to create the functionisDivideBy 
# (or is_divide_by) to check if an integer number
#  is divisible by both integers a and b.
#(-12, 2, -6)  ->  true
#(-12, 2, -5)  ->  false

#(45, 1, 6)    ->  false
#(45, 5, 15)   ->  true

#(4, 1, 4)     ->  true
#(15, -5, 3)   ->  true

#def is_divide_by(number, a, b):
    #return # good luck
#import codewars_test as test
#from solution import is_divide_by

#@test.describe("Fixed Tests")
#def fixed_tests():
    #@test.it('Basic Test Cases')
    #def basic_test_cases():
        #test.assert_equals(is_divide_by(8, 2, 4), True)
        #test.assert_equals(is_divide_by(12, -3, 4), True)
        #test.assert_equals(is_divide_by(8, 3, 4), False)
        #test.assert_equals(is_divide_by(48, 2, -5), False)
        #test.assert_equals(is_divide_by(-100, -25, 10), True)
        #test.assert_equals(is_divide_by(10000, 5, -3), False)
        #test.assert_equals(is_divide_by(4, 4, 2), True)
        #test.assert_equals(is_divide_by(5, 2, 3), False)
        #test.assert_equals(is_divide_by(-96, 25, 17), False)
        #test.assert_equals(is_divide_by(33, 1, 33), True)

### 3
##Trolls are attacking your comment section!

#A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

#Your task is to write a function that takes a string and return a new string with all vowels removed.

#For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

#Note: for this kata y isn't considered a vowel.#

#def disemvowel(string_):
    #return string_

 #import codewars_test as test
#from solution import disemvowel

#@test.describe("Fixed Tests")
#def basic_tests():
    #@test.it("First fixed test")
    #def fixed_test_1():
        #test.assert_equals(disemvowel("This website is for losers LOL!"),
        #  "Ths wbst s fr lsrs LL!")#   
###4

 #In this Kata, you will be given a string and your task will be to return
 #  a list of ints detailing the count of uppercase letters, 
 # lowercase, numbers and special characters, as follows.

#Solve("*'&ABCDabcde12345") = [4,5,5,3]. 
#--the order is: uppercase letters, lowercase, numbers and special characters.  
# 
# In this Kata, you will be given a string and your task will be to return a list of ints detailing the count of uppercase letters, lowercase, numbers and special characters, as follows.

#In this Kata, you will be given a string and your task will be to return a list of ints detailing the count of uppercase letters, lowercase, numbers and special characters, as follows.

#def solve(s):
#pass

#test.it("Basic tests")
#test.assert_equals(solve("Codewars@codewars123.com"),[1,18,3,2])
##test.assert_equals(solve("bgA5<1d-tOwUZTS8yQ"),[7,6,3,2])
#test.assert_equals(solve("P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H"),[9,9,6,9])
#test.assert_equals(solve("RYT'>s&gO-.CM9AKeH?,5317tWGpS<*x2ukXZD"),[15,8,6,9])
#test.assert_equals(solve("$Cnl)Sr<7bBW-&qLHI!mY41ODe"), [10,7,3,6])
#test.assert_equals(solve("@mw>0=QD-iAx!rp9TaG?o&M%l$34L.nbft"), [7,13,4,10])

