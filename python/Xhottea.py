#If our tea is too hot, we’ll add a chip of ice

#Keep checking if it’s too hot and keep adding ice until it’s perfect

#tea_temperature = 115
#while tea_temperature > 112:
   # print(tea_temperature)
    # add a chip of ice
   # tea_temperature = tea_temperature - 1
 #What if we mistakenly wrote + instead of -?

#tea_temperature = 115

#while tea_temperature > 112:
  #  print(tea_temperature)
    # add a chip of ice
   # tea_temperature = tea_temperature + 1   
  ##  break
#A Useful While Loop
#meals = []

#while True:
   # meal = input("Meal ['exit' to quit] > ")

   # if meal == "exit":
      #  break

   # else:
       # meals.append(meal)

#print("Your meals are", meals)
#while True: repeats forever (or until a break statement)

#break: immediately exits loop

good_job = "congratulation"
smaily_face = (":")
good_job2 = good_job.upper()
print(good_job ,smaily_face)


#Write a while loop that counts to 5.


num = 0
while  num < 5 :
    num += 1
    print(num)


#user = input("what is your name?")
#print("wellcome",user)

while True :
    
    count = input("give me a number between 50 and 100" )
    int_count = int(count)
    if int_count > 100 :
       print("too high")
    elif int_count < 50 :
        print("too low")
    elif int_count < 100 and int_count >50 :
        #while loop sould 
        break


