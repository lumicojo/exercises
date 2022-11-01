tax_due = true
reg_due = true
while (tax_due || reg_due) do
  if tax_due
    puts "please pay taxes(y/n)"
    payment = gets.chomp
    if payment == "y"
      tax_due = false
    end
  else #if taxes no longer do
    puts "please pay registration (y/n)"
    payment = gets.chomp
    if payment == "y"
      reg_due = false
    end  
  end
end

