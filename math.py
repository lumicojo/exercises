# set two variables to the numbers 5 and 3
# set another variable called answer. the value will be the sum of the two variables (5+3)
# print the answer as a string

digit1 = "5"
digit2 = "3"
print(type(digit1))
print(type(digit2))

digit1_int = int(digit1)
digit2_int = int(digit2)
print(type(digit1_int))
print("this are str addet together ", digit1+digit2)
print("this are int added together", digit1_int + digit2_int)
answer_int = digit1_int + digit2_int
answer_str = str(answer_int)
print(answer_str)
print("this a string str ",answer_str)