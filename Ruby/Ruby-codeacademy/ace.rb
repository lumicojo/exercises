#Greet the customer.
##Ask how many adult tickets they would like.
#Accept the user's answer and save it as a variable.
#Ask how many child tickets they would like.
#Accept the user's answer and save it as a variable.
#Print a sentence returning the number of adult and child tickets the user has asked for.
customer = "hello"
puts "how many adult tickets you like "
adult_tickets = gets.chomp
puts "how many child tickets you like "
child_tickets = gets.chomp
puts "here are your " + adult_tickets + "adult_tickets and " + child_tickets + "child_tickets!"

#menu Two hamburgers and two ice cream sandwiches
      #Eight funnel cakes and a hot dog
      #Three of each item on the menu

hot_dog = 1.27
hamburger = 4.17
funnel_cake = 3.79
ice_cream_sandwich = 0.75

puts hamburger * 2 + ice_cream_sandwich * 2 
puts funnel_cake * 8 + hot_dog 
puts (hot_dog + hamburger + funnel_cake + ice_cream_sandwich) * 3