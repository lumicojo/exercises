scort = 1
puts "What difficulty would you like to play? Type easy or hard:"
difficulty = gets.chomp

if difficulty == "easy"
  random_number = rand(10) + 1
  level = 10
else difficulty == "hard"  
  random_number = rand(20) + 1
  level = 20
end  
puts "You pick a number between 1 #{level}. Guess the number."  
guess = gets.chomp.to_i

while guess != random_number
  puts "try again"
  score +=1
  guess = gets.chomp.to_i
end  

puts "you win"
puts "you score: #{score}"