# Mars Adventure
user = input("what is your name?")

print(f"hi, {user} welcome to Mars Adventure") 
print("are you excited? Y or N")
excited = input("> ")
excited = excited.upper()

if excited =="Y":
  print("I knew you'd that.It's so cool that you're gong to Mars!")
  
if excited =="N":
  
  print("Well, it's too late to back out now.")
print("It's time to pack for your trip to Mars.")  
print("How many suitcases do you plan to bring?")

num_suitcases = input("> 2")

num_suitcases = int(num_suitcases)

if num_suitcases > 2:
  
  print("That's way too many. You'll have to pack more lightly.")
  print("Please try to fit your stuff into 2 suitcases.")
else:
  print("Perfect.You’ll certainly fit in the spaceship!")

 # Companion Animal
print("You're allowed to bring one companion animal with you.")

print("What kind of companion animal would you like to bring?")
companion_type = input("> ")

print("What is your companion's name?")
companion_name = input("> ")
companion_name = companion_name.title()
print("Cool so you are bringin Mogly the dog")

#Spaceship Decor

decor = "blue_light's"
decor2 = "retro"
decor = input("what decoration are you using? ")
print(f"I am using {decor}  and {decor2}")