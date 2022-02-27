# prompt the user for their age
# prompt the user for their name 
# prompt the user for their lucky number 
# add their age and lucky number together
# return the sentence: carmen is 25 and her fav number is 10 and together that makes 30

name = input("what is your name?")
age = input("how old are you?")
lucky = input("what is your favorite number?")
int_age = int(age)
int_lucky = int(lucky)
total = int_age + int(lucky)
print(name, "is", age, "and her fav number is", lucky, "and together that makes", total)
