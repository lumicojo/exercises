#In your notes, complete the following python program meant
#  to ask a user for their favorite color, and then compliment them accordingly.

color = "blue"
color2 = "red"
color = input("what is your favorite color")
if "red":
   print("I like red too!")
if "blue":
    print("Blue is cool too")
 
# Input exercise
# Ask the user what their favorite color is
# print the user's favorite color
# ensure that favorite color is all lower case

fav_color = input("What's your favorite color? ")
fav_color = fav_color.lower()

if fav_color == "purple":
  print("Me too!")
else:
  print(f"Oh, {fav_color} is a nice color too!")

# # Getting length of color string
color_len = len(fav_color)
print(f"length of color string: {color_len}")

