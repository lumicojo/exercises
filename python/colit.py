#In order to hold the books in Brighticorn’s Library, 
# we’ll use a list. We’ll create it already holding two of Brighticorn’s favorite books:
# List we'll use for all of the books in library
# print welcome title

books = ["Dune", "Pride and Prejudice"]
print("Brighticorn's Books")
print("--------------")
print("Wellcome, Barighticorn's Books")

 #print out a menu of choices, like “You can add / view /check / exit”

#prompt the user for a command and save what they entered as the variable command

#print out the command they entered, so if they entered “add”, 
# it should print “Action: add”

while True:  

    print("You can: add / view / check / exit")
    command = input("action > ")
    command = command.lower()

    print("Action:", command)
# just the general structure of “if they said ‘add’,
#  here’s where the block of code would go to handle that”
    if command == "exit":
        print("Goodbye!")
#That will check for the exit command in our user’s input.
#Finish writing your conditional code so that it handles all of these commands: 
# If what the user entered doesn’t match any of these options,
#  make sure the program prints “Sorry, that’s not an option”.

       
        break
    
    elif command == "add":
        print("Add Book")
        book = input("Title > ")
        books.append(book)
        print("Added", book)
    
    elif command == "view":
        print("View Books")
        for book in books:
            print(book)
        print("End of listing")

    elif command == "check":
        print("Check for a Book")
        to_check = input("Title > ")

        if to_check in books:
            print("Found:", to_check)
      
        else:
            print("Not found")
      
    else:
        print("Sorry, that's not an option")
