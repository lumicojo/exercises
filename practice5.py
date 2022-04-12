#Write a while loop that continually asks a user for a number between 50 and 100.

#If the user types a number greater than 100, the program should say “Too high!”.

#If the user types a number less than 50, the program should say “Too low!”.

#If the user types a number between 50 and 100, the while loop should stop. (Hint: Use the break statement.)

while  True:
    num = input("enter a number between 50 and 100 ")
    num = int(num)
    if num > 100:
        print("to high")
    if num < 50:
        print("to low")  
    if num > 50 and num < 100 :
        break