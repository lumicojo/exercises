word = ["boo", "a", "I", "hi"]
def get_longest_word(words) :
 
  longest_word = ""
  for word in words :
   if len(word) > len(longest_word) :
      longest_word =word
      return word
      print(get_longest_word(words))
  def my_pet(name):
    #the function is called my_pet and it is expecting an argument called name
   if name == "Sushi":
    print("That's Lumi's dog!")
   elif name == "Elsa":
    print("That's Roxy's cat!")
   elif name == "Mogli":
    print("That's Carmen's dog!")
   else:
    print("That's not anyone's pet!")

# below on line 20, you are calling the function and passinbg in "Sushi" as the name
 #my_pet("Sushi")

words = ["one", "two", "superduper", "dog"]
def get_longest_word(words):
    longest_word = ""

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


    print(get_longest_word(words))


