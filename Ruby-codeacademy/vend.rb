
# puts "What items do you want to get? "
# input = gets.chomp

# puts "How many items? "
# items_number = "number"
# items_number = gets.chomp

# puts "There you go come back again!"

puts "What items do you want to get? "
item = gets.chomp
puts "How many ? "
amount = gets.chomp

if amount.include?("tons") 
  number = rand(20) + 1
  puts number
  number.times do
    puts item
  end
else 
  amount.to_i.times do
    puts item
  end
end
puts "There you go"








# 20.times do |item|
#   puts "Here is your #{item}"
# end  
# puts "There you go here is your order come back again!"
