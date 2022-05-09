#promt the user for temp outside
#if temp is 70 and up no need jacket
#temp = input("what is the temp outside?")
#print(type(temp))
#int_temp = int(temp)

#if int_temp >= 70 :
    #print("no jaket")

#elif int_temp < 70 :
   # print("need jaket")

#promt user if they hungry.
# #if they hungry ask them what kind of   food they want.
#if they not hungry ask them if they thirsty.

hungry = input("are you hungry?")
if hungry == "yes":
    food = input("what food you want") 
    print(food)
    if food == "sushi" :
        print("go get it")
elif hungry == "no" :
    thirsty =  input("are you thirsty")
    if thirsty == "yes":
        print("go get it")

