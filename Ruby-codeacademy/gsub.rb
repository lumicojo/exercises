First, you’ll need a string to play with this method.
Because the whole point of gsub is to replace parts of a string.
The “sub” in “gsub” stands for “substitute”, and the “g” stands for “global”.

str = "white chocolate"     # = "white chocolate"

str.gsub("white", "dark")    # = "dark chocolate"


Replace Patterns With A Regular Expression

"a1".gsub(/\d/, "2")      # ="a2" In this case, \d looks for numbers, like the number “1” in “a1”.
# or
"a1".gsub(/(\w)(\d)/, '\2\1')     # = "1a"  we switched order
#We can use the groups as \1 for the first group, \2 for the second group, etc.


Advanced Gsub With Blocks
Instead of using a static value.

"dog".gsub(/\w+/) { |animal| animal == "dog" ? "cat" : "dog" }
#We find the animal with \w+, which means “one or more alphanumeric characters”.
# If it’s a “dog”, we replace it with “cat”
# If the word is anything else, we replace it with “dog”


Replace Multiple Terms With A Hash

If you have a list of substitutions to make you can use a hash.
colors = {
  "B" => "blue",
  "G" => "green",
  "R" => "red"
}  #=  {"B"=>"blue", "G"=>"green", "R"=>"red"}
#This works like a translation dictionary, where the keys will be replaced by their values.
Exemple:

"BBBGR".gsub(/\w/, colors)  # =="bluebluebluegreenred"

gsub allows you to replace, or substitute characters inside a string.


Removing invalid characters (by making the 2nd argument an empty string)
Replacing placeholders & acronyms by their full values
Using patterns & logic to change a string

