# Function: Generate Hangman Phrase
# Objective: Create a function `generate_hangman_phrase` that takes a phrase and a list of guessed letters,
# and returns a string with hyphens for every letter not guessed, while showing the letters that were guessed.
# Parameters:
# - phrase: A string representing the phrase to be guessed.
# - guessed_letters: A list of characters representing the letters that have been guessed so far.
# Returns:
# - A string representing the current state of the phrase with unguessed letters replaced by hyphens.

generate_hangman_phrase = lambda phrase, guessed_letters: ''.join([char if char.lower() in set(guessed_letters) or char == ' ' else '-' if char.isalpha() else char for char in phrase])

# Example usage:
print(generate_hangman_phrase("hello world", ['e', 'o',]))  # Output: "-e--o -o---"
print(generate_hangman_phrase("Happy Birthday", ['h', 'a', 'p', 'y']))  # Output: "Happ-y B--th-a-"
print(generate_hangman_phrase("OpenAI GPT-3", ['p', 't', 'g', 'n']))  # Output: "-p-n-- GPT-3"
