# Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
#  If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
#  Write a Python program to solve the general version of the above problem.
#  Ask the user for the time now (in hours), and then ask for the number of hours 
# to wait for the alarm. Your program should output what the time will be on the clock
#  when the alarm goes off.
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