supply_list = "spaceship supply list\n"
items = "food, drinks, medicine"
total = 0
input = ""
while input != "done" do
  print "What items do you like to add to the list, (or are you 'done'): "
    input = gets.chomp
    if input != "done"
    supply_list += "* #{input}\n"
  end
  puts "\n\n"
  puts supply_list
end

total = 0.0
input = nil
while input != "done" do
  print "\n  current total is: $ #{total} "
  print "What is the cost of the item? (enter 'done' when finished) \n> "
  input = gets.chomp
  if input != "done"
  total = total += input.to_f
  end
end
puts "\n\n"
puts " The total is: #{total}"  
