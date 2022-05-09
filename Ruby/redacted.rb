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


