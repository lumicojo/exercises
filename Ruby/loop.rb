#Create an array of animals, cat, snake, wolf, dog, giraffe, elephant. 

#ask the user to guess an animal that is in your list 

#Loop through your animals to see if the animal they chose is one of the animals in your list.

#if it is, print, “that’s an animal in my list” and end the loop

#If they guess wrong, ask the user again to guess an animal until they guess one in your list. 
animals = ["cat", "snake", "wolf", "dog", "giraffe", "elephant." ]
puts "guess a animal ."
user_input = gets.chomp
play = true
while play
    animals.each do |animal|
        if user_input == animal
            puts "that's  an animal in my list"
        play = false
            break
        end
    end    
end