#Write a while loop that continually asks a user
#  for a number between 50 and 100.
while true 
    puts "enter a number between 50 and 100 "   
    user_num = gets.chomp
    num_int = user_num.to_i
    if num_int > 100
        puts "too high!"
    #If the user types a number less than 50,
    #  the program should say “Too low!”.
    elsif num_int < 50
        puts "too low!"
    #If the user types a number between 50 and 100, 
    else
         

        # the while loop should stop. (Hint: Use the break statement.)
        break
    end
end