#make sure your redactor redacts a word regardless of whether it’s upper case or lower case
#make your program take multiple, separate words to REDACT
#How might you make a new redacted string and save it as a variable, rather than just printing it to the console?

puts "Enter some text: "
text = gets.chomp

puts "Enter words to redact: "
redact = gets.chomp

words = text.split(" ")
remove = redact.split(" ")
words.each do |word|
  redacted = false
  remove.each do |redact_word|
    if word == redact_word
      redacted = true
    end 
  end 
  if redacted
    print "REDACTED "
  else
    print word + " "
  end       
end 


