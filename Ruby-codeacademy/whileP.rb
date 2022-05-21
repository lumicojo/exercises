#ask user for temperature outside
#if is over 50 but or under 60 print you need a jaket
#if is over 60 and under 70 print you need a hoodie
#if is 70 you need short's
play_game = true
while play_game
    print "guess the temp outside? "
    temp = gets.chomp 

    int_temp = temp.to_i
    if int_temp > 50 and int_temp <= 60 
        print "you need jacket" 
    elsif int_temp > 60 and int_temp <= 70 
        print "you need a hoodie " 
    elsif int_temp > 70
        print "you need a short's"
        play_game = false
    else 
        puts "try again "   
    end

end    