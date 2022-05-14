name = input("what is your nickname?")
while len(name) < 5:
    print("is to short")
    name = input("what is your nickcame?")
print("nice meet you", name.title())
