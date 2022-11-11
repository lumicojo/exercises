# print "specify y/n: "
# yes_or_no = gets.chomp
# insted the duplicate the statement
#conditional

#a,b,c,y
#trace:yes_or_no = nil, a, b, c,=true  y = false 
yes_or_no = nil
while yes_or_no != 'y' && yes_or_no != 'n'
 # require 'pry'
  #binding.pry

print "specify y/n: "
# operation that can potentially chage the conditional
yes_or_no = gets.chomp
end



puts "enter.."
random_number = 0
while random_number != 4
  puts "we are in"
  random_number = rand(4) + 1
end 
puts "out"  

puts "enter.."
random_number = 0
while random_number != 6
  puts "we are in"
  random_number = rand(6) + 1
  puts "you rolled a #{random_number}"
end 
puts "out"  



puts "do 3 laps!"
lap_count = 0
while lap_count < 3
  puts "Now doing lap #{lap_count}"
  lap_count = lap_count + 1
end  
puts "we're out of the loop"

############  or

3.times do |lap_count|
  puts "Now doing lap #{lap_count}"
end 
puts "we're out of the loop" 