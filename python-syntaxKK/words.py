def print_upper_words(words, start_letters):
    """
    Print words on separate lines in all uppercase if they start with one of the specified letters.

    Parameters:
    - words: list of words
    - start_letters: set of letters to filter words

  """
    
    for word in words:
        if word[0].lower() in start_letters:
            print(word.upper())

# Test Case
word_list = ['apple', 'always', 'orange', 'elephant', 'ear']
print_upper_words(word_list, {'a', 'e'})
