
kid1 = "tom"
kid2 = "tim"
kid3 = "mark"
kid4 = "joe"
print("the", "4", "names", "are", kid1, kid2, kid3, kid4)
print(kid1)


def age():
    user_age = input("how old are you?")
    return user_age
def fav_number() :
    num = input("what is your fav number?")
    return num

def sum () :
    int_age = int(age()) 

    int_fav_number = int(fav_number())
    return int_age + int_fav_number 

print(sum())