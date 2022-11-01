#ask user what is the every day rutine
#make a list of rutine 

plans = ["coffe", "breakfast", "walkin the dog", "work." ]
question = true
while question
    puts " guess  day plans. "
    user_input = gets.chomp
    plans.each do |plan|
        if user_input == plan
            puts "that's my plan"     
            question = false 
            break 
        end   
    end
end    