#write a function that asks the user for their age 

#write another function that checks the age. 
# if the user is over 21, print  can go to the club. if they’re under, 
#  printthey can’t. 

def user_age () :
    old = input("how old are you?")
    return old


def age() :
   

    int_old = int(user_age())
    if int_old  > 21 :
        print("can go to the club")
    elif int_old < 20 :
        print("can't go")

age()