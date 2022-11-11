numbers = [1, 2, 3, 4, 5]
current_index = 0
max_index = numbers.length - 1

while current_index <= max_index
  puts numbers[current_index]
  current_index += 1
end

puts "My to do list:"
to_do = ["buy soy milk", "learn about arrays", "learn ruby"]
i = 0
while i < to_do.length
  print " * "
  puts to_do[i]
  i += 1
end  


numbers = [1, 2, 3, 4, 5]

numbers.each do |number|
  puts number
end

puts "My To Do list:"
to_do = ["buy soy milk", "learn about arrays", "learn ruby"]

to_do.each do |item|
  print " * "
  puts item
end


doubled_numbers = []

numbers.each do |number|
  doubled_numbers << number * 2
end
doubled_numbers.each do |number|
  puts number
end


#  One Liners

#numbers.each do { |number| puts number}

names_to_greet = ['Sally', 'Samee', 'Suzi']
names_to_greet.each { |name| puts "Hi #{name}"}


#loops through an array to find names that start with 'B'.
["Bridget", "Barney", "Sam", "Ella"].each do |name|
  if name.index('B') == 0
    puts "#{name} starts with 'B"
  end
end  

#              or

["Bridget", "Barney", "Sam", "Ella"].each {|name| puts (name.index('B') == 0) ? "#{name} starts with 'B'" : "" }
