#s = [["ham", "swiss"], ["turkey", "cheddar"], ["roast beef", "gruyere"]]

#if u want to acces swiss == s[0][1]== sec element of first element.
#Puts out every element inside the sub-arrays inside s.

#Iterate through .each element in the s array. 
#Call the elements sub_array.
#Then iterate through .each sub_array and puts out their items.
sub_array = [["ham", "swiss"], ["turkey", "cheddar"], ["roast beef", "gruyere"]]
sub_array.each{|sub_array| puts "{sub_array}\n"}