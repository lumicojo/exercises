#Write a function that takes in a list of numbers.
 #  If it has more even numbers than odd numbers, return "even".
 #  If it has more odd numbers than even numbers, return "odd".
 #  If there's a tie, return "even and odd".
 
def more_evens_or_odds(nums):
    count_evens = 0
    count_odds = 0

    for num in nums:
        if num % 2 == 0:
            count_evens = count_evens + 1
        else:
            count_odds = count_odds + 1

    if count_evens > count_odds:
        return 'even'
    elif count_odds > count_evens:
        return 'odd'
    else:
        return 'even and odd'

#Write a function that takes in a list of numbers. 
# The function should return a new list of those items, 
# in the same order, but with any duplicates removed.
#remove_dupes([1, 4, 1, 1, 3])
def remove_dupes_number(numbers):
    #Return new list of numbers with duplicates removed.
     result = [] 
     for num in numbers:
        if num not in result:
            result.append(num)

     return result
     print(remove_dupes([1, 4, 1, 1, 3]))


 #Show Even Numbers' Indices
#Write a function that takes in a list of numbers. 
# The function should return a list of the indices of all numbers
#  which are even.

#>>> show_even_indices([2, 4, 6, 8])
#[0, 1, 2, 3]
def show_even_indices(nums):
    """Given list of ints, return list of *indices* of even numbers in list."""

    indices = []

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            indices.append(i)

int(show_even_indices([7, 3, 11])) 