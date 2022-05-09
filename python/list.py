#Write a while loop that continually asks a user for a number between 50 and 100.

#If the user types a number greater than 100, the program should say “Too high!”.

#If the user types a number less than 50, the program should say “Too low!”.

#If the user types a number between 50 and 100, the while loop should stop. (Hint: Use the break statement.)

while True:
    num = input("write a number between 50 and 100")
    num = int(num)
    
    if  num > 100:
        print("to high")
    if  num < 50:
        print("to low")
    if  num >50 and num <100:
        break
        
students = ["Julia", "Sarah", "Andy", "Charlotte", "Taylor", "Sam"]

for student in students :
    print(student)
    count = 0
    while count < len(students)  :
     print(count)
    students +=1

students = ["Julia", "Sarah", "Andy", "Charlotte", "Taylor", "Sam"]
students.sort ()

for student in students :

    print(student)
#
#Write a function that takes in a list of words. It should return the longest word 
# (the one with the greats amount of characters) in the list.
# ["boo", "a", "I", "hi"] => 'boo'
#print(get_longest_word(["boo", "a", "I", "hi"]))


#How would we create an empty list?
students = []
students.append('lumi')
students.append('kevin')
students.append('carmen')
#
#how to access first student to sign up
students[0]
# how many students we got
len(students)
#>>> meals = ['apple','bbq','chilly','donats']
#>>> meals .append('eggs')
#>>> print(meals)
#['apple', 'bbq', 'chilly', 'donats', 'eggs']
#>>Removing from Lists
#Remove item from end: pop with nothing in parentheses

#Syntax: list_name.pop()

#>>> meals = ['artichokes', 'bbq', 'chili', 'donuts']

#>>> last_meal = meals.pop()
#>>> print(last_meal)
#donuts

#>>> print(meals)
#['artichokes', 'bbq', 'chili']
#pop returns the removed item
#Remove at any index: put index in parentheses after pop
#last_meal = meals.pop()
#>>> print(last_meal)
#bbq
#Syntax: list_name.pop(index)

#SORTING LIST

#list_name.sort()
#>>> meals = ['hummus', 'ice cream', 'grits']
#>>> meals.sort()
#>>> print(meals)
#['grits', 'hummus', 'ice cream']

#Getting List Length

#Syntax: len(list_name)
#>>> print(len(meals))
#
#Items and Indexes
#You can loop over both the item and index with enumerate

#meals = ['artichokes', 'bbq', 'eggs']

#for i, meal in enumerate(meals):
    #print(f'Index is {i}')
    #print(f'Meal is {meal}')

    #Filtering and Updating Items in a List
#colors = ['blue', 'purple', 'blue', 'red', 'red']
#We want to replace every 'blue' with 'aquamarine'.

#The plan:

##for color in colors:
    #if color == 'blue':
        # ...what goes here?
#How do we update colors?

#for i, color in enumerate(colors):
    #if color == 'blue':
    #colors[i] = 'aquamarine'

#hobbies = input("What are your hobbies? ")

#if "chess" in hobbies:
    #print("Checkmate!")
#if "cats" in hobbies:
   # print("Meow!")
#color= "red"
#color = input("what is your color?")
#if color == ("red") :
 #print(f"my color")
#if color == ("blue") :
    #print(f"blue is nice to")


#Nested Questions¶

    #Sometimes one condition depends on another
weather = input("How is the weather? ")

if weather == "rain":

    coat = input("What kind of coat are you wearing? ")

    if coat == "raincoat":
        print("Good thinking!")

    else:
        print("Oh no, you'll get wet!")

else:
    print("Let's have lunch outdoors!")

    #Multiple Conditions¶

    sandwiches = int(input("How many sandwiches did you pack? "))

if sandwiches < 2:
    print("EMERGENCY! We need more food!")

if sandwiches < 4:
    print("Remember to stop at the deli")

else:
    print("Yay! We have enough food")