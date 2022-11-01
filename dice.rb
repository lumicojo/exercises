# play = ""
# puts "Roll the dice , y/n "
# input = gets.chomp
# if input == "yes"
#   dice_1 = rand(6) + 1
#   dice_2 = rand(6) + 1
#   total = dice_1 + dice_2
#   puts "you rolled a#{dice_1} && #{dice_2}  "
#   puts "total: #{total}"
# else
#   puts " ok to stop"
# end  


continue = true
while continue do
  puts "How many sides your dice have? "
  user = gets.chomp
  puts "How many times you like to roll your pair of dice? "
  input = gets.chomp.to_i
  input.times do
  dice_1 = rand(6) + 1
  dice_2 = rand(6) + 1
  total = dice_1 + dice_2
  puts "you rolled a#{dice_1} and #{dice_2}  "
  puts "total: #{total}"
  end
  puts "rolled again? (y/n)"
  response = gets.chomp
  if response == "n"
   continue = false
  end
end





