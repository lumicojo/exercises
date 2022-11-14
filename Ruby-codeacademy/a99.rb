bottles = 91
while bottles >= 0
  puntuation = "."
  if bottles %10 == 0 
    punctuation = "!"
  end
  if bottles == 1
    puts "#{bottles} bottle of beer on the wall, #{bottles} bottle of beer#{punctuation}\n " "Take one down and pass it around, no more bottles of beer on the wall. \n"
    bottles -=1
  elsif bottles != 1 && bottles != 2 && bottles != 0
    puts"#{bottles} bottles of beer on the wall,#{bottles} bottles of beer#{punctuation}\n" "Take one down and pass it around, #{bottles-=1} bottles of beer on the wall.\n"
  elsif bottles == 2  
    puts"#{bottles} bottles of beer on the wall,#{bottles} bottles of beer#{punctuation}\n" "Take one down and pass it around, #{bottles-=1} bottle of beer on the wall.\n"
  else
    bottles -= 1
    puts "No more bottles of beer on the wall, no more bottles of beer.\n" "Go to the store and buy some more, 99 bottles of beer on the wall."
    
  end
end  