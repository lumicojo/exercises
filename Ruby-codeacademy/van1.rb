# puts "What items  would you like "
# item = gets.chomp
# puts "How many items do you like "
# amount = gets.chomp.to_i
# amount.times do |amount|
#   puts item
# puts "Here you go !"
# end

puts "What would you like? "
item = gets.chomp
puts "How many?"
amount = gets.chomp.to_i
if amount == "tons"
  amount = rand(20) + 1
  amount.times do |amount|
    puts item
  end
else amount.to_i.times do
  puts item
  end  
end
puts "There you go!"
