numbers = [1, 3, 5, 7]
numbers.each { |n| puts n }
#“For each element in numbers print its value.”

#with hash
hash = { bacon: 300, coconut: 200 }
hash.each { |key,value| puts "#{key} price is #{value}" }

# Each With Index
animals = ["cat", "dog", "tiger"]
animals.each_with_index { |animal, idx| puts "We have a #{animal}
 with index #{idx}" }

10.times { puts "hello" }

#Range Looping
(1..10).each { |i| puts i }

#Iterations With The Next
10.times do |i|
next unless i.even?
puts "hello #{i}"
end

#  A better way to do this is to use other methods like step & select.
(0...10).select(&:even?)
# [0, 2, 4, 6, 8]

##  How to Stop A Loop Early
numbers = [1,2,4,9,12]
numbers.each do |n|
    break if n > 10
    puts n
  end

#The upto method
 1.upto(5) { |i| puts i }  
