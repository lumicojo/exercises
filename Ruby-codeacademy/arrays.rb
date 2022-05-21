#print the third value of demo_array to the console.
demo_array = [100, 200, 300, 400, 500]

print demo_array[2] # Add your code here!

string_array = ["These", "are", "some", "strings"]
multi_d_array = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

multi_d_array.each { |x| puts "#{x}\n" }
my_2d_array = [[1, 2, 3, 4, 5], ["Here", "are", "some", "strings"], [true, false]]

numbers = [1, 2, 3, 4, 5]
 
# one way to loop
numbers.each { |item| puts item }
 
# another way to loop
numbers.each do |item|
  puts item
end

odds = [1,3,5,7,9]

# Add your code below!
odds.each do |x|
 x *= 2
 print "#{x}"
end 

numbers = [1, 2, 3, 4, 5]
numbers.each { |element| puts element }