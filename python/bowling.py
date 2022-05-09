
#write a function ask the user how old they are
def age() :
    user_age = input("how old are you?")
    return user_age

def old_enough() :
    if int(age()) >= 10 :
        print("old enough to go bowling")
    else :
        print("to young")   

old_enough()

