#Use puts to prompt the user for input two times.
# For the first puts, declare a variable called text and
# set it equal to the user’s input via gets.chomp.

#For the second puts, declare a variable called redact 
#and set it equal to the user’s input using gets.chomp.
puts "Enter some text: "
text = gets.chomp

puts "Enter words to redact: "
redact = gets.chomp
#Declare a variable called words and set it equal to the result of calling
# the .split method on text.
 #Pass .split a space (" ") to use as a delimiter so that 
 #we get an array made up of the words from text.
 words = text.split(" ")
 #Let’s start simple: write an .each loop that iterates through words
 # and just prints out each word it finds.
 words.each { |word|
     
#Add an if/else statement inside your .each.
#if the current word equals the word to be redacted, then print "REDACTED " with that extra space.
#Otherwise (else), print word + " ".
#The extra space in both cases prevents the words from running together. 

    if word == redact   # condition
        print "REDACTED"  # take this action
    else
        print word + " " # take this other action
    end }   