30.times { print "Ruby!" }
i = 0
loop do
  print "Rubu"
  i += 1
  break if i == 30
end  
i = 3
while i > 0 do
  print i
  i -= 1
end
 
j = 3
until j == 0 do
  print j
  j -= 1
end

numbers = [1, 2, 3, 4, 5]
 
# one way to loop
numbers.each { |item| puts item }
 
# another way to loop
numbers.each do |item|
  puts item
end
odds = [1,3,5,7,9]

# Add your code below!
odds.each do |x|
 x *= 2
 print "#{x}"
end 
