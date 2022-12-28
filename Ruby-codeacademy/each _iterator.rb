#Use the .each method on the odds array to print out double the value of each item of the array. 
#In other words, multiply each item by 2
#.Make sure to use print rather than puts, so your output appears on one line.



numbers = [18,33,5,7,9]
multiplay_numbers = numbers.select{ |n| 2 * n == 0}
puts multiplay_numbers
end