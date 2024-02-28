# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 02/28/2024
# Description: Project 8a

def count_letters(string):
    # Dictionary to store letter counts
    letter_dict = {}

    # Iterate through each character in the input string
    for char in string:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Convert the letter to uppercase for case-insensitivity
            char = char.upper()

            # Update the letter count in the dictionary
            # If the letter is not in the dictionary, get() returns 0
            letter_dict[char] = letter_dict.get(char, 0) + 1

    # Return the final letter count dictionary
    return letter_dict
