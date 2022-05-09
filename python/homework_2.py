####Conditional

# 1
#Solve the following problems using conditionals.
#Write an if-else statement. It should print “longer than 15 characters”
#  if the sentence is longer than 15 characters, 
# and “not longer than 15 characters” if it’s not.
sentence = "Time flies when you're coding."
if len(sentence) > 15 :
    print(" longer then 15 charactes")
else :
    print("“not longer than 15 characters”")
  #############################################################  
# 2
#We’ll write a basic calculator program 
# that either adds or subtracts 2 numbers provided by the user.
#  Copy the following code into your Repl session to get started:
#Prints the correct mathematical answer 
# if the user provides 2 numbers and a + or -.

#Prints “Sorry, can only add or subtract” 
# if the user types something other than + or - for the operator.

print("Welcome to the adder-subtractor!")

num1 = input("What is number 1? ")
num2 = input("What is number 2?")

num1_int = int(num1)
num2_int = int(num2)

print("Would you like to add or subtract those numbers?")
print("Please type + or -")

operator = input("> ")
if operator == ("+") :
    print(num1_int + num2_int)
elif operator == ("-") :
    print(num1_int - num2_int)
else : 
    print("Sorry, can only add or subtract")

# 3
#In order to enter the competition, their croissant must:
#Have at least 6 layers
#Be crescent-shaped
#Have a golden brown color
croissant_1 = ["Yao", 4, "golden brown", "crescent"]
croissant_2 = ["Alana", 33, "golden brown", "crescent"]
croissant_3 = ["George", 27, "golden brown", "crescent"]
croissant_4 = ["George", 27, "light brown", "rectangle"]

#We can interpret the lists as having the following data:
#Index 0     Name of baker
#Index 1      Number of layers
#Index 2      Croissant color
#Index 3       Shape
#Write 4 conditionals that will each programmatically determine 
# if each of those bakers are eligible to enter the Croissant Competition.
 
if croissant_1[1] >= 6 and croissant_1[2] == "golden brown" and croissant_1[3] == "crescent" :
    print(f"{croissant_1[0]} is eligible")
else :
    print(f"{croissant_1[0]} not elegible")

if croissant_2[1] >= 6 and croissant_2[2] == "golden brown" and croissant_2[3] == "crescent" :
    print(f"{croissant_2[0]} is eligible")
else :
    print(f"{croissant_2[0]} not elegible")

if croissant_3[1] >= 6 and croissant_3[2] == "golden brown" and croissant_3[3] == "crescent" :
    print(f"{croissant_3[0]} is eligible")
else :
    print(f"{croissant_3[0]} not elegible")

if croissant_4[1] >= 6 and croissant_4[2] == "golden brown" and croissant_4[3] == "crescent" :
    print(f"{croissant_4[0]} is eligible")
else :
    print(f"{croissant_4[0]} not elegible")


#  L00PS

# 1

#First, write a for-loop that prints out each student in the list.


students = ["Julia", "Sarah", "Andy", "Charlotte", "Taylor", "Sam"]

for student in students :
    print(student)

# 2
count = 0
while count < len(students) :
    print(count)
    count +=1

# 3
students = ["Julia", "Sarah", "Andy", "Charlotte", "Taylor", "Sam"]  
students.sort()

for student in students :

    print(student)

