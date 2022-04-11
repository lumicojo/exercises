while True:
    name = input("wath is your name?")
    name = name.title()
    if len(name) >= 5:
        break
    print("is to short")
print("hi", name)
print(f"hi {name} ")