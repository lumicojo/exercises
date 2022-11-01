require 'pry'
value = 0
continue = true
while continue do.to_i
  puts "please input value of sum"
  new_value = gets.chomp.to_i
  value = value + new_value
binding.pry
  puts "do you want to input another value? t/f"
  input = gets.chomp
  if input == "f"
    continue = false
    puts "sum of value is #{value}"
  end
end  