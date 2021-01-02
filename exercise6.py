# Ask for a word
word = input('Please enter a word: ').strip()


# Check if word is not empty

if word:
    if word == word[::-1]:
        print('String {} is palindrome'.format(word))
    else:
        print('String {} is not palindrome'.format(word))
else:
    print('Word should not be empty')