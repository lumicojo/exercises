
# change this code
mystring = "hello"
myfloat = 10,0
myint = 20


# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)


nmbers = [1]
strings = [2]
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = "Eric"


# this code should write out the filled arrays and the second name in the names list (Eric).
print(nmbers)
print(strings)
print("The second name on the names list is %s" % second_name)

helloworld = "hello" + " " + "world"
print(helloworld)


x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

#You will need to write a format string 
# which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)