
bottles = 99
while bottles > 0
  if bottles == 0
    puts "No more bottles of beer on the wall no more bottles of beer. \n" "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
  elsif bottles == 1  
    puts "puts #{bottles} bottle of beer on the wall #{bottles} bottle of beer \n "  "Take one down and pass it around, no more bottles of beer on the wall." 
    bottles -= 1
  else 
    puts "#{bottles} bottles of beer on the wall #{bottles} bottles of beer \n " "Take one down and pass it around, #{bottles -=1} bottles of beer on the wall. \n "
  end
end

