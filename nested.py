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
