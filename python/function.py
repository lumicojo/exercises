#def sum(arg1, arg2):
   # if type (arg1) != type(arg2) :

      # print("please give the args of same type")
       #return
    #return (arg1 +arg2)

#a = sum(15,60) #integr  colling a function
#print(a)
#print(sum('hello','word')) #string 
#print(sum(15.647, 80.258))  #floot 
################

def student(name ='Unknown name', age = 0) :
    print("name:",name)
    print("age", age)

student('tom',22)


def student(name , age , *marks) :
    print("name:",name)
    print("age", age)
    print(marks)
    
    student('tom', 22, 95, 70, 80, 50)



A = [1, 5, 23, 89, 11, 84, 5] #list
def list (integers) :
  print(integers)



 #Variable inside of function

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
