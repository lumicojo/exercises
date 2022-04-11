#Ask a user for their nickname
#Complain if it’s too short (less than 5 characters)
#If it’s long enough, greet the user

nickname = input("Nickname? ")

if len(nickname) < 5:
    print("That's too short!")

else:
    nickname = nickname.title()
    print("Hiya", nickname)
