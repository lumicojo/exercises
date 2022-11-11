#rewrite your while loop using until. You still want to print out the numbers 1 through 50, inclusive.
#counter = 0
#while counter >= 50
    #print counter
    #counter -= 1
  


i = 1
until i == 51
  print i
  i += 1
end


x = gets.chomp.to_i
until x < 0
    puts x
    x -= 1
end 
puts "finish"   