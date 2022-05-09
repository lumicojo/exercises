#def animal_list() :
   #return ["cat","rat","dog"]

#print(animal_list())

# write a function that asks the user for their favorite animal and make sure you return it
# write a second function that takes that favorite animal
#  and print “cats are cool” if their favorite animal is “cat”,
#  “dogs are awesome” if their favorite animal is dog,
#  and “I’m sure your animal is cool” if they write something else. 
#Then call the function 

def fav_animal() :
    animal = input("what is your fav_animal?")
    return animal


def fav_pet() :
    animal = fav_animal()
    if animal == "cat":
        print("cats are coll") 
    elif animal == "dog" :
        print("dogs are awesome")    
    

fav_pet()