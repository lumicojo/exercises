#make a variable called items,
# assign it to array containing spatula, pot, and pan. 
# iterate through each of your list and print  #“i’m using the pot” and “i’m using the pan”.
#“i’m using the spatula” and
#“i’m using the pot” and “i’m using the pan”
#remember to use interpolation 

items = ["spatula", "pot", "pan"]
items.each do |item| 
    puts "I am using #{item}"
end


