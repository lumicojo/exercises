#List that you can do with it pet 
#["fetching","walking"," staying_indoor",]
#If Y go loop thru list and print out each 

#pet_list = [f"fetching,walking, staying_indoor",]

pet_activities = ["fetch","walk", "play indoors",]
  

#Prompt  the user for their pet's name.
pet_name = input("What is your pet name?" )

#Ask them if they like to play fetch.
pet_fetch = input("Does your pet play fetch ?") 

#Ask user if the pet listen to commands    
listen = input("Does your pet listen?" )
listen = listen.upper()

if(listen == "Y") : 
    print(" he get's a treat,long walk to the park to play.")  
elif(listen == "N") :
    print("he  don't listen he get's nothing")
    
#If it’s cold rainy day we stay in and play
weather = input("How is the weather, rainy  or sunny?" ) 

if(weather == "rainy" ) :
     print("we stay in doors and play")
elif(weather =="sunny") :
    print("Let's go for walk.")
else: 
   print("wrong ")

fun_day = input(f"do you want to treat {pet_name} to a fun day ? Y/N ")
if(fun_day == "Y") :
    for pet_activity in pet_activities :
        print(f"let's go for a {pet_activity}")
else :
    print("wrong answer the pet deserve a fun day")