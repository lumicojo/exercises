puts "Enter some text: "
user_input = gets.chomp

puts "Enter words to redact: "
user_redact = gets.chomp

input_words = user_input.split(" ")
redacted_words = user_redact.split(" ")
input_words.each do |current_input_word|
  redacted = false
  redacted_words.each do |current_redact_word|
    if current_input_word == current_redact_word
      redacted = true
    end 
  end 
  if redacted
    print "REDACTED "
  else
    print current_input_word + " "
  end       
end 


