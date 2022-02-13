#print(13+50)#63
#print (63%24)#15

#there are 24 hours in a day.
#ask user what time it is (current time)
#we want to ask the user how many hours before alarm goes off (wait_time)
#then we need to find the remainder of wait time and 24 hours
# print (int("1"))
current_time_str = input("what time is It?")
print(current_time_str)
print("current time str", type(current_time_str))
current_time_int = int(current_time_str)
print("current time int", type(current_time_int))
wait_time_str = input("How long until alarm goes off?")
print(wait_time_str)
print("wait time str", type(wait_time_str))
wait_time_int = int(wait_time_str)
print("wait time int", type(wait_time_int))

total_time = current_time_int + wait_time_int
print(total_time)
alarm = total_time % 24
print(alarm)