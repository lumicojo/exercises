#Use .each to iterate over the secret_identities hash.
#Use puts to print each key-value pair, 
#separated by a colon and a space (:).
secret_identities = {
    "The Batman" => "Bruce Wayne",
    "Superman" => "Clark Kent",
    "Wonder Woman" => "Diana Prince",
    "Freakazoid" => "Dexter Douglas"
  }
secret_identities.each do | item, name |
    puts " #{item} : #{name} "
end    


restaurant_menu = {
    "noodles" => 4,
    "soup" => 3,
    "salad" => 2
  }
   
  restaurant_menu.each do |item, price|
    puts "#{item}: #{price}"
  end