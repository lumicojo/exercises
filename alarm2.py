# Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
#  If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
#  Write a Python program to solve the general version of the above problem.
#  Ask the user for the time now (in hours), and then ask for the number of hours 
# to wait for the alarm. Your program should output what the time will be on the clock
#  when the alarm goes off.

start_time = input("what time is it?") #9
wait_time = input("how many hours until the alarm goes off?")#50
start_time_int = int(start_time) 
wait_time_int = int(wait_time)
final_time_int = (start_time_int+ wait_time_int)
print(final_time_int)
result = final_time_int % 24
print(result)



