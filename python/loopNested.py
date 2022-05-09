#Sometimes one condition depends on another
weather = input("how is the weather?")
if weather == "rain":
    coat = input("what kind of coat are you wearing?")
    if coat == "raincoat":
        print("good thinking!")
    else:
         print("o no, you'll get wet!")   
else:
    print("let's have lunch outdoors!")         

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