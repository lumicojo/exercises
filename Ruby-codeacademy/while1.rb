#i = 0
#while i < 5
  #print( "value of i is :" , i)
    #i += 1
  #print "finished"
#end
###########################################


# countdown.rb
x = gets.chomp.to_i

while x >= 0
  puts x
  x = x - 1     #x -= 1 # <- refactored this line
end

puts "Done!"

