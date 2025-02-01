# # Function to square a number
# def square(x):
#     return x * x

# # List of numbers
# numbers = [1, 2, 3, 4, 5]

# # Using map to apply square function to each element
# squared_numbers = map(square, numbers)

# # Converting map object to a list to see the result
# print(list(squared_numbers))



def process_words(words):
    
    words = [word for word in words if len(word) >= 5]
    
    vowels = "aeiouAEIOU"
    number_of_vowels = []
    number_of_consonants = []

    for word in words: 
        vowels_count = sum(1 for char in word if char in vowels)
        consonants_count = sum(1 for char in word if char.isalpha() and char not in vowels)
        number_of_vowels.append(vowels_count)
        number_of_consonants.append(consonants_count)

    
    return words, number_of_vowels, number_of_consonants

words = ["fhghsdfa", "aeinfh", "tuanhia"]
result = process_words(words)
print(result)
