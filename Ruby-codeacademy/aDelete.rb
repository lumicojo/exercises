animal = []
# animal = ["dog", "racun", "libra", "rat", "cat"]
#we add items to empty array
animal << "dog"
animal << "racun"
animal << "libra"
animal << "rat"
animal << "cat"
puts animal

# Combine arrays 
food = ["apple", "milk", "juice", "snack"]
new_array = animal + food
# or
new_array = animal.concat(food)
puts new_array

# reference
new_array = new_array.length # 
puts new_array
new_array.first  # first item
new_array.last
new_array[1] #sec item
new_array[2] # third item
new_array[-2] # sec from the last
new_array.index("snack") # what is the index of snak


# Checking

new_array.include?("apple") #does contain apple?
new_array.include?("juice")


# Sorting

puts new_array.sort_by { |item| item.length }#by word length
puts new_array.sort  # alphabet
puts new_array.sort { |a, b| b <=> a }  # reverse alphabet order
# or
#puts strings.sort { |first_string, second_string| second_string <=> first_string}


#Check
#while loop
count = 0
while count < new_array
  puts new_array[count]
  count += 1
end

#each loop
new_array.each do |item| 
  puts item
end


# Delete
new_array.shift #delete first item
new_array.pop # delete the last item
new_array.delete("apple")
new_array.delete("juice")