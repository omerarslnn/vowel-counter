def count_vowels(word):
    vowels = "aeiou"
    count = 0
    for letter in word.lower():
        if letter in vowels:
            count += 1
    return count


# Taking input from the terminal
word = input("Enter a word or phrase to count vowels: ")
vowel_count = count_vowels(word)

print(f"The number of vowels in '{word}' is {vowel_count}.")
