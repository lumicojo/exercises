#ask user for the name
name = input("what is your nickname?")
while len(name) < 5:
    print("is to short")
    name = input("what is your nickcame?")
print("nice meet you", name.title())


#Write a function that takes in a list of numbers.
#  It should return the sum of all the numbers in the list.


def add_numbers(list_of_numbers) :
    sum = 0
    for number in list_of_numbers :
     sum += number
    return sum
the_list =[1,1,1]
print(add_numbers(the_list))

