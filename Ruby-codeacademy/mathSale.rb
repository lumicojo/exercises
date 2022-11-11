#write a program that informs you when you have reached $100 of sales.
puts "Enter your values here!"

total = 0.0
while total < 100 do
  puts ">"
  input = gets.chomp.to_f
  total = total + input
end
puts ("you reach 100")  

if total >= 125
  twenty_five_mores = ((total - 100) / 25).to_i
  twenty_five_mores.times do
    puts "You've earned another 25!"
  end
end